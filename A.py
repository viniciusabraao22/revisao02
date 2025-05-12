contador = 0
palavra = input("Digite uma frase: ")  # Agora o usuário pode inserir a frase

for i in palavra.lower():
    if i == "a":  # Verifica cada caractere da string
        contador += 1

print(f"Quantos 'A' tem a frase: {contador}")
