"""
arena.py
"""

class Kostka:
    """
    Trida reprezentuje hraci kostku
    """

    def __init__(self):
        """
        iniciacni metoda
        """
        #self.pocet_sten = 6     # takto je atribut veřejný a lze jej měnit zvenku třídy
                                # např. kostka.pocet_sten = 12
        self.__pocet_sten = 6   # dvojité podtržítko před názvem udělá z atributu atribut neveřejný 


    def vrat_pocet_sten(self):
        """
        vrati pocet sten kostky 
        """
        return self.__pocet_sten


kostka = Kostka()
print(kostka.vrat_pocet_sten())

steny = int(input("zadej počet stěn: "))
kostka.__pocet_sten = steny
print(kostka.__pocet_sten)
print(kostka.vrat_pocet_sten())