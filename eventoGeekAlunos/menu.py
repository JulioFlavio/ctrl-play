import cadastrar as cad
import atividades as ativ

print("==================\n    EVENTO GEEK\n==================\n\n1 - Cadastrar participantes\n2 - Ver participantes\n3 - Registrar atividade\n4 - Comprar produtos\n5 - Ver pontuações\n6 - Relatório final\n0 - Encerrar programa")

acao = int(input("Oque deseja fazer?"))
participantes = []

if acao == 0:
    print("Adeus")
if acao == 1:
    participantes = cad.cadastro()
    acao = int(input("Oque deseja fazer?"))
if acao == 2:
    cad.olhar_pessoas(participantes)
    acao = int(input("Oque deseja fazer?"))
if acao == 3:
    ativ.atividades()
    acao = int(input("Oque deseja fazer?"))
