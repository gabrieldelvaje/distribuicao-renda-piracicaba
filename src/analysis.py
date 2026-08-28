"""
analysis.py
Calcula crescimento nominal, valores históricos em R$ de 2022
e a distância entre média e mediana.

Importante:
- O projeto original usou valores nominais nos gráficos históricos.
- Para uma comparação econômica mais consistente, este script também
  calcula uma versão corrigida pelo IPCA usando índices médios anuais.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "processed" / "renda_bairros_base.csv"
OUTPUT = ROOT / "data" / "processed"

# Índices médios anuais usados no projeto.
# Para atualizar, substitua pelos valores oficiais da série do IBGE/SIDRA.
IPCA_AVG = {
    2000: 1636.098333,
    2010: 3114.504167,
    2022: 6368.604167,
}

def main():
    df = pd.read_csv(INPUT)

    factor_2000 = IPCA_AVG[2022] / IPCA_AVG[2000]
    factor_2010 = IPCA_AVG[2022] / IPCA_AVG[2010]

    df["renda_2000_em_R$2022"] = df["2000"] * factor_2000
    df["renda_2010_em_R$2022"] = df["2010"] * factor_2010

    df["crescimento_nominal_2000_2022_%"] = (
        df[2022] / df[2000] - 1
    ) * 100

    df["crescimento_real_2000_2022_%"] = (
        df[2022] / df["renda_2000_em_R$2022"] - 1
    ) * 100

    df["crescimento_real_2010_2022_%"] = (
        df[2022] / df["renda_2010_em_R$2022"] - 1
    ) * 100

    c22 = pd.read_csv(OUTPUT / "renda_2022.csv")
    c22["renda_media_2022"] = pd.to_numeric(c22["renda_media_2022"], errors="coerce")
    c22["renda_mediana_2022"] = pd.to_numeric(c22["renda_mediana_2022"], errors="coerce")

    df = df.merge(
        c22[["bairro", "renda_media_2022", "renda_mediana_2022"]],
        on="bairro",
        how="left",
    )

    df["gap_media_mediana_2022"] = (
        df["renda_media_2022"] - df["renda_mediana_2022"]
    )
    df["media_mediana_ratio_2022"] = (
        df["renda_media_2022"] / df["renda_mediana_2022"]
    )

    df.to_csv(OUTPUT / "renda_bairros.csv", index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    main()
