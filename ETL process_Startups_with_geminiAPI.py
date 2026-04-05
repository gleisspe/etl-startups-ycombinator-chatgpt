import pandas as pd
import google.generativeai as genai # Biblioteca do Gemini

# Configurando minha APIKEY.
# Lembre-se de colocar sempre sua chave APIKEY que você pega no site (seja do gpt ou gemini)
GOOGLE_API_KEY = "AIzaSyD1R1QDDAwExwHHyUEBe05SC9nhxrvv9tA"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Buscando meu arquivo que escolhi na base de dados do kaggle.
# No caso escolhi uma base de dados sobre startups porque trabalhei com elas ano passado como analista de inovação.
try:
    df_startups = pd.read_csv('Startups.csv')
except FileNotFoundError:
    print("Erro: O arquivo Startups.csv não foi encontrado!")
    exit()

# Transformando um pouco o arquivo selecionado!
# Filtrando apenas USA porque estou residindo no Texas atualmente
df_usa = df_startups[df_startups['Headquarters (Country)'] == 'USA'].copy()

# Selecionando apenas colunas úteis nesse primeiro momento
colunas_uteis = ['Company', 'Satus', 'Year Founded', 'Headquarters (US State)', 'Description']
df_limpo = df_usa[colunas_uteis]

# Gerando o resumo para a IA
resumo_estados = df_limpo['Headquarters (US State)'].value_counts().head(5)
print(f"Top 5 estados com mais startups:\n{resumo_estados}")

#Quero saber o top 5 de investidores de startups dos EUA para tirar inisights
df_startups.info()
investidores_series = df_startups['Investors'].dropna()
todos_investidores = investidores_series.str.split(', ').explode()
top_5_investidores = todos_investidores.value_counts().head(5)

print("\n--- Top 5 Maiores Investidores (Frequência) ---")
print(top_5_investidores)

# Gerando pensamentos com a IA baseados em minha vivencia em todo o ecosssistema no brasil!
def gerar_insight_ia(resumo):
    prompt = f"""
    Analise este resumo de startups da Y Combinator nos EUA: {resumo}.
    Explique brevemente por que o primeiro estado da lista domina tanto o cenário 
    e se existe algum incentivo fiscal ou histórico conhecido.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao conectar com Gemini: {e}. (Reposta Genérica caso erro***: A Califórnia domina devido ao Vale do Silício)."

# Executando a IA
insight = gerar_insight_ia(resumo_estados.to_dict())
print("\n--- Insight da IA Gemini ---")
print(insight)

# Salvando o resultado para finalizar o processo ETL
df_limpo.to_csv('startups_processadas.csv', index=False)
print("\nProcesso ETL concluído! Arquivo 'startups_processadas.csv' gerado.")