# etl-startups-ycombinator-chatgpt
Pipeline de ETL com Python para análise dessa base de dados retirada do Kaggle onde analisei as principais cidades dos EUA com a maior densidade de startups e também os 5 maiores investidores de Startups dos EUA. Usei a biblioteca PANDAS e API'S do GOOGLE GEMINI e do CHATGPT.

Escolhi esse projeto pois ele faz referencia a minha última posição profissional como analista de inovação, analisando o ecossistema e buscando soluções de problemas com contato direto com startups!

# 🚀 Análise de Dados: Ecossistema de Startups dos EUA

Este projeto foi desenvolvido como parte de um desafio de **ETL (Extract, Transform, Load)** da plataforma **DIO**. O objetivo principal é processar dados históricos de startups americanas, realizar uma limpeza técnica em valores de investimento e utilizar Inteligência Artificial para gerar insights estratégicos.

## 🧠 Contexto do Projeto
Como Engenheiro de Produção, meu foco foi aplicar a lógica de processos para transformar dados brutos (CSV) em informação de valor. Analisei quase 700 empresas aceleradas pela Y Combinator para entender a dominância geográfica e o papel dos grandes investidores no cenário americano.

## 🛠️ Tecnologias Utilizadas
* **Python**: Linguagem base.
* **Pandas**: Manipulação e limpeza de dados (Dataframes).
* **Google Gemini API**: Geração de insights macroeconômicos automatizados.
* **ChatGPT**: Geração de insigths macroecônomicos automatizados.
* **Kaggle Dataset**: Fonte dos dados originais.

## 📊 O Processo ETL

1.  **Extract (Extração)**: Consumo de base de dados via CSV.
2.  **Transform (Transformação)**: 
    * Filtro focado em Headquarters nos EUA.
    * Tratamento de strings complexas na coluna de Investidores (técnica de `.explode()`).
    * Limpeza financeira (conversão de texto monetário para números reais).
3.  **Load (Carga/Enrichment)**: Integração com a API do Gemini para explicar a concentração de startups no Vale do Silício e o ranking dos Top 5 investidores (Sequoia, 500 Startups, etc).

## 📈 Resultados Obtidos
O pipeline identifica automaticamente as cidades líderes em inovação e correlaciona a presença dos maiores fundos de Venture Capital com o volume de empresas fundadas.

---
Feito por Gleisson Leonardo Pereira - Engenheiro de Produção e Aspirante a Engenheiro de Dados

English ****

Python-based ETL pipeline for analyzing a Kaggle dataset of US startups. I analyzed city density and the Top 5 investors using PANDAS, Google Gemini, and ChatGPT APIs. This project reflects my professional background as an Innovation Analyst, where I specialized in ecosystem mapping and startup-driven problem-solving.
🚀 Data Analytics: US Startup Ecosystem (Y Combinator).

This project was developed as part of an ETL (Extract, Transform, Load) challenge from the DIO platform. The main goal is to process historical data from American startups, perform technical cleaning on investment values, and leverage Artificial Intelligence to generate strategic insights.

🧠 Project Context
As an Industrial Engineer, my focus was applying process logic to transform raw data (CSV) into high-value information. I analyzed nearly 700 Y Combinator-accelerated companies to understand geographic dominance and the role of major investors in the American tech landscape.

This project is directly inspired by my previous role as an Innovation Analyst, where I worked within the startup ecosystem seeking solutions and maintaining direct contact with emerging tech companies.

🛠️ Technologies Used
* **Python**: Core language.
* **Pandas**: Data manipulation and cleaning (DataFrames).
* **Google Gemini API**: Automated macroeconomic insights.
* **ChatGPT (OpenAI API)**: Automated macroeconomic insights.
* **Kaggle Dataset**: Original data source.

📊 The ETL Process
Extract: Data consumption via CSV files.

Transform:

Filtered for US-based Headquarters.

Handled complex strings in the "Investors" column (using the .explode() technique).

Financial cleaning (converting currency strings into float values for numerical analysis).

Load (Enrichment): Integration with the Gemini API to explain the startup concentration in Silicon Valley and the ranking of the Top 5 investors (e.g., Sequoia Capital, 500 Startups).

## 📈 Results 

The pipeline automatically identifies leading cities in innovation and correlates the presence of major venture capital investors with the total number of startups founded.

Made by Gleisson Leonardo Pereira - Industrial Engineer and future Data Engineer
