import pandas as pd
import streamlit as st

dados = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vTnQORvrZiO6l26dKcj9alqq76X1sP7IdLjfSwu-FVhj2b3pM8PvjPGVEHcDt6nhhIkFXy-utm9FIQ9/pub?output=xlsx')

crs = st.selectbox('Selecione a CRS', options=dados['Regional de Saúde'].unique(), index=None)
municipio = st.selectbox('Selecione o município', options=dados[dados['Regional de Saúde']==crs]['Município'].unique(), index=None)
tipo_forma_abastecimento = st.selectbox('Selecione o município', options=dados[dados['Município']==municipio]['Tipo da Forma de Abastecimento'].unique(), index=None)
dados_municipio = dados[(dados['Município']==municipio)&(dados['Tipo da Forma de Abastecimento']==tipo_forma_abastecimento)]
try:
  st.dataframe(dados_municipio)

except:
  st.write('')
