"""
desitkovaDvojkovaOOP.py

"""

class Prevod:
    """
    převádí číslo z desítkové na dvojkovou soustavu a opačně
    dvojkova_desitkova
    """
    def dvojkova_desitkova(self, dvojkove):
        """
        metoda převádí dvojkové číslo na desítkovou soustavu
        parametr metody je čislo (int) ve dvojkové soustavě
        vrací číslo v desítkové soustavě 
        """
        cislo = 0
        seznam = list(dvojkove)
        zacatek = 0
        konec = len (seznam)

        for i in range(zacatek, konec):
            cislo = cislo + int(seznam[i])*2**(konec - i - 1)
        return cislo


    def desitkova_dvojkova(self, cislo):
        """
        metoda převádí číslo v desítkové soustavě na číslo ve dvojkové soustavě
        parametr metody je čislo (int) ve desítkové soustavě
        vrací číslo v dvojkové soustavě
        """
        x = cislo
        seznam = []
        while x != 0:
            zbytek = x % 2
            seznam.append(zbytek)
            x = x // 2

        zacatek = 0
        konec = len(seznam)
        vysledek = []
        dvojkove = ""

        for i in range (konec-1, zacatek-1, -1):
            vysledek.append(str(seznam[i]))

        dvojkove = "".join(vysledek)
        dvojkove = "0" * (8 - len(dvojkove)) + dvojkove

        return dvojkove

# instance třídy Převod
prevod = Prevod()

# převod desítková na dvojkovou
cislo = int(input("Zadej celé číslo v desítkové soustavě: "))
dvoj = prevod.desitkova_dvojkova(cislo)
print()
print(f"{cislo} v desítkové soustavě je {dvoj} ve dvojkové soustavě")

#a opačně dvojková na desítkovou
dvoj = str(input("Zadej celé číslo ve dvojkové soustavě: "))
cislo = prevod.dvojkova_desitkova(dvoj)
print()
print(f"{dvoj} ve dvojkové soustavě je {cislo} v desítkové soustavě")

