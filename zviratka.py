"""
zviratka.py

dle tutorialu https://naucse.python.cz/course/pyladies/beginners/class/
"""
class Zviratko:
    """
    spolecna trida pro vsechny zviratka
    metody:
    snez(jidlo) - sni jidlo, vypíše text
    udelej_zvuk(zvuk) - vypíše zvuk 

    """
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná! ")

    def udelej_zvuk(self, zvuk):
        """
        metoda vypíše zvuk
        """
        print(f"{self.jmeno}: {zvuk}! ")


class Kotatko(Zviratko):
    """
    dedicna trida z tridy Zviratka
    vytvoří objekt Kotatko
    
    """
    def __str__(self):
        return (f"Koťátko jménem {self.jmeno}")
                
    
class Stenatko(Zviratko):
    """
    trida stenatek
       
    """
    def __str__(self):
        return (f"Štěňátko jménem {self.jmeno}")
                
       
class Kocka(Zviratko):
    """
    dedicna trida z tridy Zviratka
    třída kočka má devět životů
    dostupné metody:
    je_ziva() - True pokud pocet_zivotu > 0
    uber_zivot() - ubere 1 život 
    snez() - lokalni metoda stejneho jmena, jako metoda v nadtride. Lokalni ma prednost.
    """
    def __init__(self, jmeno):
        """
        metoda se spusti pri vytvareni instance objektu
        super() prevezme funkcionalitu metody nadtridy
        a doplni dalsi vlastnosti self.ini_pocet_zivotu (maximálni pocet zivotu)
        a priradi jej do self.pocet_zivotu
        """
        super().__init__(jmeno)         
        self.ini_pocet_zivotu = 9
        self.pocet_zivotu = self.ini_pocet_zivotu

    def __str__(self):
        return (f"Kočka jménem {self.jmeno}")

    def uber_zivot(self, pocet):
        """
        metoda ubere z aktualniho mnozstvi zivotu pocet zivotu definovane v argumentu pocet
        """
        if not self.je_ziva():
            print("Nemůžeš zabít mrtvou kočku")
        else:
            self.pocet_zivotu = self.pocet_zivotu - pocet
        
    def je_ziva(self):
        """
        metoda testuje, zda ma kocka pocet_zivotu > 0
        """
        if self.pocet_zivotu > 0:
            return True
        else:
            return False

    def snez(self, jidlo):
        """
        lokálni metoda snez() ma prednost pred metodou snez() z nadtridy
        argument jidlo obsahuje nazev jidla
        testuje, zda je kocka ziva
        pokud jidlo obsahuje ryba, pak pricte jeden zivot (do vyse maximalniho poctu zivotu)
        """
        if not self.je_ziva():
            print("Je zbytečné krmit mrtnou kočku")
        
        elif "ryba" in jidlo or self.pocet_zivotu != self.ini_pocet_zivotu:
            self.pocet_zivotu = self.pocet_zivotu + 1
            print(f"Kočka snědla rybu a obnovil se jí jeden život")
        else:
            print(f"{self.jmeno}: Mňam, {jidlo} mi chutná, mňau! ")       
    


mourek = Kotatko("Mourek")
micka = Kotatko("Micka")
zorro = Stenatko("Zorro")

print(mourek)
print(micka)
print(zorro)
mourek.udelej_zvuk("Mňau")
micka.udelej_zvuk("Mňau, mňoumňau")
zorro.udelej_zvuk("Haf, haf, haf")

micka.snez("ryba a brambory")
mourek.snez("řízek")
zorro.snez("kost a maso")

# ukázka polymorfismu
# důležitá vlastnost podtříd: když máš nějaké Kotatko, můžeš ho použít
# kdekoliv kde program očekává Zviratko, protože každé koťátko je zvířátko.

zviratka = [Kotatko("Micka"), Kotatko("Mourek"), Stenatko("Zorro")]
for i in zviratka:
    i.snez("flákota")

skliba = Kocka("Sklíba")
print(skliba)
skliba.udelej_zvuk("Mňau")
skliba.snez("mléko")
skliba.uber_zivot(3)
print(skliba.pocet_zivotu)
skliba.snez("mléko a ryba")
print(skliba.pocet_zivotu)


