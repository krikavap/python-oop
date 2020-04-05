"""
statika.py
soubor na procvičení statických proměnných a metod
"""
class Uzivatel:
    minimalni_delka_hesla = 6           # statická proměnná - existuje ještě před vytvořením instance objektu
    dalši_id = 1                        # další statická proměnná na jedinečné číslo uživatele

    def __init__(self, jmeno, heslo):
        self.jmeno = jmeno
        self.heslo = heslo
        self.prihlaseny = False
        print(Uzivatel.dalši_id)
        self.id = Uzivatel.dalši_id 
        print(self.id)
        Uzivatel.dalši_id = Uzivatel.dalši_id + 1
        print(Uzivatel.dalši_id)
    def prihlas_se(self, zadane_heslo):
        if self.heslo == zadane_heslo:
            self.prihlaseny = True
            return True     # hesla souhlasí
        else:
            self.prihlaseny = False
            return False    # hesla nesouhlasí
    
    def __str__(self):
        return self.jmeno

class Trida:
    # může exisovat i statická metoda např. pro validaci hesla 
    # a klasické funkce v třídě jako statické metody

    @staticmethod
    def zvaliduj_heslo(heslo):
        if len(heslo) < Uzivatel.minimalni_delka_hesla:
            print(f"Heslo musí být dlouhé minimálně {Uzivatel.minimalni_delka_hesla} znaků")
            return False
        else:
            return True

    @staticmethod
    def registrace():
        print("Registrace")
        name = input("Jméno: ")
        passw = input("Heslo: ")
        while Trida.zvaliduj_heslo(passw) == False:          # volá statickou metodu pro validaci hesla
            passw = input("Heslo: ")
        
        xxx = Uzivatel(name, passw)             # založí instanci objektu Uživatel
        return xxx                              # vrátí ukazatel na novou instanci třídy Uživatel

# registrace nového uživatele
novy_uz = Trida.registrace()
print(novy_uz)

# přihlášení nového uživatele
print("Přihlášení")
passw = input("Zadej heslo:")
prihlaseni = novy_uz.prihlas_se(passw)
if prihlaseni:
    print("úspěšné přihlášení")
else:
    print("neúspěšné přihlášení")

"""
# tohle je varianta kontroly délky hesla na statickou proměnnou
while delka < Uzivatel.minimalni_delka_hesla:
    passw = input("Heslo: ")
    delka = len(passw)
    if delka < Uzivatel.minimalni_delka_hesla:
        print(f"Heslo musí být dlouhé minimálně {Uzivatel.minimalni_delka_hesla} znaků")
"""