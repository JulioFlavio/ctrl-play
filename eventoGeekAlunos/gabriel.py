nome = input("Qual é o seu nome?")
idade = input("\n=====================\nQuantos anos vc tem?")
carro = input("\n==================\nQual é o seu carro?")
cor = input("\n====================\nQual sua cor favorita?")

pessoa = {"nome": nome, "idade": idade, "carro": carro, "cor": cor}
print("Seu nome é", pessoa["nome"], "\n======================\nVocê tem", pessoa["idade"], "anos\n======================\nSeu carro é um", pessoa["carro"], "\n======================\n E sua cor favorita é:", pessoa["cor"])