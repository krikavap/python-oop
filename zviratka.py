"""
zviratka.py

dle tutorialu https://naucse.python.cz/course/pyladies/beginners/class/
"""
class Kotatko:
    """
    vytvoří objekt Kotatko
    povinné argumenty: jmeno
    dostupné metody:
    zamnoukej()
    snez() s povinným argumentem jidlo 
    """
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return (f"Koťátko jménem {self.jmeno}")
                
    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")
        #return "Mňau!"

    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňam, {jidlo} mi chutná, mňau! ")

class Kocka:
    """
    třída kočka má devět životů
    dostupné metody:
    je_ziva() - True pokud pocet_zivotu > 0
    zamnoukej() - vrátí zamňoukání
    uber_zivot() - ubere 1 život 
    snez() s povinným argumentem jidlo 
    """
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.ini_pocet_zivotu = 9
        self.pocet_zivotu = self.ini_pocet_zivotu

    def __str__(self):
        return (f"Kočka jménem {self.jmeno}")

    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

    def uber_zivot(self, pocet):
        self.pocet_zivotu = self.pocet_zivotu - pocet
        text = self.je_ziva()
        print(text)
        
    def je_ziva(self):
        if self.pocet_zivotu > 0:
            return (f"{self.jmeno}: jsem živá ")
        else:
            return (f"{self.jmeno}: jsem mrtvá ")

    def snez(self, jidlo):
        if "ryba" in jidlo or self.pocet_zivotu != self.ini_pocet_zivotu:
            self.pocet_zivotu = self.pocet_zivotu + 1
        print(f"{self.jmeno}: Mňam, {jidlo} mi chutná, mňau! ")       
    


mourek = Kotatko("Mourek")

micka = Kotatko("Micka")

print(mourek)
print(micka)
mourek.zamnoukej()
micka.zamnoukej()

micka.snez("ryba a brambory")
mourek.snez("řízek")

skliba = Kocka("Sklíba")
print(skliba)
skliba.zamnoukej()
skliba.snez("mléko")
skliba.uber_zivot(3)
print(skliba.pocet_zivotu)
skliba.snez("mléko a ryba")
print(skliba.pocet_zivotu)

#print(micka.jmeno, micka.zamnoukej())
#print(mourek.jmeno, mourek.zamnoukej())

