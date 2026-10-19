import xml.etree.ElementTree as ET
import re
import requests
from typing import List, Dict, Any, Optional
from bs4 import BeautifulSoup

RSS_FEEDS = {
    "politica": [
        "https://feeds.bbci.co.uk/portuguese/rss.xml",
        "https://g1.globo.com/rss/g1/politica/",
        "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml"
    ],
    "mundo": [
        "https://feeds.bbci.co.uk/portuguese/rss.xml",
        "https://news.un.org/feed/subscribe/pt/news/all/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    ],
    "tecnologia": [
        "https://g1.globo.com/rss/g1/tecnologia/",
        "https://feeds.bbci.co.uk/portuguese/rss.xml"
    ],
    "oficiais_brasil": [
        "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml",
        "https://www.camara.leg.br/noticias/rss/ultimas-noticias"
    ],
    "oficiais_mundo": [
        "https://news.un.org/feed/subscribe/pt/news/all/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://feeds.bbci.co.uk/portuguese/rss.xml"
    ]
}

class NewsFetcher:
    @staticmethod
    def fetch_full_article(url: str) -> Optional[Dict[str, Any]]:
        """Extrai o texto original autêntico diretamente da página da BBC, G1 ou NYT sem alucinações."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        try:
            resp = requests.get(url, headers=headers, timeout=6)
            if resp.status_code != 200:
                return None

            soup = BeautifulSoup(resp.content, "html.parser")

            # Extrai imagem principal autêntica da matéria via OpenGraph ou Twitter Card
            og_img = (
                soup.find("meta", {"property": "og:image"}) or
                soup.find("meta", {"name": "twitter:image"}) or
                soup.find("meta", {"property": "twitter:image"})
            )
            image_url = og_img.get("content") if og_img else None

            # Remove tags irrelevantes ou poluidoras do corpo de texto
            for tag in soup(["script", "style", "nav", "header", "footer", "aside", "figure", "form", "noscript"]):
                tag.decompose()

            # Busca autor se disponível
            author = None
            author_tag = (
                soup.find("meta", {"name": "author"}) or
                soup.find("meta", {"property": "article:author"}) or
                soup.find(class_=re.compile(r"byline|author-name|content-publication-data__from", re.I))
            )
            if author_tag:
                author = author_tag.get("content") or author_tag.get_text().strip()

            # Extrai parágrafos genuínos de corpo de texto
            paragraphs = []
            junk_terms = [
                "cookies", "termos de uso", "inscreva-se", "leia mais:", "vídeos mais vistos",
                "compartilhe no whatsapp", "todos os direitos reservados", "foto:", "— foto",
                "reprodução", "crédito:", "clique aqui", "assine já"
            ]

            for p in soup.find_all("p"):
                txt = p.get_text().strip()
                if len(txt) < 55:
                    continue
                txt_lower = txt.lower()
                if any(junk in txt_lower for junk in junk_terms):
                    continue
                if txt.startswith("—") or txt.startswith("Foto:"):
                    continue
                paragraphs.append(txt)

            if len(paragraphs) >= 2:
                # Retorna os 4 a 6 parágrafos principais
                selected_p = paragraphs[:5]
                return {
                    "author": author,
                    "image_url": image_url,
                    "paragraphs": selected_p,
                    "full_text": "\n\n".join(selected_p),
                    "lead": selected_p[0]
                }
        except Exception:
            pass
        return None

    @staticmethod
    def fetch_rss(url: str, limit: int = 5) -> List[Dict[str, str]]:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
        items = []
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            if resp.status_code == 200:
                root = ET.fromstring(resp.content)
                channel = root.find("channel")
                if channel is not None:
                    for item in channel.findall("item")[:limit]:
                        title = item.findtext("title", "").strip()
                        desc = item.findtext("description", "").strip()
                        link = item.findtext("link", "").strip()
                        pub_date = item.findtext("pubDate", "").strip()
                        
                        image_url = None
                        credit = None
                        media_content = item.find("{http://search.yahoo.com/mrss/}content")
                        media_thumb = item.find("{http://search.yahoo.com/mrss/}thumbnail")
                        enclosure = item.find("enclosure")
                        if media_content is not None and media_content.get("url"):
                            image_url = media_content.get("url")
                        elif media_thumb is not None and media_thumb.get("url"):
                            image_url = media_thumb.get("url")
                        elif enclosure is not None and enclosure.get("url") and "image" in enclosure.get("type", ""):
                            image_url = enclosure.get("url")

                        if image_url and "bbci.co.uk" in image_url and "/240/" in image_url:
                            image_url = image_url.replace("/240/", "/800/")

                        credit_elem = item.find("{http://search.yahoo.com/mrss/}credit")
                        if credit_elem is not None and credit_elem.text:
                            credit = credit_elem.text.strip()

                        author = item.findtext("{http://purl.org/dc/elements/1.1/}creator") or item.findtext("author")
                        clean_source = channel.findtext("title", "Imprensa").replace(" > ", " • ").replace("g1", "G1").strip()
                        if not author or author.lower() in ["redação", "redacao"]:
                            author = f"Correspondência {clean_source}"

                        desc_clean = re.sub('<[^<]+?>', '', desc)
                        if title:
                            items.append({
                                "title": title,
                                "summary": desc_clean[:280] + "..." if len(desc_clean) > 280 else desc_clean,
                                "source": clean_source,
                                "author": author,
                                "link": link,
                                "date": pub_date,
                                "image_url": image_url,
                                "image_credit": credit or clean_source
                            })
        except Exception:
            pass
        return items

    @classmethod
    def get_weekly_news(cls) -> Dict[str, List[Dict[str, Any]]]:
        news = {"politica": [], "mundo": [], "tecnologia": []}
        for feed in RSS_FEEDS["politica"]:
            news["politica"].extend(cls.fetch_rss(feed, limit=3))
            if len(news["politica"]) >= 4:
                break

        for feed in RSS_FEEDS["mundo"]:
            news["mundo"].extend(cls.fetch_rss(feed, limit=3))
            if len(news["mundo"]) >= 4:
                break

        for feed in RSS_FEEDS["tecnologia"]:
            news["tecnologia"].extend(cls.fetch_rss(feed, limit=3))
            if len(news["tecnologia"]) >= 3:
                break

        # Para as matérias líderes, extrai o texto integral fidedigno da fonte oficial
        for cat in ["politica", "mundo", "tecnologia"]:
            if news[cat]:
                lead_item = news[cat][0]
                full_art = cls.fetch_full_article(lead_item["link"])
                if full_art:
                    lead_item["paragraphs"] = full_art["paragraphs"]
                    lead_item["full_text"] = full_art["full_text"]
                    if full_art.get("author"):
                        lead_item["author"] = full_art["author"]

        return news

    @classmethod
    def fetch_ibge_news(cls, limit: int = 4) -> List[Dict[str, Any]]:
        """Consome a API oficial de notícias e divulgações de estatísticas do IBGE."""
        headers = {"User-Agent": "ThePersonalDispatch/2.0 (mhgdidi@gmail.com; official-stats)"}
        items = []
        try:
            resp = requests.get(f"https://servicodados.ibge.gov.br/api/v3/noticias/?qtd={limit}", headers=headers, timeout=6)
            if resp.status_code == 200:
                data = resp.json().get("items", [])
                for item in data:
                    title = item.get("titulo", "").strip()
                    intro = item.get("introducao", "").strip()
                    link = item.get("link", "").strip()
                    date_pub = item.get("data_publicacao", "")
                    
                    # Imagens do IBGE vêm em campo json dentro de 'imagens'
                    img_url = None
                    try:
                        import json as j_mod
                        img_data = j_mod.loads(item.get("imagens", "{}"))
                        img_path = img_data.get("image_intro") or img_data.get("image_fulltext")
                        if img_path:
                            img_url = f"https://agenciadenoticias.ibge.gov.br/{img_path}"
                    except Exception:
                        pass

                    if title:
                        items.append({
                            "title": title,
                            "summary": intro[:250] + "..." if len(intro) > 250 else intro,
                            "source": "IBGE • Notícias Oficiais de Estatística",
                            "dateline": "RIO DE JANEIRO • IBGE",
                            "author": "Coordenação de Comunicação Social do IBGE",
                            "link": link,
                            "date": date_pub,
                            "image_url": img_url,
                            "image_credit": "Foto: Acervo Oficial IBGE / Agência de Notícias",
                            "impact_badge": "Indicadores Oficiais"
                        })
        except Exception:
            pass
        return items

    @classmethod
    def get_official_facts_briefing(cls) -> Dict[str, List[Dict[str, Any]]]:
        """
        Gera micro-cápsulas no formato clássico 'The World in Brief' e 'Brasil: Fatos Oficiais'.
        Consome estritamente fontes primárias oficiais e governamentais:
        - Brasil: Agência Brasil (EBC), IBGE Notícias e Agência Câmara.
        - Mundo: ONU News (Português), The New York Times / Reuters e BBC News Internacional.
        """
        # 1. Fatos Oficiais do Brasil
        br_facts = []
        # Ingestão de estatísticas e censos do IBGE
        ibge_items = cls.fetch_ibge_news(limit=2)
        br_facts.extend(ibge_items)

        # Ingestão de atos e serviços da Agência Brasil (EBC)
        ebc_items = cls.fetch_rss("https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml", limit=4)
        for item in ebc_items:
            item["dateline"] = "BRASÍLIA • Agência Brasil"
            item["impact_badge"] = "Ato de Estado"
            if not item.get("image_credit"):
                item["image_credit"] = "Foto: Agência Brasil / EBC"
            br_facts.append(item)
            if len(br_facts) >= 4:
                break

        # 2. Fatos Oficiais do Mundo
        world_facts = []
        # Ingestão de despachos da ONU (Nações Unidas em Português)
        onu_items = cls.fetch_rss("https://news.un.org/feed/subscribe/pt/news/all/rss.xml", limit=3)
        for item in onu_items:
            item["dateline"] = "GENEBRA / NY • ONU News"
            item["impact_badge"] = "Diplomacia & Paz"
            if not item.get("image_credit"):
                item["image_credit"] = "Foto: Acervo Multimídia ONU"
            world_facts.append(item)

        # Ingestão internacional (BBC Mundo / NYT)
        nyt_items = cls.fetch_rss("https://rss.nytimes.com/services/xml/rss/nyt/World.xml", limit=3)
        for item in nyt_items:
            item["dateline"] = "NOVA YORK • NYT Global"
            item["impact_badge"] = "Relações Globais"
            world_facts.append(item)
            if len(world_facts) >= 4:
                break

        return {
            "brasil_facts": br_facts[:4],
            "world_facts": world_facts[:4]
        }
