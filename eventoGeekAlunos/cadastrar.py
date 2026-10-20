def cadastro():
    nome1 = input("Qual é o nome do primeiro participante?")
    email1 = input("\n==============\nQual é o email do primeiro participante?")
    cep1 = int(input("\n===============\nQual e o cep do primeiro participante?"))
    telefone1 = int(input("\n==============\nQual e o telefone do primeiro participante?"))
    altura1 = float(input("\n==============\nQual é a altura do primeiro participante?"))

    nome2 = input("Qual é o nome do segundo participante?")
    email2 = input("\n==============\nQual é o email do segundo participante?")
    cep2 = int(input("\n===============\nQual e o cep do segundo participante?"))
    telefone2 = int(input("\n==============\nQual e o telefone do segundo participante?"))
    altura2 = float(input("\n==============\nQual é a altura do segundo participante?"))

    nome3 = input("Qual é o nome do terceiro participante?")
    email3 = input("\n==============\nQual é o email do terceiro participante?")
    cep3 = int(input("\n===============\nQual e o cep do terceiro participante?"))
    telefone3 = int(input("\n==============\nQual e o telefone do terceiro participante?"))
    altura3 = float(input("\n==============\nQual é a altura do terceiro participante?"))

    nome4 = input("Qual é o nome do quarto participante?")
    email4 = input("\n==============\nQual é o email do quarto participante?")
    cep4 = int(input("\n===============\nQual e o cep do quarto participante?"))
    telefone4 = int(input("\n==============\nQual e o telefone do quarto participante?"))
    altura4 = float(input("\n==============\nQual é a altura do quarto participante?"))

    nome5 = input("Qual é o nome do quinto participante?")
    email5 = input("\n==============\nQual é o email do quinto participante?")
    cep5 = int(input("\n===============\nQual e o cep do quinto participante?"))
    telefone5 = int(input("\n==============\nQual e o telefone do quinto participante?"))
    altura5 = float(input("\n==============\nQual é a altura do quinto participante?"))

    return [nome1, email1, cep1, telefone1, altura1], [nome2, email2, cep2, telefone2, altura2], [nome3, email3, cep3, telefone3, altura3], [nome4, email4, cep4, telefone4, altura4], [nome5, email5, cep5, telefone5, altura5]

def olhar_pessoas(participantes):
    for pessoa in participantes:
        print("Nome: ", pessoa[0])
        print("Email: ", pessoa[1])
        print("CEP: ", pessoa[2])
        print("Telefone: ", pessoa[3])
        print("Altura: ", pessoa[4])
        print("==============================")
        

    

