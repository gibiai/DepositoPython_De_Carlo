# CLASSE MADRE
class Animale:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def fai_suono(self):
        print(f"{self.nome} fa un suono generico")


#CLASSE FIGLIA - Leone
class Leone(Animale):
    def __init__(self, nome, età, territorio):
        super().__init__(nome, età)
        self.territorio = territorio

    def fai_suono(self):
        print(f"{self.nome} ruggisce!")

    def caccia(self):
        print(f"{self.nome} sta cacciando nel territorio {self.territorio}")


# CLASSE FIGLIA - Giraffa
class Giraffa(Animale):
    def __init__(self, nome, età, altezza):
        super().__init__(nome, età)
        self.altezza = altezza

    def fai_suono(self):
        print(f"{self.nome} grugnisce!")

    def mangia(self):
        print(f"{self.nome} mangia le foglie alte {self.altezza} metri")


# CLASSE FIGLIA - Pinguino
class Pinguino(Animale):
    def __init__(self, nome, età, velocità_nuoto):
        super().__init__(nome, età)
        self.velocità_nuoto = velocità_nuoto

    def fai_suono(self):
        print(f"{self.nome} stride!")

    def nuota(self):
        print(f"{self.nome} nuota a {self.velocita_nuoto} km/h")


# TEST
l = Leone("Simba", 5, "Savana")
l.fai_suono()
l.caccia()

g = Giraffa("Melman", 3, 5.5)
g.fai_suono()
g.mangia()

p = Pinguino("Skipper", 2, 30.0)
p.fai_suono()
p.nuota()