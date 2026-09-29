def cadastrar():
    print("ATENÇÃO, para CEP, telefone e altura digite apenas números")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    cep = input("Digite seu CEP: ")
    telefone = int(input("Digite seu telefone: "))
    altura = int(input("Digite sua altura: "))
    return [nome, email, cep, telefone, altura]

def exibir_participantes(participantes):
    print("========== PARTICIPANTES CADASTRADOS ==========")
    for i in participantes:
        print("==============================")
        print("Nome: ", i[0])
        print("Email: ", i[1])
        print("CEP: ", i[2])
        print("Telefone: ", i[3])
        print("Altura: ", i[4])
    print("==============================")