import random

class RPG():
    nome = ""
    vida = 0
    nivel = 1

    def __init__(self, nome, vida, nivel):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel
    
    def getNome(self):
        return self.nome

    def mostrarJogador(self):
        print(str(self.nome), int(self.vida), int(self.nivel))

class mago(RPG):
    mana = 0
    
    def carregarMana(self):
        self.mana += 10
    
    def usarMagia(self):
        if self.mana >= 20:
            print("Derrotou inimigo")
        else: print("Virou sapo")


mago1 = mago("joao", 10, 2)
mago1.mostrarJogador()
mago1.carregarMana()
mago1.carregarMana()
mago1.usarMagia()

class guerreiro(RPG):
    armas = []

    def __init__(self, armas, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self.armas = armas

    def lutar(self):
        if "Espada" or "espada" or "Escudo" or "escudo" in self.armas:
            print("Voce venceu")
        else: print("Perdeu")
    
    def mostrarGuerreiro(self):
        print(self.armas, str(self.nome), int(self.vida), int(self.nivel))
    

soldado = guerreiro(["Espada", "arco", "poçao"], "Carlao", 50, 4)
soldado.mostrarGuerreiro()
soldado.lutar()

class arqueiro(RPG):
    mira = 0

    def __init__(self, mira, nome, vida, nivel):
        super().__init__(nome, vida, nivel)
        self.mira = mira

    def testarMira(self):
        print(f"Voce acertou {random.randint(self.mira, (self.mira * 2))} flechas no alvo!")
    
    def mostrarArqueiro(self):
        print(self.mira, self.nome, self.vida, self.nivel)

arqueiro = arqueiro(10, "Claudio", 40, 6)
arqueiro.mostrarArqueiro()
arqueiro.testarMira()
