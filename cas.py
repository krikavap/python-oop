"""
cas.py
cviceni s knihovnami time a calendar
"""
import time
i = 1
startClock = time.process_time()   # fce time.clock() vrátí počet sekund práce procesoru na tomto procesu
startTime = time.time()     # fce time.time() vrátí číslo ukazující počet sekund od 1/1/1970 
while (time.time()-startTime) < 1 :             # cyklus trvající 1 sekundu
    print (time.time())
    i = i + 1
print(f"proběhlo {i} cyklů")
print(f"procesor na tomto programu pracoval {time.process_time()} s ")
print(f"světový aktuální čas {time.gmtime()}")

# konverze výstupu time.gmtime() do lidského formátu
svet = time.gmtime()        
print(f"konverze time.gmtime() datum: {svet[2]}. {svet[1]}. {svet[0]} čas: {svet[3]}:{svet[4]}:{svet[5]}")
print(f"místní aktuální čas {time.localtime()}")
loc = time.localtime()
print(f"aktuální místní datum a čas pomocí time.asctime() {time.asctime(loc)}")
print(f"aktuální místní datum a čas pomocí time.ctime() {time.ctime()}")


