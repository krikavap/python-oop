"""
uzivatel.py
"""

class Uzivatel:
    def __init__(self, jmeno, vek):
        """ 
        iniciační metoda
        argumenty jmeno, vek
        
        self.__jmeno = jmeno
        self.__vek = vek
        """
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        """
        vrací textovou reprezenaci objektu
        text = str(self.__jmeno) + " věk: " + str(self.__vek)
        """
        text = str(self.jmeno) + " věk: " + str(self.vek)
        return text


# vytvoření instance (nového objektu) třídy Uzivatel. u obsahuje odkaz na objekt
u = Uzivatel("Jan Novák", 28)       
v = Uzivatel("Pavel Slánský", 32)

print(f"u: {u} \nid(u): {id(u)}")
print(f"v: {v} \nid(v): {id(v)}")
print("-" * 20)
u = v

print(f"u: {u} \nid(u): {id(u)}")
print(f"v: {v} \nid(v): {id(v)}")
print("-" * 20)
# změna
v.jmeno = "Bruce Wilace"

print(f"u: {u} \nid(u): {id(u)}")
print(f"v: {v} \nid(v): {id(v)}")
print("-" * 20)
# další změna
v.jmeno = "Pepa Chládek"
v = None
print(f"u: {u} \nid(u): {id(u)}")
print(f"v: {v} \nid(v): {id(v)}")