# Criando a classe Animal - Super-Classe
class Animal():
    def __init__(self):
        print('animal criado')

    def Identif(self):
        print("Animal")

    def comer(self):
        print("Comendo")


# Criando a classe Cachorro - Sub-Classe
class Cachorro(Animal):
    def latir(self):
        print("latir")


a = Animal()
a.comer()

c = Cachorro()
c.comer()
c.latir()
