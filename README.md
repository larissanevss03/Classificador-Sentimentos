# Classificador-Sentimentos

Este projeto implementa um classificador de sentimentos utilizando Processamento de Linguagem Natural (PLN) e Machine Learning em Python.

O programa é treinado com frases positivas e negativas e classifica novas frases como:

- Positivo
- Negativo

## Tecnologias

- Python 3
- Pandas
- Scikit-learn

## Instalação

Clone o repositório e após entre na pasta:

```bash
cd classificador-sentimentos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python main.py
```

## Exemplo

```
=== CLASSIFICADOR DE SENTIMENTOS COM IA ===

Digite uma frase:
O atendimento foi excelente

Sentimento: Positivo
```

## Como funciona

O projeto utiliza:

- CountVectorizer para transformar texto em números;
- Multinomial Naive Bayes para treinar um modelo de classificação;
- Machine Learning para prever o sentimento de novas frases.
