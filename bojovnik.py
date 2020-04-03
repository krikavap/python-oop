"""
bojovnik.py
trida bojovnik a hratky s ni
"""

class Bojovnik:
    """
    Trida reprezentuji bojovnika do areny
    """
    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        """
        jmeno - jmeno bojovnika
        zivot - maximalni zivot bojovnika
        utok - utok bojovnika
        obrana - obrana bojovnika
        kostka - instance kostky
        """
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__max_zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka

    def __str__(self):
        """
        vrati jmeno bojovnika
        """
        return str(self.__jmeno)

    
    def __repr__(self):
        """
        vraci v retezci kod konstruktoru pro funkci eval(), tj vytvoreni kopie bojovnika
        """
        text = str("Bojovnik(\""+self.__jmeno+"\","+str(self.__max_zivot)+","+str(self.__utok)+","+str(self.__obrana)+",\""+(self.__kostka)+"\")")
        return text

    
    @property               # dekorátor = mění metodu na vlastnost /atribut
    def nazivu(self):
        """
        test, zda je bojovnik nazivu, tzn. zda jeho aktualni zivot je > 0
        """
        if self.__zivot > 0:
            return True
        else:
            return False

    def graficky_zivot(self):
        """
        graficky vyjadri mnozstvi zbyvajiciho zivota bojovnika
        """
        celkem = 20     # max. pocet znaku pro delku zivota 
        #self.__zivot = 50
        pocet = int(self.__zivot/self.__max_zivot * celkem)     # delka zivota
        if (pocet == 0 and self.nazivu):                        # pokud je hodnota života malá, ale bojovník je naživu, dáme pocet = 1
            pocet = 1
        return (("#" * pocet) + (" " * (celkem - pocet) ))           # vrátí počet křížků dle aktuálního života bojovníka
            

bojovnik1 = Bojovnik("Pepa", 90, 20, 10, "kostka")
print(bojovnik1)


novy_boj = eval(repr(bojovnik1))
print()
print(novy_boj)

print(bojovnik1.graficky_zivot())