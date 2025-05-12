
nomes = []

for i in range(5):
    nome = input("Digite seu nome: ")
    nomes.append(nome)
    if nome.startswith('A'):
        print(nome)
