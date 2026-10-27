class AnimalSelvagem():
    
    def mover(self):
        print("estou correndo")
        
    def come(self):
        print("comendo")
        
class AnimalDomestico():
    def mover():
        print("estou andando")
        
    def getDono(self):
        return self.dono
        
class Cachorro(AnimalSelvagem, AnimalDomestico):
    def __init__(self, dono):
        self.dono = dono
        
    def late(self):
        print("Auau!")

c = Cachorro("Luis")

print(c.getDono())
c.come()
c.late()
c.mover()