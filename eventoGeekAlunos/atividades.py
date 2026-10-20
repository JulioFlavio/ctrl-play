def atividades():
    print("Atividades disponíveis:\n================\n1 - Quiz de Programação\n================\n2 - Campeonato de Mario Kart\n================\n3 - Desafio de Minecraft\n================\n4 - Torneio de Pokémon\n================\n5 - Competição de Just Dance\n================\nCaso o participante nao queira nada, apenas deixe em branco")

    p1 = input("Qual atividade o participante 1 quer fazer?")
    p2 = input("Qual atividade o participante 2 quer fazer?")
    p3 = input("Qual atividade o participante 3 quer fazer?")
    p4 = input("Qual atividade o participante 4 quer fazer?")
    p5 = input("Qual atividade o participante 5 quer fazer?")

    pp1 = int(input("Qual a pontuacao do participante 1?"))
    pp2 = int(input("Qual a pontuacao do participante 2?"))
    pp3 = int(input("Qual a pontuacao do participante 3?"))
    pp4 = int(input("Qual a pontuacao do participante 4?"))
    pp5 = int(input("Qual a pontuacao do participante 5?"))

    if p1 == "":
        p1 = "nada"
    if p2 == "":
        p2 = "nada"
    if p3 == "":
        p3 = "nada"
    if p4 == "":
        p4 = "nada"
    if p5 == "":
        p5 = "nada"

    print(f"O participante um jogou {p1}\nO participante um fez {pp1} pontos\n=====================\nO participante dois jogou {p2}\nO participante dois fez {pp2} pontos\n=====================\nO participante tres jogou {p3}\nO participante tres fez {pp3} pontos\n=====================\nO participante quatro jogou {p4}\nO participante quatro fez {pp4} pontos\n=====================\nO participante cinco jogou {p5}\nO participante cinco fez {pp5} pontos\n=====================")

