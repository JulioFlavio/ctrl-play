import cadastro as cad

participantes = []
print("============= EVENTO GEEK ==============")
print("Seja bem vindo ao Evento Geek 2026.\nVamos começar cadastrando os 5 participantes!\n\n")

for i in range(1, 6):
    participante = cad.cadastrar()
    participantes.append(participante)

print(cad.exibir_participantes(participantes))