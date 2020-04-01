"""
arena.py
"""

class Kostka:
    """
    Trida reprezentuje hraci kostku
    """

    def __init__(self):
        self.pocet_sten = 6     # takto je atribut veřejný a lze jej měnit zvenku třídy
                                # např. kostka.pocet_sten = 12


kostka = Kostka()
print(kostka.pocet_sten)
steny = input("zadej počet stěn: ")
kostka.pocet_sten = steny
print(kostka.pocet_sten)