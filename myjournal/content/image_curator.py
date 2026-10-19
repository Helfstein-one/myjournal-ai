import base64
import hashlib
import os
import re
import urllib.parse
from pathlib import Path
from typing import Dict, Any, List, Optional
import requests
from myjournal.config import Config

# SVG vintage engravings para fallback offline garantido
VINTAGE_FALLBACKS = {
    "front_page": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f8f6f0"/><rect x="20" y="20" width="760" height="410" fill="none" stroke="#222" stroke-width="2"/><line x1="20" y1="40" x2="780" y2="40" stroke="#222" stroke-width="0.8"/><text x="400" y="210" font-family="Georgia, serif" font-size="28" font-style="italic" text-anchor="middle" fill="#222">The Personal Dispatch</text><text x="400" y="245" font-family="'Courier New', monospace" font-size="13" text-anchor="middle" fill="#666" letter-spacing="3">EDIÇÃO DOMINICAL • GRAVURA EDITORIAL</text><path d="M 250 280 L 550 280 M 320 290 L 480 290" stroke="#444" stroke-width="1"/></svg>""",
    "politics_national": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f6f4ee"/><rect x="20" y="20" width="760" height="410" fill="none" stroke="#222" stroke-width="2"/><line x1="180" y1="330" x2="620" y2="330" stroke="#222" stroke-width="3"/><path d="M 220 330 L 220 210 L 360 210 L 360 330 M 440 330 L 440 210 L 580 210 L 580 330" stroke="#333" stroke-width="2" fill="none"/><path d="M 260 210 Q 300 150 340 210 M 460 210 Q 500 270 540 210" stroke="#333" stroke-width="2" fill="none"/><text x="400" y="380" font-family="Georgia, serif" font-size="14" font-style="italic" text-anchor="middle" fill="#333">Instituições Republicanas & Poder Nacional</text></svg>""",
    "international": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f4f1ea"/><rect x="15" y="15" width="770" height="420" fill="none" stroke="#333" stroke-width="1.5"/><circle cx="400" cy="225" r="140" fill="none" stroke="#444" stroke-width="1" stroke-dasharray="4 2"/><ellipse cx="400" cy="225" rx="140" ry="60" fill="none" stroke="#555" stroke-width="1"/><line x1="400" y1="85" x2="400" y2="365" stroke="#555" stroke-width="1"/><text x="400" y="395" font-family="Georgia, serif" font-size="14" font-style="italic" text-anchor="middle" fill="#333">Panorama Geopolítico Global</text></svg>""",
    "tech_ai": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f5f3ec"/><rect x="20" y="20" width="760" height="410" fill="none" stroke="#222" stroke-width="1.5"/><rect x="280" y="150" width="240" height="150" fill="none" stroke="#333" stroke-width="2"/><line x1="240" y1="225" x2="280" y2="225" stroke="#444" stroke-width="2"/><line x1="520" y1="225" x2="560" y2="225" stroke="#444" stroke-width="2"/><circle cx="400" cy="225" r="30" fill="none" stroke="#222" stroke-width="2"/><text x="400" y="380" font-family="Georgia, serif" font-size="14" font-style="italic" text-anchor="middle" fill="#333">Tecnologia, Inovação & Inteligência Artificial</text></svg>""",
    "sp_politics": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f7f5ed"/><rect x="20" y="20" width="760" height="410" fill="none" stroke="#111" stroke-width="2"/><rect x="250" y="160" width="300" height="160" fill="none" stroke="#333" stroke-width="2"/><line x1="250" y1="200" x2="550" y2="200" stroke="#333" stroke-width="1"/><line x1="200" y1="320" x2="600" y2="320" stroke="#222" stroke-width="4"/><text x="400" y="385" font-family="Georgia, serif" font-size="14" font-style="italic" text-anchor="middle" fill="#333">Política Paulista: Palácio dos Bandeirantes & Alesp</text></svg>""",
    "national_economy": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f8f7f2"/><rect x="20" y="20" width="760" height="410" fill="none" stroke="#222" stroke-width="1.5"/><polyline points="200,320 320,260 420,290 520,200 600,160" fill="none" stroke="#222" stroke-width="3"/><line x1="180" y1="340" x2="620" y2="340" stroke="#444" stroke-width="2"/><line x1="180" y1="140" x2="180" y2="340" stroke="#444" stroke-width="2"/><text x="400" y="385" font-family="Georgia, serif" font-size="14" font-style="italic" text-anchor="middle" fill="#333">Macroeconomia, Moeda & Mercados Financeiros</text></svg>""",
    "world_geopolitics": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f4f1ea"/><rect x="15" y="15" width="770" height="420" fill="none" stroke="#333" stroke-width="1.5"/><circle cx="400" cy="225" r="130" fill="none" stroke="#333" stroke-width="1.5"/><ellipse cx="400" cy="225" rx="130" ry="55" fill="none" stroke="#555" stroke-width="1"/><line x1="400" y1="95" x2="400" y2="355" stroke="#555" stroke-width="1"/><text x="400" y="395" font-family="Georgia, serif" font-size="14" font-style="italic" text-anchor="middle" fill="#333">Diplomacia Global & Relações Internacionais</text></svg>""",
    "lifestyle_sp": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f5f3ec"/><rect x="20" y="20" width="760" height="410" fill="none" stroke="#222" stroke-width="1.5"/><path d="M 240 330 L 240 180 L 320 180 L 320 330 M 340 330 L 340 130 L 460 130 L 460 330 M 480 330 L 480 200 L 560 200 L 560 330" fill="none" stroke="#333" stroke-width="2"/><text x="400" y="380" font-family="Georgia, serif" font-size="14" font-style="italic" text-anchor="middle" fill="#333">Metrópole: Paisagem Arquitetônica Paulistana</text></svg>""",
    "crafts_careers": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%"><rect width="800" height="450" fill="#f6f4ee"/><rect x="20" y="20" width="760" height="410" fill="none" stroke="#222" stroke-width="1.5"/><line x1="150" y1="320" x2="650" y2="320" stroke="#333" stroke-width="4"/><rect x="200" y="240" width="100" height="80" fill="none" stroke="#222" stroke-width="2"/><circle cx="500" cy="220" r="35" fill="none" stroke="#444" stroke-width="2"/><line x1="500" y1="255" x2="540" y2="310" stroke="#444" stroke-width="3"/><text x="400" y="380" font-family="Georgia, serif" font-size="14" font-style="italic" text-anchor="middle" fill="#333">Ateliê de Restauro & Bancada de Ourivesaria</text></svg>"""
}

class ImageCurator:
    def __init__(self):
        self.image_dir = Config.OUTPUT_DIR / "images"
        self.image_dir.mkdir(parents=True, exist_ok=True)
        self.headers = {"User-Agent": "ThePersonalDispatch/2.0 (mhgdidi@gmail.com; news-aggregator)"}

    def _to_data_uri(self, content_bytes: bytes, mime_type: str = "image/jpeg") -> str:
        b64 = base64.b64encode(content_bytes).decode("utf-8")
        return f"data:{mime_type};base64,{b64}"

    def _svg_to_data_uri(self, svg_str: str) -> str:
        b64 = base64.b64encode(svg_str.encode("utf-8")).decode("utf-8")
        return f"data:image/svg+xml;base64,{b64}"

    def _download_and_convert(self, url: str, target_name: str) -> Optional[str]:
        try:
            resp = requests.get(url, headers=self.headers, timeout=6)
            if resp.status_code == 200 and len(resp.content) > 5000:
                # Salva localmente
                ext = ".jpg"
                mime = "image/jpeg"
                if "png" in resp.headers.get("Content-Type", "") or url.lower().endswith(".png"):
                    ext = ".png"
                    mime = "image/png"
                elif "webp" in resp.headers.get("Content-Type", "") or url.lower().endswith(".webp"):
                    ext = ".webp"
                    mime = "image/webp"

                local_path = self.image_dir / f"{target_name}{ext}"
                local_path.write_bytes(resp.content)
                return self._to_data_uri(resp.content, mime)
        except Exception as e:
            pass
        return None

    def search_wikimedia(self, query: str) -> Optional[Dict[str, str]]:
        try:
            params = {
                "action": "query",
                "generator": "search",
                "gsrsearch": query,
                "gsrnamespace": 6,
                "gsrlimit": 4,
                "prop": "imageinfo",
                "iiprop": "url|mime",
                "format": "json"
            }
            resp = requests.get("https://commons.wikimedia.org/w/api.php", params=params, headers=self.headers, timeout=6)
            if resp.status_code == 200:
                pages = resp.json().get("query", {}).get("pages", {})
                for k, v in pages.items():
                    info = v.get("imageinfo", [{}])[0]
                    url = info.get("url")
                    if url:
                        clean_url = url.split("?")[0].lower()
                        if clean_url.endswith((".jpg", ".jpeg", ".png", ".webp")):
                            clean_title = v.get("title", "").replace("File:", "").split(".")[0]
                            return {
                                "url": url,
                                "title": clean_title,
                                "credit": "Acervo Wikimedia Commons / Domínio Público"
                            }
        except Exception:
            pass
        return None

    def _curate_from_article_or_search(
        self,
        target_name: str,
        headline: str,
        image_url: Optional[str] = None,
        image_credit: Optional[str] = None,
        fallback_queries: Optional[List[str]] = None,
        fallback_svg_key: str = "front_page",
        default_caption: str = "",
        default_credit: str = "Arquivo Editorial / The Personal Dispatch"
    ) -> Dict[str, str]:
        # 1. Foto real do artigo original
        if image_url and image_url.startswith("http"):
            data_uri = self._download_and_convert(image_url, target_name)
            if data_uri:
                clean_title = headline.strip() if headline else default_caption
                return {
                    "url": data_uri,
                    "caption": f"Registro oficial: {clean_title[:95]}...",
                    "credit": image_credit or "Foto: Agência de Notícias Oficial"
                }

        # 2. Busca na Wikimedia baseada nas palavras-chave reais da matéria
        queries = []
        if headline:
            clean_q = re.sub(r'[^\w\s]', '', headline).strip()
            words = [w for w in clean_q.split() if len(w) > 3 and w.lower() not in ["para", "com", "como", "sobre", "mais", "entre", "onde", "quem", "nesta", "neste", "pode", "estao", "desta", "pelo", "pela"]]
            if words:
                queries.append(" ".join(words[:4]))
        if fallback_queries:
            queries.extend(fallback_queries)

        for q in queries:
            res = self.search_wikimedia(q)
            if res:
                data_uri = self._download_and_convert(res["url"], target_name)
                if data_uri:
                    return {
                        "url": data_uri,
                        "caption": f"Documento contextual: {res['title'][:85]}.",
                        "credit": res["credit"]
                    }

        # 3. SVG editorial garantido
        svg_key = fallback_svg_key if fallback_svg_key in VINTAGE_FALLBACKS else "front_page"
        return {
            "url": self._svg_to_data_uri(VINTAGE_FALLBACKS[svg_key]),
            "caption": default_caption or (headline[:80] if headline else "Gravura editorial."),
            "credit": default_credit
        }

    def curate_images(self, journal_data: Dict[str, Any], news_items: List[Dict[str, Any]]) -> Dict[str, Dict[str, str]]:
        """
        Curadoria dinâmica das imagens dos cadernos do jornal garantindo fidelidade 100% à pauta:
        - Capa (Hero Image)
        - Política Nacional (Pág. 4)
        - Radar Internacional (Pág. 5)
        - Tecnologia & IA (Pág. 6)
        - Política de São Paulo (Pág. 8)
        - Atualidades & Economia Nacional (Pág. 9)
        - Mundo em Foco & Geopolítica (Pág. 10)
        - Metrópole SP (Pág. 11)
        - Ofícios & Concursos (Pág. 12)
        """
        curated = {}

        # 1. CAPA (Hero Image)
        front_headline = journal_data.get("front_page", {}).get("lead_headline", "")
        front_img_url = None
        front_credit = None
        for item in news_items:
            if item.get("image_url"):
                front_img_url = item["image_url"]
                front_credit = item.get("image_credit")
                break

        curated["front_page"] = self._curate_from_article_or_search(
            target_name="front_page_hero",
            headline=front_headline,
            image_url=front_img_url,
            image_credit=front_credit,
            fallback_queries=["Vintage broadsheet newspaper printing press engraving", "The New York Times building historic"],
            fallback_svg_key="front_page",
            default_caption="Frontispício editorial da presente edição dominical."
        )

        # 2. POLÍTICA NACIONAL (Pág. 4)
        pol_data = journal_data.get("politics_world", {})
        pol_headline = pol_data.get("headline", "")
        pol_img_url = pol_data.get("lead_item", {}).get("image_url")
        pol_credit = pol_data.get("lead_item", {}).get("image_credit")
        if not pol_img_url:
            for item in news_items:
                if any(k in item.get("source", "").lower() for k in ["política", "brasil", "g1"]):
                    if item.get("image_url"):
                        pol_img_url = item["image_url"]
                        pol_credit = item.get("image_credit")
                        break

        curated["politics_national"] = self._curate_from_article_or_search(
            target_name="politics_national",
            headline=pol_headline,
            image_url=pol_img_url,
            image_credit=pol_credit,
            fallback_queries=["Congresso Nacional Brasilia", "Palacio do Planalto Brasilia", "Supremo Tribunal Federal"],
            fallback_svg_key="politics_national",
            default_caption="Edifício do Congresso Nacional e centro dos debates republicanos em Brasília."
        )

        # 3. RADAR INTERNACIONAL (Pág. 5)
        intl_item = news_items[1] if len(news_items) > 1 else (news_items[0] if news_items else {})
        curated["international_radar"] = self._curate_from_article_or_search(
            target_name="international_radar",
            headline=intl_item.get("title", "Radar Internacional"),
            image_url=intl_item.get("image_url"),
            image_credit=intl_item.get("image_credit"),
            fallback_queries=["United Nations assembly hall vintage", "World diplomacy conference historic"],
            fallback_svg_key="international",
            default_caption="Sessão de debates internacionais e acordos multilaterais."
        )
        curated["international"] = curated["international_radar"]

        # 4. TECNOLOGIA & IA (Pág. 6)
        tech_data = journal_data.get("tech_ai", {})
        tech_headline = tech_data.get("headline", "")
        tech_img_url = tech_data.get("lead_item", {}).get("image_url")
        tech_credit = tech_data.get("lead_item", {}).get("image_credit")
        if not tech_img_url:
            for item in news_items:
                if "tecnologia" in item.get("source", "").lower() or "tech" in item.get("source", "").lower():
                    if item.get("image_url"):
                        tech_img_url = item["image_url"]
                        tech_credit = item.get("image_credit")
                        break

        curated["tech_ai"] = self._curate_from_article_or_search(
            target_name="tech_ai",
            headline=tech_headline,
            image_url=tech_img_url,
            image_credit=tech_credit,
            fallback_queries=["Artificial Intelligence server computer vintage", "Microelectronics technology hardware"],
            fallback_svg_key="tech_ai",
            default_caption="Processamento de dados e circuitos de computação e inteligência artificial."
        )

        # 5. POLÍTICA DE SÃO PAULO (Pág. 8)
        sp_data = journal_data.get("sp_politics", {})
        sp_headline = sp_data.get("headline", "")
        sp_lead = sp_data.get("lead_item", {})
        sp_img_url = sp_data.get("image_url") or sp_lead.get("image_url")
        sp_credit = sp_data.get("image_credit") or sp_lead.get("image_credit")

        curated["sp_politics"] = self._curate_from_article_or_search(
            target_name="sp_politics_curation",
            headline=sp_headline,
            image_url=sp_img_url,
            image_credit=sp_credit,
            fallback_queries=["Palacio dos Bandeirantes Sao Paulo", "Assembleia Legislativa do Estado de Sao Paulo", "Edificio Matarazzo Prefeitura"],
            fallback_svg_key="sp_politics",
            default_caption="Sede do Governo do Estado de São Paulo e plenário da Alesp."
        )
        curated["history"] = curated["sp_politics"]

        # 6. ATUALIDADES & ECONOMIA NACIONAL (Pág. 9)
        eco_data = journal_data.get("national_economy", {})
        eco_headline = eco_data.get("headline", "")
        eco_lead = eco_data.get("lead_item", {})
        eco_img_url = eco_data.get("image_url") or eco_lead.get("image_url")
        eco_credit = eco_data.get("image_credit") or eco_lead.get("image_credit")

        curated["national_economy"] = self._curate_from_article_or_search(
            target_name="national_economy_curation",
            headline=eco_headline,
            image_url=eco_img_url,
            image_credit=eco_credit,
            fallback_queries=["Banco Central do Brasil Brasilia", "Bolsa de Valores B3 Sao Paulo", "Ministerio da Fazenda Brasilia"],
            fallback_svg_key="national_economy",
            default_caption="Painel econômico, indicadores fiscais e política monetária do Banco Central."
        )
        curated["fashion"] = curated["national_economy"]

        # 7. MUNDO EM FOCO & GEOPOLÍTICA (Pág. 10)
        world_data = journal_data.get("world_geopolitics", {})
        world_headline = world_data.get("headline", "")
        world_lead = world_data.get("lead_item", {})
        world_img_url = world_data.get("image_url") or world_lead.get("image_url")
        world_credit = world_data.get("image_credit") or world_lead.get("image_credit")

        curated["world_geopolitics"] = self._curate_from_article_or_search(
            target_name="world_geopolitics_curation",
            headline=world_headline,
            image_url=world_img_url,
            image_credit=world_credit,
            fallback_queries=["United Nations General Assembly", "Diplomatic conference international relations"],
            fallback_svg_key="world_geopolitics",
            default_caption="Encontro diplomático internacional e alianças de segurança global."
        )
        curated["jewelry"] = curated["world_geopolitics"]

        # 8. METRÓPOLE SP (Pág. 11)
        curated["lifestyle_sp"] = self._curate_from_article_or_search(
            target_name="lifestyle_sp_curation",
            headline="Patrimônio e Vida Cultural de São Paulo",
            image_url=None,
            image_credit=None,
            fallback_queries=["Pinacoteca de Sao Paulo", "Theatro Municipal de Sao Paulo", "Edificio Copan Sao Paulo", "Parque Ibirapuera"],
            fallback_svg_key="lifestyle_sp",
            default_caption="Perspectiva da arquitetura e vida cultural da capital paulista."
        )

        # 9. OFÍCIOS, RESTAURO & OPORTUNIDADES (Pág. 12)
        curated["crafts_careers"] = self._curate_from_article_or_search(
            target_name="crafts_careers_curation",
            headline="Bancada de Ourivesaria e Restauro de Acervos",
            image_url=None,
            image_credit=None,
            fallback_queries=["Goldsmith workshop engraving", "Art conservation restoration workshop historic", "Jewelry workbench tools vintage"],
            fallback_svg_key="crafts_careers",
            default_caption="Bancada de ourivesaria e ateliê técnico de conservação de acervos."
        )

        return curated
