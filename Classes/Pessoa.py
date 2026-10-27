class Pessoa():
    nome = ""
    idade = 0
    altura = 0
    cor = ""
    __cpf = ""

    def __init__(self, nome, idade, altura, cor, cpf):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cor = cor
        self.__cpf = cpf

    def identificar(self):
        print("================")
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Altura: ", self.altura)
        print("Cor: ", self.cor)
        print("=================")

    def mostrarCPF(self):
        print(self.__cpf)


pessoa1 = Pessoa("Júlio", 22, 210, "Branco", "111.222.333-44")
#Exemplo de criação de objeto (instancia)

class Crianca(Pessoa):
    brinquedo_favorito = ""
    desenho_favorito = ""

    def __init__(self, nome, idade, altura, cor, cpf, brinquedo, desenho):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cor = cor
        self.__cpf = cpf
        self.brinquedo_favorito = brinquedo
        self.desenho_favorito = desenho

    def identificar(self):
        print("================")
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Altura: ", self.altura)
        print("Cor: ", self.cor)
        print(self.desenho_favorito, self.brinquedo_favorito)
        print("=================")


crianca1 = Crianca("Júlio", 12, 160, "Negro", "555.666.777-88", "Carrinho", "Peppa Pig")

pessoa1.identificar()
crianca1.identificar()