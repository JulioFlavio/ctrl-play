import cadastro as cad
import atividades

participantes = []
def exibirMenu():
    print("==================\n    EVENTO GEEK\n==================" \
    "\n\n1 - Cadastrar participantes" \
    "\n2 - Ver participantes" \
    "\n3 - Registrar atividade" \
    "\n4 - Comprar produtos" \
    "\n5 - Ver pontuações" \
    "\n6 - Relatório final" \
    "\n0 - Encerrar programa")

    return int(input("Oque deseja fazer? "))

def escolherOpcao(resposta):
    if resposta == 1:
        qtdParticipantes = int(input("Quantos participantes deseja cadastrar? "))

        for participante in range(qtdParticipantes):
            participantes.append(cad.cadastrar(participante + 1))
            print(f"Participante {participante + 1} cadastrado com sucesso!")

        exibirMenuNovamente = input("Todos os participantes foram cadastrados com sucesso! Exibir o menu novamente para escolher outra opção? (S/N)").lower()
        
        if exibirMenuNovamente == "s":
            exibirMenu()
        else:
            print("Programa encerrado.")
        print("===============================================")


    elif resposta == 2:
        cad.exibir_participantes()


    elif resposta == 3:
        atividades.registrar_atividade()


    elif resposta == 4:
        cad.comprar_produtos()


    elif resposta == 5:
        cad.ver_pontuacoes()


    elif resposta == 6:
        cad.relatorio_final()


    elif resposta == 0:
        print("Programa encerrado.")
    else:
        print("Opção inválida. Tente novamente.")
        exibirMenu()