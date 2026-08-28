# Metodologia detalhada

## 1. Unidade espacial

A unidade principal da análise é o **bairro de Piracicaba**.

## 2. 2000

O Censo 2000 fornece classes de rendimento. A renda média foi estimada por pontos representativos das classes.

Fórmula:

`media = Σ(contagem_classe × ponto_médio_classe) / total`

## 3. 2010

Os dados foram agregados dos setores censitários para o bairro:

`media_bairro = Σ(rendimento_setor) / Σ(responsáveis_setor)`

Essa agregação evita dar o mesmo peso a setores com tamanhos diferentes.

## 4. 2022

Foram utilizados diretamente os indicadores de média e mediana do rendimento nominal mensal do responsável pelo domicílio.

## 5. Crescimento nominal

`crescimento = (renda_final / renda_inicial - 1) × 100`

## 6. Correção monetária

Para comparar poder de compra, foi criada uma segunda série em reais de 2022:

`renda_2022 = renda_historica × (IPCA_médio_2022 / IPCA_médio_ano)`

Fatores usados no pipeline:

- 2000 → 2022: **3.892556**
- 2010 → 2022: **2.044821**

Esses fatores são uma escolha metodológica baseada em médias anuais do índice. Eles não devem ser confundidos com o fator `3,393` presente na planilha original.

## 7. Média versus mediana

`gap = média - mediana`

`ratio = média / mediana`

Quanto maior a distância, maior a assimetria positiva da distribuição.

## 8. Interpretação dos condomínios

A análise espacial busca identificar coincidências entre:

- expansão de empreendimentos;
- localização periférica;
- aumento da renda média;
- diferença entre média e mediana.

O resultado é **descritivo/associativo**, não uma estimativa causal.
