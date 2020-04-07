"""
vlastnosti.py
příklady třídy a vlastnosti třídy
init verze s veřejně dostupnými atributy 
z vnějšku třídy lze atribut změnit a způsobit tak nekonzistenci
"""
class Student:
    def __init__(self, jmeno, muz, vek):
        self.jmeno = jmeno                  # veřejně přístupné atributy
        self.muz = muz
        self.vek = vek
        self.plnolety = (vek > 18)      # vlastnost?

    def __str__(self):
        jsem_plnolety = "jsem" if self.plnolety else "nejsem"       # to je hezká zkratka s if
        muz = "muž" if self.muz else "žena"
        privlastek = "plnoletý" if self.muz else "plnoletá"
        return (f"Jsem {self.jmeno}, {muz}. Je mi {self.vek} let a {jsem_plnolety} {privlastek}. ")

s = Student("Jiří Hora", True, 29)
print(s)
s.vek = 15                  # veřejně přístupné atributy můžeme zvenku měnit a způsobit nekonzistenci
s.muz = False
print(s)
s2 = Student("Jiřina Nová Hora", False, 15)
print(s2)