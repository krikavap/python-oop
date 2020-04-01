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
        #self.__pocet_sten = 6   # dvojité podtržítko před názvem udělá z atributu atribut neveřejný 
        self.__pocet_sten = pocet_sten


    def vrat_pocet_sten(self):
        """
        vrati pocet sten kostky 
        """
        return self.__pocet_sten


sestistena = Kostka()   # původní definice s prázdným konstruktorem
print(sestistena.vrat_pocet_sten())

steny = int(input("zadej počet stěn: "))
kostka = Kostka(steny)      # nová definice instance, kdy určíme počet stěn nového objektu
print(kostka.vrat_pocet_sten())
