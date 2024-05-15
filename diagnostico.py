import pandas as pd
import streamlit as st

  def reset():
#    conn.update(
#            worksheet="dados_form",
#            data=df,
#        )
    for key in st.session_state.keys():
        st.session_state[key] = None 

dados = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vTnQORvrZiO6l26dKcj9alqq76X1sP7IdLjfSwu-FVhj2b3pM8PvjPGVEHcDt6nhhIkFXy-utm9FIQ9/pub?output=xlsx')

crs = st.selectbox('Selecione a CRS', options=dados['Regional de Saúde'].unique(), index=None, placeholder='Selecione uma CRS')
municipio = st.selectbox('Selecione o município', options=sorted(dados[dados['Regional de Saúde']==crs]['Município'].unique()), index=None, placeholder='Selecione uma município')
tipo_forma_abastecimento = st.selectbox('Selecione o tipo da forma de abastecimento', options=sorted(dados[dados['Município']==municipio]['Tipo da Forma de Abastecimento'].unique()), index=None, placeholder='Selecione um tipo de forma de abastecimento')
dados_municipio = dados[(dados['Município']==municipio)&(dados['Tipo da Forma de Abastecimento']==tipo_forma_abastecimento)][['Nome da Forma de Abastecimento','Sem informação',	'Funcionando', 'Parada/danificada']]
try:
  st.subheader(f'{tipo_forma_abastecimento} no município de {municipio}')
  st.data_editor(dados_municipio, use_container_width =True, hide_index=True)
  st.write('Marque o status de cada uma para informar seu status')
  submit = st.button('Enviar atualização!', type='primary', on_click=reset)


  if submit:
          st.success('Atualização enviada!', icon="✅")
          st.cache_data.clear()


except:
  st.write('')
