#1 feladat:

lista=[]
import random
def beker():
    szam = int(input("kérem adjon meg egy számot"))
    while szam % 2 != 0:
        print("Ez nem páros! PÁROSAT KÉREK!")
        szam = int(input("kérem adjon meg egy számot"))
    lista.append(szam)
    return szam

def haromparos():
    for i in range(3):
        paros = beker()
        print(f"{i+1}. páros szám!")

def legkisebb():
    i=0
    min=0
    minindex=0
    while i<len(lista):
        if lista[i]< min:
            min=lista[i]
            minindex=i
        i+=1
    print(f"Legkisebb szám:{min} és a {minindex}. nak adta meg a felhasználó")

#2. feladat
listavszam=[]
def masodikfeladat():
    for i in range(13):
        vszam = random.randint
        print(vszam)
        listavszam.append(vszam)

def ketjegyuek_szama(listavszam):
    ketjegyu=0
    for i in range (len(listavszam)):
        if listavszam[i]> 9 and listavszam[i] < 100:
            ketjegyu+=1
    return ketjegyu
def paros_osszege(listavszam):
    osszeg = 0
    for i in range(len(listavszam)):
        if listavszam[i] %2==0:
            osszeg += listavszam[i]
    return osszeg
def paratlan_osszege(listavszam):
    osszeg = 0
    for i in range(len(listavszam)):
        if listavszam[i] % 2 != 0:
            osszeg += listavszam[i]
    return osszeg
paratlan=paratlan_osszege(listavszam)
paros=paros_osszege(listavszam)
if paros < paratlan:
    print("Páratlan a nagyobb!")
else:
    print("Páros a nagyobb!")

#3.feladat
def fajlosfeladat():
    listaa=[]
    fajlom=open("stadionok.txt")
    sorok=fajlom.readlines()
    listaa.append(sorok)
    listaa.remove(listaa[0])
    print(len(listaa))
