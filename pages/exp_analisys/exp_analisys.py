import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def exp_analisys():
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

    # Explore the dataset

    st.write('Explorando a base de dados:')
    st.write(df.head()) # View first few rows
    st.write(df.info()) # Get information about the dataset
    st.write(df.isnull().sum()) # Verificar dados faltantes
    st.write(df.describe())

    # Calcular média e desvio padrão para todas as variáveis
    n_list = ['Engine Size(L)', 'Cylinders',                              
'Fuel Consumption City (L/100 km)',     
'Fuel Consumption Hwy (L/100 km)' ,     
'Fuel Consumption Comb (L/100 km)',     
'Fuel Consumption Comb (mpg)',          
'CO2 Emissions(g/km)']
    dfn = df[n_list]
    st.write('Calculando média e desvio padrão para as colunas:')
    st.write(dfn.mean())
    st.write(dfn.std())

    
    st.title('1. Análise exploratória')
    
        # Histograma de Emissões de CO2
    st.subheader('Histograma de Emissões de CO2')
    fig_1, ax = plt.subplots()
    sns.barplot(x='CO2 Emissions(g/km)', y='Frequency', data=df)
    plt.figure(figsize=(10, 6))
    plt.hist(df['CO2 Emissions(g/km)'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Histograma de Emissões de CO2')
    plt.xlabel('CO2 Emissions (g/km)')
    plt.ylabel('Frequency')
    st.pyplot(fig_1)
 
    # Gráfico de Dispersão entre Tamanho do Motor e Emissões de CO2
    st.subheader('Gráfico de Dispersão entre Tamanho do Motor e Emissões de CO2')
    fig_2, ax = plt.subplots()    
    sns.scatterplot(x='Engine Size(L)', y='CO2 Emissions(g/km)', data=df, color='coral')
    plt.figure(figsize=(10, 6))
    plt.title('Gráfico de Dispersão entre Tamanho do Motor e Emissões de CO2')
    plt.xlabel('Engine Size(L)')
    plt.ylabel('CO2 Emissions (g/km)')
    st.pyplot(fig_2)
 
    # Boxplot por Tipo de Combustível
    st.subheader('BoxPlot por tipo de Combustível')
    fig_3, ax = plt.subplots()    
    sns.boxplot(x='Fuel Type', y='CO2 Emissions(g/km)', data=df, palette='viridis', hue='Fuel Type', legend=False)
    plt.figure(figsize=(12, 8))
    plt.title('Boxplot de Emissões de CO2 por Tipo de Combustível')
    plt.xlabel('Fuel Type')
    plt.ylabel('CO2 Emissions (g/km)')
    st.pyplot(fig_3)

    st.write('Resultados e Interpretação:')
    st.write('O resumo estatístico fornece uma visão geral das medidas centrais, variabilidade e distribuição de cada variável no conjunto de dados.')
    st.write('O histograma de emissões de CO2 oferece uma visão da distribuição das emissões, mostrando se estão concentradas em determinadas faixas.')
    st.write('O gráfico de dispersão entre o tamanho do motor e as emissões de CO2 indica padrões ou correlações entre essas variáveis.')
    st.write('O boxplot por tipo de combustível permite visualizar a variabilidade nas emissões de CO2 para diferentes tipos de combustíveis.')

