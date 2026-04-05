import pandas as pd

# Carregando o arquivo anexado
df_startups = pd.read_csv('Startups.csv')

#Raio x para ver todas as colunas da minha base de dados usada.
#df_startups.info()

# Visualizando as primeiras 5 linhas para ver se o código funciona mesmo!!!
print(df_startups.head())

# Irei filtrar apenas as startups listadas nos EUA para fins de verificação qual estado tem mais headquarters, possivelmente veremos SF devido ao vale do silicio.
df_usa = df_startups[df_startups['Headquarters (Country)'] == 'USA'].copy()

# Irei remover colunas que você não vai usar para o impacto (como Logo ou Links)
colunas_uteis = ['Company', 'Satus', 'Year Founded', 'Headquarters (US State)', 'Description']
df_limpo = df_usa[colunas_uteis]

# Criei um resumo para enviar para a IA analisar o porque desse estado ter mais headquartes, se tem algum incentivo
# ou coisa do tipo.
resumo_estados = df_limpo['Headquarters (US State)'].value_counts().head(5)
print(f"Top 5 estados com mais startups:\n{resumo_estados}")

from openai import OpenAI

client = OpenAI(api_key='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')

def gerar_insight_ia(resumo):
    # Apenas comentei a parte da API porque não tinha créditos suficientes na OPENAI para rodar um insigth usando o CHATGPT.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
    """
    # Retornei a resposta abaixo apenas:
    return "Simulação de Insight: A concentração de startups na Califórnia reflete a maturidade do ecossistema do Vale do Silício."


