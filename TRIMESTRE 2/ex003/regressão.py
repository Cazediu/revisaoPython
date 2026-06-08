# regressao_acuracia.py
# Requisitos: pandas numpy scikit-learn
# pip install pandas numpy scikit-learn

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# 1. Carregar dados
df = pd.read_csv("diabetes.csv")

# 2. Alvo (target) - prever Glucose
TARGET = "Glucose"

# 3. Tratar zeros como missing em colunas clínicas comuns
zero_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for c in zero_cols:
    if c in df.columns:
        df[c] = df[c].replace(0, np.nan)

# Imputar com mediana simples
df = df.fillna(df.median())

# 4. Features e target
X = df.drop(columns=[TARGET])
y = df[TARGET]

# 5. Padronizar features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 6. Separar treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2
)

# 7. Treinar modelos
lr = LinearRegression().fit(X_train, y_train)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
lr_poly = LinearRegression().fit(X_train_poly, y_train)

rf = RandomForestRegressor(n_estimators=100, random_state=42).fit(X_train, y_train)

# 8. Calcular R² (acurácia para regressão)
r2_lr = r2_score(y_test, lr.predict(X_test))
r2_poly = r2_score(y_test, lr_poly.predict(X_test_poly))
r2_rf = r2_score(y_test, rf.predict(X_test))

# 9. Imprimir resultados
print(f"Regressão Linear R²: {r2_lr:.4f}")
print(f"Regressão Polinomial R²: {r2_poly:.4f}")
print(f"Random Forest R²: {r2_rf:.4f}")
