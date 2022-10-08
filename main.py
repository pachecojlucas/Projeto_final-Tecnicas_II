############################################
# Construindo uma aplicação com streamlit  #
#                                          #
# instalação: pip install streamlit        #
#                                          #
# executar: streamlit run main.py          #
#                                          #
# Prof: Tiago Dias                         #
############################################

# importar bibliotecas
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import missingno as msno

# função principal da aplicação
def app():
        # titulo da aplicação
        st.title('Projeto Final: Técnicas de Programação II Python')
        # sub titulo da aplicação
        st.subheader('Utilizando Framework Streamlit')
        # adicionando uplouder buttom
        uplouded_file = st.file_uploader(label="Faça o uploud do seu arquivo csv aqui!", type=['csv'])
        # ler arquivo csv
        if uplouded_file is not None:
                df = pd.read_csv(uplouded_file)
                # adicionar texto na página
                st.markdown('Dimensão da **Base de Dados**')
                # escrever informações do dataset
                st.write('Número de observações', df.shape[0], 'Número de colunas', df.shape[1])
                # adicionar texto na página
                st.markdown('Soma de dados nulos da **Base de Dados**')
                # escrever informações de soma de dados nulos
                st.write(df.isnull().sum())
                # adicionar texto na página
                st.markdown('Percentual de dados nulos da **Base de Dados**')
                # escrever informações de percentual de dados nulos
                st.write(round(df.isna().sum()/len(df)*100,2))
                # adicionar texto na página
                st.markdown('Visualizando dados nulos da **Base de Dados**')
                # exibindo um gráfico de dados nulos
                nulos = msno.matrix(df, color=(0.27, 0.52, 1.0))
                st.pyplot(nulos.figure)
                # adicionar texto na página
                st.markdown('Primeiros registros da **Base de Dados**')
                # exibindo as primeiras linhas do dataframe
                st.dataframe(df.head())
                #Gerar gráficos:
                if st.checkbox('Gerar gráficos de dados categoricos'):
                        # criar um selectbox com as colunas do dataframe
                        colunaC = st.selectbox('Selecione uma coluna', list(df.select_dtypes(include=object).columns))
                        # adicionar texto na página
                        st.markdown('Gráfico de **Barras**')
                        # exibindo um gráfico de barras seaborn
                        fig, ax = plt.subplots()
                        # criando um gráfico de barras
                        sns.countplot(data=df, x=colunaC, ax=ax)
                        fig.set_size_inches(38.5, 30.5)
                        ax.set_xlabel(colunaC, fontsize=30)
                        ax.set_ylabel('Count', fontsize=20)
                        # levando o gráfico para a aplicação
                        st.pyplot(fig)
                        # adicionar texto na página
                if st.checkbox('Gerar gráficos de comparação entre variaveis'):
                        coluna = st.selectbox('Selecione primeira coluna', list(df.columns))
                        coluna2 = st.selectbox('Selecione a segunda coluna', list(df.columns))
                        st.markdown('Gráfico de **Dispersão Seaborn**')
                        # exibindo um gráfico de dispersão seaborn
                        fig, ax = plt.subplots()
                        # criando um gráfico de dispersão
                        sns.regplot(data=df, x=coluna, y=coluna2)
                        # levando o gráfico para a aplicação
                        st.pyplot(fig)
                if st.checkbox('Gerar heatmap para correlação entre dados'):
                        st.markdown('Gráfico de **Calor Seaborn**')
                        # exibindo um gráfico de heatmap seaborn
                        fig, ax = plt.subplots()
                        # criando um gráfico de heatmap
                        sns.heatmap(df.corr(), cmap="Blues_r", annot=True)
                        # levando o gráfico para a aplicação
                        st.pyplot(fig)
                if st.checkbox('Gerar dados estatísticos de percentual'):
                        # criar um selectbox com as colunas do dataframe
                        coluna4 = st.selectbox('Selecione uma coluna para gerar coisas', list(df.select_dtypes(include=object).columns))
                        # exibindo um gráfico de pizza
                        fig, ax = plt.subplots()

                        ax.pie(df[coluna4].value_counts().values, labels=df[coluna4].value_counts().index, autopct = '%1.1f%%')
                        fig.set_size_inches(28.5, 20.5)
                        # levando o gráfico para a aplicação
                        st.pyplot(fig)
                        # Input de texto do usuário
                        texto = st.text_input('Digite o seu nome!!! Você chegou ao final da aplicação!!!')
                        # Escrevendo o texto do usuário na tela
                        if texto:
                                st.write('Obrigado', texto, 'volte sempre!!!')

        # chamada para executar a aplicação principal
if __name__ == '__main__':
        app()