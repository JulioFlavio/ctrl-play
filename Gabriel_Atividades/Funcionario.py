class Funcionario():
    nome = ""
    idade = 0
    identificacao = ""
    salario = 0.0

    def __init__(self, nome, idade, identificacao, salario):
        self.nome = nome
        self.idade = idade
        self.identificacao = identificacao
        self.salario = salario
    
    def ExibirFuncionario(self):
        print("Nome: ", self.nome, "\nIdade: ", self.idade, "\nIdentificaçao: ", self.identificacao, "\nSalario: ", self.salario)

funcionario1 = Funcionario("Carlos", 21, "Carlão", 1618)
funcionario1.ExibirFuncionario()

class Estagiario(Funcionario):
    horasTrabalhadas = 0
    horaExtra = 0


    def __init__(self, nome, idade, identificacao, salario, horaExtra, horasTrabalhadas):
        self.nome = nome
        self.idade = idade
        self.identificacao = identificacao
        self.salario = salario
        self.horaExtra = horaExtra
        self.horasTrabalhadas = horasTrabalhadas

    def exibirEstagiario(self):
        print("Nome: ", self.nome, "\nIdade: ", self.idade, "\nIdentificaçao: ", self.identificacao, "\nSalario: ", self.salario, "\nHoras Trabalhadas: ", self.horasTrabalhadas, "\nHora Extra: ", self.horaExtra, " horas")

estagiario1 = Estagiario("Joao", 19, "Jozin", 12, 2, 9)
estagiario1.exibirEstagiario()