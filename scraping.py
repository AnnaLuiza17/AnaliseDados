import streamlit as st #importei minha biblioteca e apilidei
import pandas as pd 

dados = pd.read_excel("Dados.xlsx") #dados está recebendo o excel, usando pandas (pd) e o método read_excel para ler a tabela do excel
print(dados)

st.title("📊 Análise de Dados - Dashboard") #streamlit(st) vai buscar um título
st.subheader("Comparativo dos principais notebooks vendidos no Mercado Livre")
st.write("Quantidade de empresas analisadas", dados["FABRICANTE"].nunique()) #dado[] aponta para a coluna que eu quero e ninuque() vai contar 
                                                                            #*concout é a quantidade de linhas 

st.sidebar.title("🔍Filtro") #sidebar será a barra que fica na esquerda

fabricantes = st.sidebar.multiselect("Empresas", dados["FABRICANTE"].unique()) #multiselect é a multipla escolha do filtro com o unique para não repetir o mesmo nome

if fabricantes:
    dados = dados[dados["FABRICANTE"].isin(fabricantes)] #dados vai receber a planilha toda, depois especificamente a coluna fabricante apontando para dados | isin aplica o filtro
    st.balloons() # NOVO: Solta balões subindo pela tela sempre que um filtro for ativado!

# NOVO COMPONENTE: Adicionado o seletor para você escolher a cor da linha dinamicamente na tela
cor_da_linha = st.sidebar.color_picker("🎨 Cor do Gráfico de Linha", "#9b2ec2")

# NOVO COMPONENTE: Caixinha para escolher se quer ver as tabelas no dashboard ou esconder para limpar o visual
mostrar_tabelas = st.sidebar.checkbox("📋 Mostrar tabelas de dados", value=True)

col1, col2 = st.columns(2)

with col1:
    st.metric("TOTAL RECEITA BRUTA", f"R$ {dados['TOTAL'].sum():,.2f}") #metric é o quantidade, é a média , é o total | sum é a soma

with col2:
    st.metric("MÉDIA RECEITA BRUTA", f"R$ {dados['TOTAL'].mean():,.2f}") #mean é a média

st.write("Gráfico de Barras - TOTAL de Vendas em R$💵")

# AJUSTE: O .reset_index() foi adicionado para o Streamlit aceitar o x, y e a cor com legenda
st.bar_chart(
    dados.groupby("FABRICANTE")["TOTAL"].sum().reset_index(), 
    x="FABRICANTE", 
    y="TOTAL", 
    color="FABRICANTE"
) #bar_chart é o gráfico de barras 
  #a tabela dados vai agrupar por fabricante e total, depois ele soma e gera o gráfico

# st.bar_chart(dados.groupby("FABRICANTE")["TOTAL"].sum(), color="#9b2ec2") 

# MELHORIA: Agora a cor do seu gráfico de linha obedece ao que você selecionar no color_picker da barra lateral
st.line_chart(dados.groupby("FABRICANTE")["TOTAL"].mean(), color=cor_da_linha) #gráfico de linha com a média

# MELHORIA: Só exibe a tabela principal se a caixinha na barra lateral estiver marcada
if mostrar_tabelas:
    st.dataframe(dados) #tela da planilha 

# mais_vendido = dados.loc[dados["QUANTIDADE"].idxmax()] 
# st.metric("Produto mais vendido", mais_vendido["PRODUTO"]) #o índice selecionado vai na coluna produto e retorna um nome
                              
mais_vendido = dados.loc[dados["QUANTIDADE"].idxmax()] #vai nessa coluna e me da o índice de maior valor e retornar o índice
                                                        #o loc vai localizar o índice e colocar no mais vendido
 
st.caption("Produto mais vendido") # rótulo do produto

st.write(f"**{mais_vendido['PRODUTO']}**") #Usamos o st.write com ** para deixar o texto em tamanho normal de leitura, mas destacado em negrito

st.caption("Unidades vendidas") # rótulo da quantidade
st.write(f"**{int(mais_vendido['QUANTIDADE'])}** unidades") # CORREÇÃO: int() remove o '.0' do número

 
#st.caption("Produto mais vendido") # cria o rótulo cinza e pequeno no topo
# st.subheader(f"{mais_vendido['PRODUTO']} ({mais_vendido['QUANTIDADE']} un.)") # exibe o nome e a quantidade ao lado entre parênteses
                                                                            # exibe o nome do produto com uma letra menor que não vai cortar

ranking = dados.groupby("FABRICANTE")["TOTAL"].sum().sort_values(ascending=False) #agrupando por fabricante total para fazer a soma e ordenar do maior para o menor
# MELHORIA: O ranking também obedece à caixinha de mostrar/esconder tabelas
if mostrar_tabelas:
    st.subheader("Raking da Empresas TOP ONE 🥇")
    st.dataframe(ranking)
