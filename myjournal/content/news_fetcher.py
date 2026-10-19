import xml.etree.ElementTree as ET
import re
import requests
from typing import List, Dict, Any, Optional
from bs4 import BeautifulSoup

RSS_FEEDS = {
    "politica": [
        "https://feeds.bbci.co.uk/portuguese/rss.xml",
        "https://g1.globo.com/rss/g1/politica/"
    ],
    "mundo": [
        "https://feeds.bbci.co.uk/portuguese/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    ],
    "tecnologia": [
        "https://g1.globo.com/rss/g1/tecnologia/",
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
