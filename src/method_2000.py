"""
method_2000.py
Demonstra o cálculo da renda média de 2000 a partir das classes
de rendimento do Censo.

A média é estimada por ponto médio de cada classe:
    renda_estimada = soma(contagem_da_classe * ponto_medio) / total

Para a classe "mais de 20 salários mínimos", o projeto adotou
R$ 3.775 como valor representativo, equivalente a 25 SM usando
R$ 151 como salário mínimo de referência.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "source" / "Compilado.xlsx"

def main():
    df = pd.read_excel(SOURCE, sheet_name="Censo_2000", header=0)

    # Linhas válidas de bairros
    df = df.iloc[4:].copy()
    df = df.rename(columns={df.columns[0]: "bairro"})

    # Pontos representativos utilizados na planilha original.
    midpoint = {
        "Até 1/2 salário": 37.5,
        "Mais de 1/2 a 1 salário": 113.25,
        "Mais de 1 a 2 salários": 226.5,
        "Mais de 2 a 3 salários": 377.5,
        "Mais de 3 a 5 salários": 604.0,
        "Mais de 5 a 10 salários": 1132.5,
        "Mais de 10 a 15 salários": 1887.5,
        "Mais de 15 a 20 salários": 2642.5,
        "Mais de 20 salários": 3775.0,
    }

    for col in midpoint:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["total_estimado"] = sum(df[col] * value for col, value in midpoint.items())
    df["renda_media_2000"] = df["total_estimado"] / pd.to_numeric(df["Total"], errors="coerce")

    df[["bairro", "renda_media_2000"]].to_csv(
        ROOT / "data" / "processed" / "renda_2000_recalculada.csv",
        index=False,
        encoding="utf-8-sig",
    )

if __name__ == "__main__":
    main()
