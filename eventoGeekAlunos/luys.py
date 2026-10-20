carro = input("Qual seu carro? ")
nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade "))
corfavorita = input("Qual sua cor favorita? ")

coisasdapessoa = {
" Seu nome" : nome,
" Seu carro" : carro,
" Sua idade" : idade,
" Sua Cor Favorita" : corfavorita
}

print("Seu nome é:", coisasdapessoa[" Seu nome"])
print("Seu carro é:", coisasdapessoa[" Seu carro"])
print("Sua cor favorita é:", coisasdapessoa[" Sua Cor Favorita"])
print("Sua idade é:", coisasdapessoa[" Sua idade"])


