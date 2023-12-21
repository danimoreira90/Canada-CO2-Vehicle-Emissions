import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.preprocessing import StandardScaler

def data_quality():
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

    st.title('2. Qualidade de dados:')

    # Boxplot por Consumo de Combustível Combinado (mpg)
    
    st.subheader('Boxplot por Consumo de Combustível Combinado (mpg)')
    fig1, ax = plt.subplots()    
    sns.boxplot(x='Fuel Consumption Comb (mpg)', y='CO2 Emissions(g/km)', data=df, palette='viridis', hue='Fuel Consumption Comb (mpg)',legend=False )
    plt.figure(figsize=(12, 8))
    plt.title('Boxplot de Emissões de CO2 por Consumo de Combustível Combinado (mpg)')
    plt.xlabel('Fuel Consumption Comb (mpg)')
    plt.ylabel('CO2 Emissions (g/km)')
    st.pyplot(fig1)
 

    # Gráfico de Dispersão entre Consumo de Combustível na Cidade e Emissões de CO2
    
    st.subheader('Gráfico de Dispersão entre Consumo de Combustível na Cidade e Emissões de CO2')
    fig2, ax = plt.subplots()
    sns.scatterplot(x='Fuel Consumption City (L/100 km)', y='CO2 Emissions(g/km)', data=df, color='green')
    plt.figure(figsize=(10, 6))  
    plt.title('Gráfico de Dispersão entre Consumo de Combustível na Cidade e Emissões de CO2')
    plt.xlabel('Fuel Consumption City (L/100 km)')
    plt.ylabel('CO2 Emissions (g/km)')
    st.pyplot(fig2)

    st.write('Problema 1: Outliers')
    st.write('Problema: Presença de valores extremos em uma ou mais variáveis.')
    st.write('Dimensões de Qualidade Afetadas: Precisão, Consistência.')
    st.write('Solução: Identificar e tratar outliers, por exemplo, removendo-os ou ajustando-os.')

    st.write('Base de dados com a coluna Frequência sem remoção de outliers')
    st.write(df.head)

    # Identificar e remover outliers em 'CO2 Emissions (g/km)'
    st.subheader('Identificar e remover outliers em CO2 Emissions (g/km)')
    Q1 = df['CO2 Emissions(g/km)'].quantile(0.25)
    Q3 = df['CO2 Emissions(g/km)'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    st.subheader('Após identificar e remover outliers em CO2 Emissions (g/km)')
    df = df[(df['CO2 Emissions(g/km)'] >= lower_bound) & (df['CO2 Emissions(g/km)'] <= upper_bound)]
    st.write(df)

    st.write('Problema 2: Dados Incompatíveis')
    st.write('Problema: Valores que não fazem sentido nas colunas.')
    st.write('Dimensões de Qualidade Afetadas: Consistência, Validade.')
    st.write('Solução: Verificar valores únicos em cada coluna e corrigir ou remover valores inconsistentes.')

    st.write('Exemplo: Verificar valores únicos em Fuel Type')
    unique_fuel_types = df['Fuel Type'].unique()
    # Se houver valores incorretos, corrigir ou remover
    st.write(df)


    st.write('Padronizando as colunas numéricas')

    scaler = StandardScaler()

    # Selecionar colunas numéricas
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # Criar uma cópia do DataFrame para evitar o aviso
    df_copy = df.copy()

    # Padronizar as colunas numéricas
    df_copy[numeric_columns] = scaler.fit_transform(df_copy[numeric_columns])

    # Atribuir de volta ao DataFrame original
    df = df_copy
    df_copy
