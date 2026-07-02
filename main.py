import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Carregar base de dados
dados = pd.read_csv("dados.csv")

# Separar textos e rótulos
X = dados["texto"]
y = dados["sentimento"]

# Converter texto em números
vectorizer = CountVectorizer()
X_vectorizado = vectorizer.fit_transform(X)

# Separar treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X_vectorizado,
    y,
    test_size=0.2,
    random_state=42
)

# Criar e treinar modelo
modelo = MultinomialNB()
modelo.fit(X_treino, y_treino)

# Avaliação
previsoes = modelo.predict(X_teste)

print("=" * 50)
print("CLASSIFICADOR DE SENTIMENTOS")
print("=" * 50)
print(f"Acurácia: {accuracy_score(y_teste, previsoes):.2f}")
print("\nRelatório de Classificação:")
print(classification_report(y_teste, previsoes))

# Classificação interativa
while True:
    frase = input("\nDigite uma frase (ou 'sair'): ")

    if frase.lower() == "sair":
        print("Programa encerrado.")
        break

    frase_vetor = vectorizer.transform([frase])
    resultado = modelo.predict(frase_vetor)

    print(f"Sentimento identificado: {resultado[0]}")
