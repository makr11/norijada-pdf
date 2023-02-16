from pathlib import Path
import sys
src_path = Path("scripts").parent / "src/norijada"
sys.path.append(str(src_path.absolute()))

from norijada_pdf.main import arrange, plot


if __name__ == "__main__":
    fonts = Path("src/norijada/fonts")
    for font in fonts.iterdir():
        arrange(f"{font.stem}.ttf", "input.txt", rotation=True, unique_identifier=f"{font.stem}-rotated")
        plot(f"{font.stem}.ttf", "input.txt", rotation=False, unique_identifier=f"{font.stem}-horizontal")
