positivas = [
    "bom",
    "otimo",
    "excelente",
    "feliz",
    "gostei",
    "maravilhoso",
    "incrivel",
    "legal",
    "amei"
]

# Palavras negativas
negativas = [
    "ruim",
    "pessimo",
    "horrivel",
    "triste",
    "odiei",
    "terrivel",
    "decepcionado",
    "mal"
]

print("CLASSIFICADOR DE SENTIMENTOS")

while True:

    frase = input("\nDigite uma frase (ou 'sair'): ").lower()

    if frase == "sair":
        print("Programa encerrado.")
        break

    positivo = 0
    negativo = 0

    palavras = frase.split()

    for palavra in palavras:
        if palavra in positivas:
            positivo += 1

        if palavra in negativas:
            negativo += 1

    if positivo > negativo:
        print("Sentimento: POSITIVO")

    elif negativo > positivo:
        print("Sentimento: NEGATIVO")

    else:
        print("Sentimento: NEUTRO")
