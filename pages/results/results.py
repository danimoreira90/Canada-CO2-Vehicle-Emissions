import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def results():
        # Carregando a base de dados
    try:
        df1 = pd.read_csv(
            'https://raw.githubusercontent.com/danimoreira90/Canada-CO2-Vehicle-Emissions/main/data/CO2%20Emissions_Canada.csv')
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")


    # Create a new column 'Frequency' based on the 'Fuel Consumption Comb (L/100 km)' values
    df1['Frequency'] = df1.groupby('Fuel Consumption Comb (L/100 km)')['Fuel Consumption Comb (L/100 km)'].transform('count')

    # Create a new dataframe with the added 'Frequency' column
    df = df1.copy()

    st.title('3. Resultados:')
    st.subheader('Valores reais X Previsões')
    # Identificar colunas numéricas
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # Normalizar colunas numéricas
    df[numeric_columns] = MinMaxScaler().fit_transform(df[numeric_columns])

    # Dividir os dados em conjuntos de treinamento e teste
    X = df[numeric_columns].drop('CO2 Emissions(g/km)', axis=1)  # Remover a coluna alvo das features
    y = df['CO2 Emissions(g/km)']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criar e treinar o modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Fazer previsões no conjunto de teste
    y_pred = model.predict(X_test)

    # Avaliar o desempenho do modelo
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)

    # Criar gráfico de dispersão
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.set_xlabel('Valores Reais')
    ax.set_ylabel('Previsões')
    ax.set_title('Valores Reais vs. Previsões')
    st.pyplot(fig)

    # Exibir métricas no Streamlit
    st.write(f'Mean Squared Error (MSE): {mse}')
    st.write(f'Root Mean Squared Error (RMSE): {rmse}')
    st.write(f'Mean Absolute Error (MAE): {mae}')
