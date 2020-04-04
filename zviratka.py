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

mourek = Kotatko("Mourek")

micka = Kotatko("Micka")

print(mourek)
print(micka)
mourek.zamnoukej()
micka.zamnoukej()

micka.snez("ryba a brambory")
mourek.snez("řízek")


#print(micka.jmeno, micka.zamnoukej())
#print(mourek.jmeno, mourek.zamnoukej())

