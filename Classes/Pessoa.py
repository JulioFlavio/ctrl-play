class Pessoa():
    nome = ""
    idade = 0
    altura = 0
    cor = ""

    def __init__(self, nome, idade, altura, cor):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cor = cor

    def identificar(self):
        print("================")
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Altura: ", self.altura)
        print("Cor: ", self.cor)
        print("=================")

    # pessoa1 = Pessoa("Júlio", 22, 210, "Branco")
    #Exemplo de criação de objeto (instancia)