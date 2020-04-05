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

passw = ""
print("Registrace")
name = input("Jméno: ")
delka = 0
while delka < Uzivatel.minimalni_delka_hesla:
    passw = input("Heslo: ")
    delka = len(passw)
    if delka < Uzivatel.minimalni_delka_hesla:
        print(f"Heslo musí být dlouhé minimálně {Uzivatel.minimalni_delka_hesla} znaků")
pepa = Uzivatel(name, passw)
print(pepa)

print("Přihlášení")
passw = input("Zadej heslo:")
prihlaseni = pepa.prihlas_se(passw)
if prihlaseni:
    print("úspěšné přihlášení")
else:
    print("neúspěšné přihlášení")
