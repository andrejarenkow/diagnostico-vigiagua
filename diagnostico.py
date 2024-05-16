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
        
container_titulo = st.container()       
with container_titulo:
    coluna_inicial1,coluna_inicial2,coluna_inicial3 = st.columns([1,8,1])

    with coluna_inicial2:
        st.markdown(f'<h1 style="text-align: center;color:#FFFFFF;font-size:42px;">{"FORMULÁRIO VIGIAGUA - VIGIDESASTRES"}</h1>', unsafe_allow_html=True)    
        st.markdown(f'<h1 style="text-align: center;color:#FFFFFF;font-size:24px;">{"CRS/CEVS/Secretaria de Saúde do Estado do Rio Grande do Sul"}</h1>', unsafe_allow_html=True)

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
# Lê os dados de um arquivo Excel online
dados = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1V6v6pqt21cR3yHkkraQJMYdutJg2PAM1T8nKpRxd-VE/edit?usp=sharing")

ws = conn.get_worksheet('Tabela1')

#CODIGO_PLANILHA = '1V6v6pqt21cR3yHkkraQJMYdutJg2PAM1T8nKpRxd-VE'
#gc = gspread.service_account(filename='key.json')
#sh = gc.open_by_key(CODIGO_PLANILHA)
#ws = sh.worksheet('Página1')
container_Sbox = st.container()
col1,colcenter2,col3 = st.columns(3)
# Cria um seletor para escolher a Regional de Saúde
with container_Sbox:
    with colcenter2:
        crs = st.selectbox('COORDENADORIA REGIONAL DE SAÚDE', options=dados['Regional de Saúde'].unique(), index=None, placeholder='Selecione uma CRS', key='crs')
        
        # Cria um seletor para escolher o município com base na Regional de Saúde selecionada
        municipio = st.selectbox('MUNICÍPIO', options=sorted(dados[dados['Regional de Saúde']==crs]['Município'].unique()), index=None, placeholder='Selecione uma município', key='municipio')
        
        # Cria um seletor para escolher o tipo da forma de abastecimento com base no município selecionado
        tipo_forma_abastecimento = st.selectbox('TIPO DA FORMA DE ABASTECIMNENTO', options=sorted(dados[dados['Município']==municipio]['Tipo da Forma de Abastecimento'].unique()), index=None, placeholder='Selecione um tipo de forma de abastecimento', key='forma')

        st.markdown(
            f"""
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) {{
                box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.25);
                border: 2px solid white;
                border-radius: 15px;
                padding: 15px;
            }}
            </style>
            """,
            unsafe_allow_html=True
            
        )        
        st.markdown(
            f"""
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(1) > div > div {{
                background-color: #FFFFFF; /* Verde bem clarinho */
                border: 1px solid white; /* Borda verde */
                border-radius: 10px;
                padding: 0px;
                max-width: calc(100% - 25px);
                margin-left: 20px;
            }}
            </style>
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div {{
                background-color: #FFFFFF; /* Verde bem clarinho */
                border: 1px solid white; /* Borda verde */
                border-radius: 10px;
                padding: 0px;
                max-width: calc(100% - 25px);
                margin-left: 20px;
            }}
            </style>
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(3) > div > div {{
                background-color: #FFFFFF; /* Verde bem clarinho */
                border: 1px solid white; /* Borda verde */
                border-radius: 10px;
                padding: 0px;
                max-width: calc(100% - 25px);
                margin-left: 20px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(1) > div > label {{
                text-align: center;
                margin: 0 auto; /* Centraliza horizontalmente */
                display: table;
            }}
            </style>
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(2) > div > label {{
                text-align: center;
                margin: 0 auto; /* Centraliza horizontalmente */
                display: table;
            }}
            </style>
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(3) > div > label {{
                text-align: center;
                margin: 0 auto; /* Centraliza horizontalmente */
                display: table;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # Filtra os dados para exibir apenas as informações relevantes com base no município e tipo da forma de abastecimento selecionados
        dados_municipio = dados[(dados['Município']==municipio)&(dados['Tipo da Forma de Abastecimento']==tipo_forma_abastecimento)][['Nome da Forma de Abastecimento','Sem informação', 'Funcionando', 'Parada/danificada']]
        
container_data_editor = st.container()
with container_data_editor:
    col4,colcenter5,col6 = st.columns([1,2,1])
    try:
        # Tenta executar as seguintes instruções
        # Comentários abaixo são comentários de código, não estão habilitados no momento devido ao formato da entrada.
        # st.subheader(f'{tipo_forma_abastecimento} no município de {municipio}')
        with colcenter5:
            st.markdown(f'<h1 style="text-align: center;color:#FFFFFF;font-size:16px;">{"Marque o status de cada uma para informar seu status"}</h1>', unsafe_allow_html=True)  # Exibe uma mensagem para o usuário
            edited_df = st.data_editor(dados_municipio, use_container_width=True, hide_index=True)  # Exibe os dados do município para edição
            
            # Cria um botão para enviar a atualização e redefine o estado da sessão quando clicado           
            submit = st.button('Enviar atualização!', type='primary', on_click=reset)
            
            st.markdown(f'''
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div > div > div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div:nth-child(3) > div {{
                display: flex;
                justify-content: center; /* Centraliza horizontalmente */
                align-items: center;
            }}
            </style>
            ''', unsafe_allow_html=True)
            
            # Verifica se o botão de envio foi clicado
            if submit:
                lista_atualizacoes = []
                mudancas = []
                for index, row in dados.iterrows():
                    matching_rows = edited_df[
                        (edited_df['Nome da Forma de Abastecimento'] == row['Nome da Forma de Abastecimento']) &
                        (edited_df['Município'] == row['Município'])
                    ]
                    for _, match in matching_rows.iterrows():
                        # Armazenar dados antes da mudança
                        old_values = row[['Sem informação', 'Funcionando', 'Parada/danificada']].tolist()
                        new_values = [match['Sem informação'], match['Funcionando'], match['Parada/danificada']]
                        
                        # Verificar se realmente há uma mudança
                        if old_values != new_values:
                            lista_atualizacoes.append({
                                'range': f'A{index+2}:D{index+2}',
                                'values': [new_values]
                            })
                            mudancas.append({
                                'Index': index,
                                'Antes': old_values,
                                'Depois': new_values
                            })
                
                # Atualizar a planilha
                for update in lista_atualizacoes:
                    conn.update(worksheet=ws, range=update['range'], values=update['values'])
                try:
                    st.markdown(f'<h1 style="text-align: center;color:#FFFFFF;font-size:16px;">{"As linhas modificadas na tabela foram:"}</h1>', unsafe_allow_html=True)
                    df_mudancas = pd.DataFrame(mudancas)
                except Exception as x_error:
                    st.write(x_error)
                #conn.update(data=dados)
                    
                # Exibe uma mensagem de sucesso quando a atualização é enviada
                st.success(f'st.success(f"Atualização enviada! {len(lista_atualizacoes)} linhas foram atualizadas.")!', icon="✅")
                st.dataframe(df_mudancas)
                st.cache_data.clear()  # Limpa o cache de dados
                
                # Exibe uma mensagem para o usuário
                
    except Exception as erro_ultimo:
        # Se ocorrer uma exceção, exibe uma mensagem em branco
        st.write(erro_ultimo)
