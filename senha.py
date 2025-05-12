senha=12345
while True:
    senhas = int(input("digite a senha"))
    if senhas== senha:
        print("acesso liberado")
        break
    else:
        print("senha errada")