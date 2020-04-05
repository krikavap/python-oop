"""
arena.py
hra - souboj dvou bojovniku v arene
konzolova aplikace
podle tutorialu https://www.itnetwork.cz/python/oop

"""

class Arena:
    """
    trida ridici prubeh celeho zapasu
    """
    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        """
        iniciace Arena
        """
        self.__bojovnik_1 = bojovnik_1
        self.__bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def __vykresli(self):
        """
        vykresli uvodni obrazovku s prehledem bojovniku 
        jejich vlastnosti a aktualniho stavu 
        - nazivu True/False pomoci metody nazivu
        - poctu zbyvajicich zivotu (vrat_zivot())
        a grafickeho vyjadreni zbyvajiciho zivota (graficky_zivot())
        """            
        print("-" * 15, " Aréna ", "-" * 15,"\n")
        print("Bojovníci: \n")
        self.__vypis_bojovnika(self.__bojovnik_1)
        self.__vypis_bojovnika(self.__bojovnik_2)
       
    def __vypis_bojovnika(self, bojovnik):
        """
        vypise status bojovnika dle argumentu vc. grafickeho znazorneni zbyvajiciho zivota
        pokud bojovnik je Mag, pak vypise i stav many vc. grafiky
        """
        print(bojovnik)
        print(f"Naživu:     {bojovnik.nazivu}")
        print(f"Život:  {bojovnik.vrat_zivot():>5} hp       {bojovnik.graficky_zivot()} ")
        if isinstance(bojovnik, Mag):
            print(f"Mana:   {bojovnik.vrat_mana():>5} hp       {bojovnik.graficka_mana()} ")
        print()

    def __vycisti_obrazovku(self):
        """
        smaze obrazovku, a to prikazem pouzivaneho operacniho systemu
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
        # vypsání úvodní obrazovky
        self.__vycisti_obrazovku()
        print("-" * 15, " Aréna ", "-" * 15,"\n")
        print("Vítejte v aréně. Dnes se utkají bojovníci: ")
        print()
        print(f"{self.__bojovnik_1} \n{self.__bojovnik_2} ")
        print()
        print("Zápas může začít...", end=" ")
        input()

        # prohození bojovníků - pokud padne na kostce sudá, první útočí bojovnik_1
        # pokud lichá, první útočí bojovník_2
        zbytek = self._kostka.hod() % 2 
        if zbytek > 0:
            (self.__bojovnik_1, self.__bojovnik_2) = (self.__bojovnik_2, self.__bojovnik_1)

        # cyklus s bojem
        while (self.__bojovnik_1.nazivu and self.__bojovnik_2.nazivu):
            self.__vycisti_obrazovku()
            self.__bojovnik_1.utoc(self.__bojovnik_2)
            self.__vypis_zpravu(self.__bojovnik_1.vrat_posledni_zpravu())
            self.__vypis_zpravu(self.__bojovnik_2.vrat_posledni_zpravu())
            self.__vykresli()
            input()
            if self.__bojovnik_2.nazivu:        # testování zamezí tomu, aby útočil mrtvý bojovník
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
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self.__zprava = ""

    def __str__(self):
        """
        vrati jmeno bojovnika
        """
        return (str(self._jmeno) + ", životů: " + str(self._max_zivot) + " hp, útok: " + str(self._utok) + " hp, obrana: " + str(self._obrana) + " hp")

    
    def __repr__(self):
        """
        vraci v retezci kod konstruktoru pro funkci eval(), tj vytvoreni kopie bojovnika
        """
        text = str("Bojovnik(\""+self._jmeno+"\","+str(self._max_zivot)+","+str(self._utok)+","+str(self._obrana)+",\""+(self._kostka)+"\")")
        return text

    @property               # dekorátor = mění metodu na vlastnost /atribut
    def nazivu(self):
        """
        test, zda je bojovnik nazivu, tzn. zda jeho aktualni zivot je > 0
        """
        if self._zivot > 0:
            return True
        else:
            return False

    def graficky_ukazatel(self, aktualni, maximalni):
        """
        graficky vyjadri mnozstvi zbyvajiciho ukazatele
        """
        celkem = 20     # max. pocet znaku pro delku ukazatele 
        pocet = int(aktualni/maximalni * celkem)     # delka ukazatele
        if (pocet == 0 and self.nazivu):                        # pokud je hodnota ukazatele malá, ale bojovník je naživu, dáme pocet = 1
            pocet = 1
        return (("["+"#" * pocet) + (" " * (celkem - pocet)+"]" ))           # vrátí počet křížků dle aktuální hodnoty ukazatele
            
    def graficky_zivot(self):
        """
        metoda vola graficky ukazatel pro vykresleni zivota
        """
        return self.graficky_ukazatel(self._zivot, self._max_zivot)
        
    def vrat_zivot(self):
        """
        vrati aktualni pocet jednotek zivota bojovnika
        """
        return self._zivot

    def bran_se(self, uder):
        """
        metoda vypocte velikost zbyvajiciho zivota po utoku
        pokud je zraneni vetsi nez zbyvajici zivot, vrati zivot = 0
        """
        zraneni = uder - (self._obrana + self._kostka.hod())       # výpočet zranění

        if zraneni > 0:         # pokud je útok silnější než naše obrana, jsme zranění. Pokud je obrana stejná nebo silnější než útok, na zbývajícím životě se nic nemění
            zprava = (f"{self._jmeno} utrpěl poškození {zraneni} hp")          # sestavení zprávy pro konzoli
            self._zivot = self._zivot - zraneni       # výpočet zbývajícího života
        
            if self._zivot <= 0:
                self._zivot = 0        
                zprava = zprava + " a zemřel"        # doplnění zprávy
        else:
            zprava = (f"{self._jmeno} odrazil útok ")      # pokud odražení útoku bylo úspěšné a bez zranění
        
        self._nastav_zpravu(zprava)        # vepíše zprávu do vlastnosti
        
    def utoc(self, souper):
        """
        vypocita silu uderu a zautoci
        argument souper je instance bojovnika, na ktereho se utoci
        """
        uder = self._utok + self._kostka.hod()
        
        zprava = (f"{self._jmeno} útočí s úderem za {uder} hp ") # sestavení zprávy pro konzoli
        self._nastav_zpravu(zprava)
        
        souper.bran_se(uder)        

    def _nastav_zpravu(self, zprava):
        """
        privatni metoda nastavujici zpravu
        argument je textovy retezec, ktery ma byt vlozen do vlastnosti self.__zprava
        """
        self.__zprava = zprava   

    def vrat_posledni_zpravu(self):
        """
        metoda vrati posledni zpravu
        """
        return self.__zprava
        
class Mag(Bojovnik):
    """
    trida Mag je subtridou Bojovnika
    navic má mana - pokud má tuto magickou sílu plnou, může vykonat magický útok
    po každém magickém útoku mana = 0 a po každém kole souboje se zvýší o 10
    jakmile se doplní, znovu ji použije
    """
    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        """
        init funkce - prebíra init z Bojovnika a pridava dalsi argumenty
        """
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self.__mana = mana
        self.__max_mana = mana
        self.__magicky_utok = magicky_utok
        self.__zprava = ""

    def __str__(self):
        """
        vrati jmeno bojovnika - maga - oproti metode v supertride vypise i atributy max_mana a magicky_utok
        """
        return (str(self._jmeno) + ", životů: " + str(self._max_zivot) + " hp, útok: " + str(self._utok) + " hp, obrana: " + str(self._obrana)
         + " hp, mana: " + str(self.__max_mana) + " hp, magický útok: " + str(self.__magicky_utok) + " hp")

    def utoc(self, souper):
        """
        upravena metoda ze supertřídy. overi, zda mana je max
        pokud ano, tak magicky uder
        pokud ne, tak vypocita silu uderu a zautoci stejne jako v class Bojovnik
        argument souper je instance bojovnika, na ktereho se utoci      
        """    
        # mana není naplněna
        if self.__mana < self.__max_mana:
            self.__mana = self.__mana + 10      # zvýší o 10
            if self.__mana > self.__max_mana:   # pokud ale je pak větší než max, tak přiřadí max
                self.__mana = self.__max_mana
            # a dále již pokračování stejné jako u bojovníka
            super().utoc(souper)
        # magický útok
        else:
            uder = self.__magicky_utok + self._kostka.hod()      
            zprava = (f"{self._jmeno} použil magii za {uder} hp ") # sestavení zprávy pro konzoli
            self._nastav_zpravu(zprava)
            self.__mana = 1
            souper.bran_se(uder)  

    def graficka_mana(self):
        """
        vola metodu graficky_ukazatel() pro vykresleni many
        """
        return self.graficky_ukazatel(self.__mana, self.__max_mana)

    def vrat_mana(self):
        """
        vraci aktualni velikost many
        """
        return self.__mana

kostka = Kostka(10)         # vytvoření objektu kostka

# vytvoření bojovníků a arény
zalrogen = Bojovnik("ZALGOREN", 100, 20, 10, kostka)        
gandalf = Mag("GANDALF", 60, 15, 12, kostka, 30, 45)
arena = Arena(zalrogen, gandalf, kostka)

# zápas
arena.zapas()
