numero_segredo=56
tentativas=0

print("Tente adivinhar o número secreto entre 1 e 100!")

palpite=0

while palpite != numero_segredo:
    palpite=int(input("digite seu palpite"))
    tentativas = +1

    if palpite <= numero_segredo:
        print("seu numero e menor")
    elif palpite >= numero_segredo:
        print("seu numero e maior")

print("vc acertou")