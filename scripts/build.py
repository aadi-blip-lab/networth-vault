from pathlib import Path
import shutil
import re

ROOT = Path(__file__).resolve().parent.parent

PAGES = ROOT / "pages"
COMPONENTS = ROOT / "components"
ASSETS = ROOT / "assets"
OUTPUT = ROOT / "docs"


def reset_output():
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True, exist_ok=True)


def copy_assets():
    if ASSETS.exists():
        shutil.copytree(ASSETS, OUTPUT / "assets")


def load_component(name: str) -> str:
    file = COMPONENTS / f"{name}.html"

    if not file.exists():
        print(f"Missing component: {name}")
        return ""

    return file.read_text(encoding="utf-8")


def inject_components(html: str) -> str:

    pattern = r"\{\{\s*(.*?)\s*\}\}"

    def replace(match):
        component = match.group(1)
        return load_component(component)

    return re.sub(pattern, replace, html)


def build_pages():

    for page in PAGES.glob("*.html"):

        html = page.read_text(encoding="utf-8")

        html = inject_components(html)

        destination = OUTPUT / page.name

        destination.write_text(html, encoding="utf-8")

        print(f"Built {page.name}")


def main():

    print("Building NetWorth Vault")

    reset_output()

    copy_assets()

    build_pages()

    print("Done")


if __name__ == "__main__":
    main()
