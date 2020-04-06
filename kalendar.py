"""
kalendar.py
práce s knihovnou calendar
"""
import calendar

print(calendar.calendar(2020))      # vypíše roční kalendář
print(calendar.month(1966, 1))      # vypíše kalendář zadaného měsíce

print(calendar.weekday(1966,1,30))  # vrátí číslo dne v týdnu v zadaném datu 0 - neděle, 1-pondělí,...
den_v_tydnu = {0:"pondělí",1:"úterý",2:"středa",3:"čtvrtek",4:"pátek", 5:"sobota", 6:"neděle"}
for i in range(24,31):
    den = calendar.weekday(1966,1,i)
    if den in range(0,2):
        print(f"{i}.1.1966 bylo {den_v_tydnu[den]} ")
    elif den in range(5,7) or den == 2:
        print(f"{i}.1.1966 byla {den_v_tydnu[den]} ")
    else:
        print(f"{i}.1.1966 byl {den_v_tydnu[den]} ")

# zjištění přestupných roků
print("přestupné roky")
for r in range(2000, 2120):
    leap = calendar.isleap(r)
    if leap:
        print(r,end=", ")