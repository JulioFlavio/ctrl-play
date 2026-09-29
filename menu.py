import cadastrar as cad

print("==================\n    EVENTO GEEK\n==================\n\n1 - Cadastrar participantes\n2 - Ver participantes\n3 - Registrar atividade\n4 - Comprar produtos\n5 - Ver pontuações\n6 - Relatório final\n0 - Encerrar programa")

acao = input("Oque deseja fazer?")

if acao == 1:
    cad.cadastro()