# 📊 Dashboard de Análise de Vendas - Mercado Livre

Este é um projeto interativo desenvolvido em Python para analisar, tratar e comparar o desempenho de vendas dos principais fabricantes de notebooks comercializados no Mercado Livre. 

A aplicação transforma planilhas brutas do Excel em uma interface visual dinâmica, facilitando a tomada de decisão através de indicadores de desempenho (KPIs) e análise gráfica de tendências.

---

## 🚀 Principais Funcionalidades

### 🔍 Filtros Dinâmicos e Inteligentes
* **Seleção Multi-escolha:** Permite filtrar múltiplos fabricantes simultaneamente através da barra lateral (`st.sidebar`).
* **Recálculo Instantâneo:** Toda a base de dados, métricas e gráficos se atualizam automaticamente assim que um filtro é aplicado ou removido.

### 💰 Indicadores de Desempenho (KPIs)
* **Faturamento Total:** Exibição destacada do somatório absoluto da receita bruta gerada por todas as vendas.
* **Média de Receita:** Cálculo automatizado do valor médio faturado por transação ou fabricante.
* **Formatação Monetária:** Valores exibidos no padrão brasileiro de moeda (`R$ 0.000,00`).

### 📉 Análise Visual Integrada
* **Gráfico de Barras:** Comparativo visual do faturamento total consolidado por cada fabricante.
* **Gráfico de Linhas:** Demonstração da variação da média de faturamento, ideal para identificar quais marcas possuem maior ticket médio.
* **Cores por Categoria:** Gráficos configurados com legendas automáticas e cores distintas para cada empresa mapeada.

### 🏆 Inteligência de Negócio e Destaques
* **Produto Campeão:** Identificação automática do modelo de notebook mais vendido na base de dados com base no volume físico de unidades.
* **Controle de Escala:** Exibição correta da volumetria convertida para números inteiros (removendo decimais de sistema).
* **Ranking Geral:** Tabela classificatória ordenando as empresas do maior para o menor faturamento (Empresas TOP ONE).

---

## 📂 Estrutura de Arquivos Recomendada

Para que o projeto funcione perfeitamente, garanta que a estrutura do seu diretório esteja organizada da seguinte forma:

```text
ANALISEDADOS/
│
├── Dados.xlsx          # Planilha Excel contendo os dados brutos de vendas
├── scraping.py         # Código-fonte principal da aplicação Streamlit
├── .gitignore          # Arquivo para impedir o envio de arquivos temporários e de sistema
└── README.md           # Documentação explicativa do repositório
```

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python:** Linguagem de programação de alto nível utilizada para toda a lógica de processamento.
* **Streamlit:** Framework focado em dados usado para construir a interface web e os componentes visuais interativos.
* **Pandas:** Biblioteca de alta performance utilizada para manipulação, agrupamento (`groupby`) e ordenação dos dados.
* **OpenPyXL:** Mecanismo interno de leitura integrado ao Pandas para interpretar arquivos no formato `.xlsx`.

---

## 📦 Como Instalar e Executar Localmente

Siga os passos abaixo no terminal para rodar o dashboard no seu computador:

### 1. Clonar ou Baixar o Projeto
Baixe os arquivos deste repositório para uma pasta local na sua máquina.

### 2. Instalar as Dependências do Projeto
Execute o comando de instalação do gerenciador de pacotes do Python para garantir todas as bibliotecas necessárias:
```bash
pip install streamlit pandas openpyxl
```

### 3. Executar a Aplicação
Inicie o servidor local do Streamlit apontando para o seu arquivo principal de código (caso seu arquivo tenha outro nome, substitua `scraping.py` pelo nome correto):
```bash
streamlit run scraping.py
```

Após o comando, o Streamlit abrirá uma nova aba automaticamente no seu navegador web padrão (geralmente no endereço `http://localhost:8501`) exibindo o seu painel completo.

## 👨‍💻 Autores
Desenvolvedor
Anna Luíza Watanabe

Professor
Wallace Oliveira dos Santos
