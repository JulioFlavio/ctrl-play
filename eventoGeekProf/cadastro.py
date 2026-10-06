def cadastrar(numero_participante):
    print("====================")
    print("ATENÇÃO, para CEP, telefone e altura digite apenas números")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    cep = input("Digite seu CEP: ")
    telefone = int(input("Digite seu telefone: "))
    altura = int(input("Digite sua altura: "))
    print("====================")
    return [numero_participante, nome, email, cep, telefone, altura]

def exibir_participantes(participantes):
    print("========== PARTICIPANTES CADASTRADOS ==========")
    for i in participantes:
        print("==============================")
        print("Número: ", i[0])
        print("Nome: ", i[1])
        print("Email: ", i[2])
        print("CEP: ", i[3])
        print("Telefone: ", i[4])
        print("Altura: ", i[5])
    print("==============================")