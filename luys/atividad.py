class personagem():
    nome = ""
    vida = ""
    nivel = ""

    def __init__(self, nome, vida, nivel):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel

    def identificar(self):
        print("Nome: ", self.nome)
        print("Vida: ", self.vida)
        print("Nivel: ", self.nivel)


class guerreiro(personagem):
    arma = ""
    ataque = ""

    def __init__(self, nome, vida, nivel, arma, ataque):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel
        self.arma = arma
        self.ataque = ataque

    def identidicar(self):
        print("Nome: ", self.nome)
        print("Vida: ", self.vida)
        print("Nivel: ", self.nivel)
        print("Arma: ", self.arma)
        print("Ataque do gurreiro realizado: ", self.ataque)


class arqueiro(personagem):
    arma = ""
    ataque = ""

    def __init__(self, nome, vida, nivel, arma, ataque):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel
        self.arma = arma
        self.ataque = ataque
    
    def identidicar(self):
        print("Nome: ", self.nome)
        print("Vida: ", self.vida)
        print("Nivel: ", self.nivel)
        print("Arma: ", self.arma)
        print("Ataque do arqueiro realizado: ", self.ataque)

class mago(personagem):
    arma = ""
    ataque = ""
    mana = 0


    def __init__(self, nome, vida, nivel, arma, ataque, mana):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel
        self.arma = arma
        self.ataque = ataque
        self.mana = mana 

        
    def identidicar(self):
        print("Nome: ", self.nome)
        print("Vida: ", self.vida)
        print("Nivel: ", self.nivel)
        print("Arma: ", self.arma)
        print("Ataque do mago realizado: ", self.ataque)
        print("Mana do mago", self.mana)

    if mana <= 10:
        print("ataque forte")
    else:
        print("fraco")

guerreiro1 = guerreiro("lud", 15, 5, "espada", "ataque a um monstro taltaltal")
guerreiro1.identidicar()

arqueiro1 = arqueiro("legolas", 50, 10, "arco flamejante", "acabou brutalmente com uma tropa de 50 soldados")
arqueiro1.identidicar()

mago1 = mago("gandalf", 200, 500, "cajado da luz", "derrotou uma nacao inteira", 1000)
mago1.identidicar()