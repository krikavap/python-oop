"""
vlastnosti.py
příklady třídy a vlastnosti třídy
třetí verze s privátními atributy třídy a s vlastnostmi @property a novým setterem @vek.setter
podobně lze vytvořit i getter @vek.getter , který např. zajistí nějakou další logiku (zalogování přístupu k údaji apod.)
"""
class Student:
    def __init__(self, jmeno, muz, vek):
        self.__jmeno = jmeno                  # privátní atributy
        self.__muz = muz
        self.__vek = vek
        self.__plnolety = (vek >= 18)      

    def __str__(self):
        jsem_plnolety = "jsem" if self.__plnolety else "nejsem"       # to je hezká zkratka s if
        muz = "muž" if self.__muz else "žena"
        privlastek = "plnoletý" if self.__muz else "plnoletá"
        return (f"Jsem {self.__jmeno}, {muz}. Je mi {self.__vek} let a {jsem_plnolety} {privlastek}. ")

    def vrat_jmeno(self):               # metoda vracející hodnotu atributu, tzv. getter
        return self.__jmeno

    @property                           # to samé jako getter, ale pomocí property - nastavení vlastnosti (@property = dekonátor)
    def jmeno(self):
        return self.__jmeno             # atribut svázaný s metodou

    def vrat_plnoletost(self):          # getter
        return self.__plnolety

    def vrat_vek(self):                 # getter
        return self.__vek

    def vrat_muz(self):                 # getter
        return self.__muz

    def nastav_muz(self, muz):          # setter
        self.__muz = muz

    # metoda ošetří i případ, že věk < 18 a je nutné změnit i atribut plnoletost
    def nastav_vek(self, vek):      # metoda měnící atribut tzv. setter
        self.__vek = vek
        if vek < 18:
            self.__plnolety = False
        else:
            self.__plnolety = True

    @property                           # dekonátor property
    def vek(self):
        return self.__vek

    @vek.setter                         # dekonátor setter - mění vlastnost, může obsahovat i logiku (zde test plnoletosti)
    def vek(self, hodnota):
        self.__vek = hodnota
        self.__plnolety = (hodnota >= 18)

    
s = Student("Jiří Hora", True, 29)
print(s)
s.vek = 15                  # pomocí setteru vlastnosti vek lze private atribut vek zvenku řízeně změnit 
s.muz = False               # privátní atribut není možné bez setteru změnit
print(s)                    
s.nastav_vek(12)            # změna pomocí původního setteru nastav_vek()
print(s)                    # výstup se správně změněnými atributy

print(s.jmeno)              # vytvořením property lze vypsat privat jmeno
print(s.vek)                # vytvořením property lze vypsat privat vek

s2 = Student("Jiřina Nová Hora", False, 15)
print(s2)
