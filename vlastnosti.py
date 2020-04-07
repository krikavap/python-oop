"""
vlastnosti.py
příklady třídy a vlastnosti třídy
druhá verze s privátními atributy třídy a s metodami, kterými lze atributy zvenku číst (gettery) a měnit (settery)
"""
class Student:
    def __init__(self, jmeno, muz, vek):
        """
        self.jmeno = jmeno                  # veřejně přístupné atributy
        self.muz = muz
        self.vek = vek
        self.plnolety = (vek > 18)      # vlastnost?
        """
        self.__jmeno = jmeno                  # privátní atributy
        self.__muz = muz
        self.__vek = vek
        self.__plnolety = (vek > 18)      

    def __str__(self):
        jsem_plnolety = "jsem" if self.__plnolety else "nejsem"       # to je hezká zkratka s if
        muz = "muž" if self.__muz else "žena"
        privlastek = "plnoletý" if self.__muz else "plnoletá"
        return (f"Jsem {self.__jmeno}, {muz}. Je mi {self.__vek} let a {jsem_plnolety} {privlastek}. ")

    def vrat_jmeno(self):               # metoda vracející hodnotu atributu, tzv. getter
        return self.__jmeno

    def vrat_plnoletost(self):
        return self.__plnolety

    def vrat_vek(self):
        return self.__vek

    def vrat_muz(self):
        return self.__muz

    # metoda ošetří i případ, že věk < 18 a je nutné změnit i atribut plnoletost
    def nastav_vek(self, vek):      # metoda měnící atribut tzv. setter
        self.__vek = vek
        if vek < 18:
            self.__plnolety = False
        else:
            self.__plnolety = True

    def nastav_muz(self, muz):
        self.__muz = muz

    
s = Student("Jiří Hora", True, 29)
print(s)
s.vek = 15                  # public atributy nelze zvenku měnit a způsobit nekonzistenci. 
s.muz = False               
print(s)                # výstup stejný jako první, i když jsme chtěli argumenty změnit
s.nastav_vek(12)
s.nastav_muz(False)
print(s)                # výstup se správně změněnými atributy

s2 = Student("Jiřina Nová Hora", False, 15)
print(s2)
