"""
arena.py
"""

class Kostka:
    """
    Trida reprezentuje hraci kostku
    """
    def __init__(self, pocet_sten = 6):     # nová definice, přidání argumentu pocet_sten, výchozí hodnota je 6
    #def __init__(self):    # původní definice
        """
        iniciacni metoda
        argument pocet_sten určuje, kolik stěn bude objekt mít
        """
        #self.pocet_sten = 6     # takto je atribut veřejný a lze jej měnit zvenku třídy
                                # např. kostka.pocet_sten = 12
        #self.__pocet_sten = 6   # dvojité podtržítko před názvem udělá z atributu atribut vnitřní 
        self.__pocet_sten = pocet_sten


    def __str__(self):
        """
        vraci textovou reprezentaci kostky - prevadi objekt na retezec
        """
        text = str(f"Kostka s {self.__pocet_sten} stěnami")
        return text


    def vrat_pocet_sten(self):
        """
        vrati pocet sten kostky 
        """
        return self.__pocet_sten


    def hod(self):
        """
        vykona hod kostkou a vrati nahodne cislo od 1 do poctu sten
        """
        import random as _random    # import modulu random jako vnitřního modulu metody hod (s jedním podtržítkem před názvem)
        cislo = _random.randint(1, self.__pocet_sten)       # generuje náhodné číslo 1 - pocet_sten
        return cislo

    def __repr__(self):
        """
        vraci v retezci kod konstruktoru pro funkci eval()
        """
        text = str("Kostka("+str(self.__pocet_sten)+")")
        return text

# vytvoření kostek
sestistena = Kostka()   # původní definice s prázdným konstruktorem
steny = int(input("zadej počet stěn: "))
kostka = Kostka(steny)      # nová definice instance, kdy určíme počet stěn nového objektu

# hod šestistěnnou
print(sestistena)
for _ in range(10):
    print(sestistena.hod(), end=" ")
print()

# hod vícestěnnou
print(kostka)
for _ in range(10):
    print(kostka.hod(), end=" ")

jina_sestistena = eval(repr(sestistena))    # duplikuje objekt
print()
print(jina_sestistena)