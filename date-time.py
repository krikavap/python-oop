"""
date-time.py    
pokusy s knihovnou datetime
"""
import datetime

d1 = datetime.datetime(2020,4,6)            # class datetime 
print(d1)

# metody na class datetime
now = datetime.datetime.now()           # now vrátí aktuální datum a čas
print(now)
# metoda umí jednoduše vrátit jednotlivé složky datumu a času
print("Datum:")
print(f"Rok: {now.year} ")
print(f"Měsíc: {now.month} ")
print(f"Den: {now.day} ")
print("Čas:")
print(f"{now.hour}:{now.minute}:{now.second} ")
print(f"Datum jinak: {now.day}. {now.month}. {now.year} ")

# weekday() - vrátí index aktuálního dne v týdnu
den_v_tydnu = {0:"pondělí",1:"úterý",2:"středa",3:"čtvrtek",4:"pátek", 5:"sobota", 6:"neděle"}
# aktuální den v týdnu (využíváme proměnou now - viz výše)
den = den_v_tydnu[now.weekday()]
print(f"dnes je {den}")

# strftime() vytvoří použitelný a lehce čitelný formát data a času pro uživatele
text1 = now.strftime("%H:%M:%S")
text2 = now.strftime("Hodin: %H, Minut: %M, Sekund: %S")
text3 = now.strftime("Den: %d, Měsíc: %m, Rok: %Y")

print(text1)
print(text2)
print(text3)

# strptime() inverzní funkce k strftime()
info = "25. 3. 2020 12:35"
date = datetime.datetime.strptime(info, "%d. %m. %Y %H:%M")
print(date)

# aritmetické operace
now = datetime.datetime.now()       # do proměnné now aktuální datum
d2000 = datetime.datetime(2000, 1, 1)   # do proměnné d2000 datum 1.1.2000
d3 = now - d2000
d4 = datetime.timedelta.total_seconds(d3)   # timedelta.total_seconds() vrátí počet sekund v intervalu
print(f"počet dnů, hodin a minut od 1.1.2000: {d3}")
print(f"počet sekund od 1.1.2000: {d4}")