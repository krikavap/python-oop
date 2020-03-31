"""
helloObjectWorld.py
"""
# definice třídy
class Zdravic:
    """
    třída Zdravic, která slouží ke zdravení uživatelů 
    má tyto metody:
    - pozdrav_prvni - bez parametrů
    - pozdrav_druhy - parametrem předáváme jméno osoby
    - pozdrav_treti - navic definujeme atributem text pozdravu

    """
    # metoda pozdrav_prvni
    def pozdrav_prvni(self):
        """
        vrátí text Hello Object World!
        """
        return (f"Hello Object World!")
                
    # metoda pozdrav_druhy
    def pozdrav_druhy(self, jmeno):
        """
        vrátí text Ahoj uživateli + jméno předané parametrem při volání metody
        """
        return (f"Ahoj uživateli {jmeno} !!!")

    # metoda pozdrav_treti
    def pozdrav_treti(self, jmeno):
        """
        vrátí text pozdravu + jméno. 
        Text je atribut metody definovaný před voláním metody.
        Jméno je parametr předaný při volání metody.
        """
        return (f"{self.text} {jmeno} !!!")

# konec obsahu třídy

# vytvoření instance zdravic třídy Zdravic
zdravic = Zdravic()

# volání metod a rovnou tisk výsledků
print("-" * 25)
print(zdravic.pozdrav_prvni())

print("-" * 25)

print(zdravic.pozdrav_druhy("Karle"))
print(zdravic.pozdrav_druhy("Pepo"))
print("-" * 25)

zdravic.text = "Ahoj uživateli"
print(zdravic.pozdrav_treti("Karle"))
print(zdravic.pozdrav_treti("Pepo"))
print("-" * 25)
zdravic.text = "Vítám tě tu, programátore"
print(zdravic.pozdrav_treti("Richarde"))
print("-" * 25)

input()
