import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import root_mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando e pré-processando o dataset fornecido pelo professor
df = pd.read_csv(r"C:\Users\Naylan\Downloads\train.csv")

# Extraindo informações temporais da coluna datetime
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.day
df['month'] = df['datetime'].dt.month
df['year'] = df['datetime'].dt.year

# Removendo a coluna datetime original
df = df.drop('datetime', axis=1)

# Separando o target
# Removendo 'casual' e 'registered' pois 'count' é a soma delas
X = df.drop(['count', 'casual', 'registered'], axis=1)
y = df['count']

# Dividindo em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizando os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinando o modelo de regressão linear
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)
lr_pred = lr_model.predict(X_test_scaled)

# Treinando o modelo de árvore de decisão
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train_scaled, y_train)
dt_pred = dt_model.predict(X_test_scaled)

# Verificando o desempenho dos modelos
def print_metrics(y_true, y_pred, model_name):
    rmse = np.sqrt(root_mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    print(f"{model_name}:")
    print(f"RMSE: {rmse:.2f}")
    print(f"MAE: {mae:.2f}\n")

print_metrics(y_test, lr_pred, "Regressão linear")
print_metrics(y_test, dt_pred, "Árvore de decisão")

# 4. Visualizações
plt.figure(figsize=(12, 5))

# Gerando gráfico de regressão linear
plt.subplot(1, 2, 1)
plt.scatter(y_test, lr_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Valores reais')
plt.ylabel('Predições')
plt.title('Regressão linear')

# Gerando gráfico de á]rvore de decisão
plt.subplot(1, 2, 2)
plt.scatter(y_test, dt_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Valores reais')
plt.ylabel('Predições')
plt.title('Árvore de decisão')

plt.tight_layout()
plt.show()