import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#Projeto PLN - utilizei a biblioteca scikit-learn

dados = {
    "texto": [
        "Adorei esse filme",
        "Muito bom",
        "Excelente atendimento",
        "Gostei bastante",
        "Estou feliz",
        "Produto maravilhoso",
        "Não gostei",
        "Muito ruim",
        "Péssimo atendimento",
        "Estou decepcionado",
        "Foi horrível",
        "Nunca mais compro"
    ],
    "sentimento": [
        "Positivo",
        "Positivo",
        "Positivo",
        "Positivo",
        "Positivo",
        "Positivo",
        "Negativo",
        "Negativo",
        "Negativo",
        "Negativo",
        "Negativo",
        "Negativo"
    ]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Transformar texto em números
vetor = CountVectorizer()
X = vetor.fit_transform(df["texto"])

# Criar e treinar o modelo de IA
modelo = MultinomialNB()
modelo.fit(X, df["sentimento"])

print("=== CLASSIFICADOR DE SENTIMENTOS COM IA ===")

while True:
    frase = input("\nDigite uma frase (ou 'sair'): ")

    if frase.lower() == "sair":
        print("Programa encerrado.")
        break

    frase_transformada = vetor.transform([frase])
    resultado = modelo.predict(frase_transformada)

    print("Sentimento:", resultado[0])
