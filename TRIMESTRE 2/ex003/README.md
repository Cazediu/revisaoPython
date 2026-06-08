# Regressão com diabetes.csv

## Objetivo
Prever a variável contínua **Glucose (Glicose)** usando variáveis clínicas do dataset `diabetes.csv`. Implementando três modelos: Regressão Linear, Regressão Polinomial e Random Forest Regressor.

## Pré-processamento
- Zeros em colunas `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI` foram tratados como valores faltantes e imputados pela mediana.
- Todas as features numéricas foram padronizadas (StandardScaler).
- Divisão treino/teste: 80% treino / 20% teste.

## Modelos treinados
1. **Linear Regression**
2. **Polynomial Regression (degree=2)** — features polinomiais + regressão linear
3. **Random Forest Regressor** (200 árvores)

## Métricas de avaliação
- **RMSE** e **MAE** calculados no conjunto de teste.
- Acurácias encontradas:
   - Linear Regression R²: 0.3785
   - Polynomial Degree 2 R²: 0.2619
   - Random Forest R²: 0.3621

## Informações para interpretação
- R² (acurácia para regressão): indica fração da variância explicada. Valores próximos de 1 → bom ajuste; valores próximos de 0 ou negativos → modelo ruim.

- RMSE / MAE: medem erro absoluto em unidades do alvo (aqui, mg/dL de glicose). Use MAE para interpretação direta (erro médio) e RMSE para penalizar grandes erros.

- Comparação entre modelos: o melhor modelo é o que apresentar menor RMSE/MAE e R² mais alto no conjunto de teste, não no treino.

## Sinais de comportamento observado e suas causas prováveis

- Random Forest com melhor desempenho: esperado quando há relações não lineares e interações entre variáveis (ex.: BMI × Age). Se RF vence, significa que padrões complexos existem.

- Polinomial com overfitting: se o R² do treino for muito maior que o do teste, o polinômio provavelmente está ajustando ruído. Grau 2 costuma ser razoável; graus maiores aumentam risco.

- Linear com desempenho competitivo: se a regressão linear ficar próxima do RF, os relacionamentos entre features e Glucose são majoritariamente lineares ou o ruído domina os sinais.

- **Informação importante:** Impacto da imputação: imputar pela mediana tende a reduzir variabilidade; modelos complexos podem perder vantagem se a imputação “aplana” padrões.

