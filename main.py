import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Ler base de dados
dados = pd.read_csv("dados.csv")

# Separar textos e sentimentos
X = dados["texto"]
y = dados["sentimento"]

# Transformar texto em números
vectorizer = CountVectorizer()

X_transformado = vectorizer.fit_transform(X)

# Criar modelo
modelo = MultinomialNB()

# Treinar
modelo.fit(X_transformado, y)

print("=== CLASSIFICADOR DE SENTIMENTOS ===")

while True:

    frase = input("\nDigite uma frase (ou sair): ")

    if frase.lower() == "sair":
        break

    frase_transformada = vectorizer.transform([frase])

    resultado = modelo.predict(frase_transformada)

    print("\nSentimento:", resultado[0])
