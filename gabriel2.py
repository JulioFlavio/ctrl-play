nome = input("Qual e o seu nome?")
idade = int(input("Quantos anos voce tem?"))

arquivo = open("arquivo.txt", "w")
arquivo.write(f"Voce tem {idade} anos e seu nome e {nome}")