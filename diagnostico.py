import pandas as pd  # Importa a biblioteca pandas e a renomeia como pd
import streamlit as st # Importa a biblioteca streamlit e a renomeia como st
from streamlit_gsheets import GSheetsConnection

pd.options.display.max_columns=None
st.set_page_config(
    page_title="Form",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state='collapsed')

def reset():
    # Função para redefinir o estado da sessão
    # Comentários abaixo são comentários de código, não estão habilitados no momento devido ao formato da entrada.
    # conn.update(
    #         worksheet="dados_form",
    #         data=df,
    #     )
    for key in st.session_state.keys():
        # Itera sobre as chaves do estado da sessão e redefine seus valores para None
        st.session_state[key] = None
        

try:
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    print(conn)
    # Lê os dados de um arquivo Excel online
    dados = conn.read('Página1')
except Exception as e:
    print(e)

#CODIGO_PLANILHA = '1V6v6pqt21cR3yHkkraQJMYdutJg2PAM1T8nKpRxd-VE'
#gc = gspread.service_account(filename='key.json')
#sh = gc.open_by_key(CODIGO_PLANILHA)
#ws = sh.worksheet('Página1')

col1,colcenter2,col3 = st.columns(3)
# Cria um seletor para escolher a Regional de Saúde
with colcenter2:
    crs = st.selectbox('Selecione a CRS', options=dados['Regional de Saúde'].unique(), index=None, placeholder='Selecione uma CRS', key='crs')
    
    # Cria um seletor para escolher o município com base na Regional de Saúde selecionada
    municipio = st.selectbox('Selecione o município', options=sorted(dados[dados['Regional de Saúde']==crs]['Município'].unique()), index=None, placeholder='Selecione uma município', key='municipio')
    
    # Cria um seletor para escolher o tipo da forma de abastecimento com base no município selecionado
    tipo_forma_abastecimento = st.selectbox('Selecione o tipo da forma de abastecimento', options=sorted(dados[dados['Município']==municipio]['Tipo da Forma de Abastecimento'].unique()), index=None, placeholder='Selecione um tipo de forma de abastecimento', key='forma')

# Filtra os dados para exibir apenas as informações relevantes com base no município e tipo da forma de abastecimento selecionados
dados_municipio = dados[(dados['Município']==municipio)&(dados['Tipo da Forma de Abastecimento']==tipo_forma_abastecimento)][['Nome da Forma de Abastecimento','Sem informação', 'Funcionando', 'Parada/danificada']]
col4,colcenter5,col6 = st.columns([1,2,1])
try:
    # Tenta executar as seguintes instruções
    # Comentários abaixo são comentários de código, não estão habilitados no momento devido ao formato da entrada.
    # st.subheader(f'{tipo_forma_abastecimento} no município de {municipio}')
    with colcenter5:
        st.write('Marque o status de cada uma para informar seu status')  # Exibe uma mensagem para o usuário
        st.data_editor(dados_municipio, use_container_width=True, hide_index=True)  # Exibe os dados do município para edição
    
        # Cria um botão para enviar a atualização e redefine o estado da sessão quando clicado
        submit = st.button('Enviar atualização!', type='primary', on_click=reset)
    
        # Verifica se o botão de envio foi clicado
        if submit:
            # Exibe uma mensagem de sucesso quando a atualização é enviada
            st.success('Atualização enviada!', icon="✅")
            st.cache_data.clear()  # Limpa o cache de dados

except:
    # Se ocorrer uma exceção, exibe uma mensagem em branco
    st.write('')
