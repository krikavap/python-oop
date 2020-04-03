"""
arena.py
"""

class Arena:
    """
    trida ridici prubeh zapasu

    """
    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        """
        
        """
        self.__bojovnik_1 = bojovnik_1
        self.__bojovnik_2 = bojovnik_2
        self.__kostka = kostka


    def __vykresli(self):
        """
        vykresli uvodni obrazovku s prehledem bojovniku a jejich stavu
        """
        #self.__vycisti_obrazovku()
     
        print()
        print("Zdraví bojovníků: \n")
        print(f"Bojovník 1: {self.__bojovnik_1}")
        print(f"Naživu: {self.__bojovnik_1.nazivu}")
        print(f"Život:  {self.__bojovnik_1.vrat_zivot():>5} hp       {self.__bojovnik_1.graficky_zivot()} ")
        print()
        print(f"Bojovník 2: {self.__bojovnik_2}")
        print(f"Naživu: {self.__bojovnik_2.nazivu}")
        print(f"Život:  {self.__bojovnik_2.vrat_zivot():>5} hp       {self.__bojovnik_2.graficky_zivot()} ")
        

    
    def __vycisti_obrazovku(self):
        """
        smaze obrazovku
        """
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):             # test platformy windows
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])


    def __vypis_zpravu(self, zprava):
        """
        vypise zpravu predanou parametrem zprava
        po vypisu zpravy pauza .75 s
        """
        import time as _time
        print(zprava)
        _time.sleep(.75)


    def zapas(self):
        """
        metoda ridici cely zapas
        """

        self.__vycisti_obrazovku()
        print("-" * 15, " Aréna ", "-" * 15,"\n")
        print("Vítejte v aréně")
        print(f"Dnes se utkají bojovníci: ")
        print(f"{self.__bojovnik_1} \n{self.__bojovnik_2} ")
        print()
        print("Zápas může začít...", end=" ")
        input()

        # cyklus s bojem
        while (self.__bojovnik_1.nazivu and self.__bojovnik_2.nazivu):
            self.__vycisti_obrazovku()
            self.__bojovnik_1.utoc(self.__bojovnik_2)
            self.__vypis_zpravu(self.__bojovnik_1.vrat_posledni_zpravu())
            self.__vypis_zpravu(self.__bojovnik_2.vrat_posledni_zpravu())
            self.__vykresli()
            input()

            if self.__bojovnik_2.nazivu:
                self.__vycisti_obrazovku()
                self.__bojovnik_2.utoc(self.__bojovnik_1)
                self.__vypis_zpravu(self.__bojovnik_2.vrat_posledni_zpravu())
                self.__vypis_zpravu(self.__bojovnik_1.vrat_posledni_zpravu())
                self.__vykresli()
                input()

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


class Bojovnik:
    """
    Trida reprezentuje bojovnika do areny
    """
    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        """
        jmeno - jmeno bojovnika
        zivot - maximalni zivot bojovnika
        utok - utok bojovnika
        obrana - obrana bojovnika
        kostka - instance kostky
        
        zprava - zpráva na konzoli
        """
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__max_zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka
        self.__zprava = ""

    def __str__(self):
        """
        vrati jmeno bojovnika
        """
        return (str(self.__jmeno) + ", životů: " + str(self.__max_zivot) + " hp, útok: " + str(self.__utok) + " hp, obrana: " + str(self.__obrana) + " hp")

    
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
        return (("["+"#" * pocet) + (" " * (celkem - pocet)+"]" ))           # vrátí počet křížků dle aktuálního života bojovníka
            

    def vrat_zivot(self):
        """
        vrati aktualni pocet jednotek zivota bojovnika
        """
        return self.__zivot


    def bran_se(self, uder):
        """
        metoda vypocte velikost zbyvajiciho zivota po utoku
        pokud je zraneni vetsi nez zbyvajici zivot, vrati zivot = 0
        """
        zraneni = uder - (self.__obrana + self.__kostka.hod())       # výpočet zranění

        if zraneni > 0:         # pokud je útok silnější než naše obrana, jsme zranění. Pokud je obrana stejná nebo silnější než útok, na zbývajícím životě se nic nemění
            zprava = (f"{self.__jmeno} utrpěl poškození {zraneni} hp")          # sestavení zprávy pro konzoli
            self.__zivot = self.__zivot - zraneni       # výpočet zbývajícího života
        
            if self.__zivot < 0:
                self.__zivot = 0        
                zprava = zprava + "a zemřel"        # doplnění zprávy
        else:
            zprava = (f"{self.__jmeno} odrazil útok ")      # pokud odražení útoku bylo úspěšné a bez zranění
        
        self.__nastav_zpravu(zprava)        # vepíše zprávu do vlastnosti

        
    def utoc(self, souper):
        """
        vypocita silu uderu a zautoci
        argument souper je instance bojovnika, na ktereho se utoci
        """
        uder = self.__utok + self.__kostka.hod()
        
        zprava = (f"{self.__jmeno} útočí s úderem za {uder} hp ") # sestavení zprávy pro konzoli
        self.__nastav_zpravu(zprava)
        
        souper.bran_se(uder)        


    def __nastav_zpravu(self, zprava):
        """
        privatni metoda nastavujici zpravu
        argument je textovy retezec, ktery ma byt vlozen do vlastnosti self.__zprava
        """
        self.__zprava = zprava   

    def vrat_posledni_zpravu(self):
        return self.__zprava
        

kostka = Kostka(10)         # vytvoření objektu kostka

# vytvoření bojovníků a arény
zalrogen = Bojovnik("Zalgoren", 100, 20, 10, kostka)        
shadow = Bojovnik("Shadow", 60, 18, 15, kostka)
arena = Arena(zalrogen, shadow, kostka)

# zápas
arena.zapas()




