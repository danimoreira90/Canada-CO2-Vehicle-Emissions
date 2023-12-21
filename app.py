import streamlit as st
from pages.main import main
from pages.exp_analisys import exp_analisys
from pages.data_quality import data_quality
from pages.results import results

st.set_page_config(layout="wide")

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', 'Explorando os dados', 'Qualidade de dados', 'Resultado da regressão linear'])

if menu == 'Principal':
    main.main()
elif menu == 'Explorando os dados':
    exp_analisys.exp_analisys()
elif menu == 'Qualidade de dados':
    data_quality.data_quality()
elif menu == 'Resultado da regressão linear':
    results.results()
