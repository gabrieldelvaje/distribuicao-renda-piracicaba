"""
prepare_data.py
Reorganiza os dados do arquivo Compilado.xlsx e gera uma base analítica.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "source" / "Compilado.xlsx"
OUTPUT = ROOT / "data" / "processed"

def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)

    comp = pd.read_excel(SOURCE, sheet_name="Compilado", header=0)
    comp = comp.rename(columns={"Unnamed: 0": "bairro"})
    comp = comp[["bairro", 2000, 2010, 2022, "delta 00 - 10", "delta 10 - 22"]]
    comp.to_csv(OUTPUT / "renda_bairros_base.csv", index=False, encoding="utf-8-sig")

    c22 = pd.read_excel(SOURCE, sheet_name="Censo_2022", header=1)
    c22 = c22[["CD_BAIRRO", "Cidade", "NM_BAIRRO", "V06001", "V06002", "V06004", "V06006"]]
    c22 = c22.rename(columns={
        "NM_BAIRRO": "bairro",
        "V06001": "responsaveis",
        "V06002": "moradores",
        "V06004": "renda_media_2022",
        "V06006": "renda_mediana_2022",
    })
    c22.to_csv(OUTPUT / "renda_2022.csv", index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    main()
