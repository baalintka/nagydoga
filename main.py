import feladatok
parosszamlista=[]
feladatok.haromparos()
parosszam=feladatok.beker()
parosszamlista.append(parosszam)
print(parosszamlista)
feladatok.legkisebb()
paratlan=feladatok.paratlan_osszege()
paros=feladatok.paros_osszege()
if paros < paratlan:
    print("Páratlan a nagyobb!")
else:
    print("Páros a nagyobb!")