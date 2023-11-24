miLista = ["Manuel","Paula","Victoria","Mónica"]
miLista.append("Mariano")
miLista.insert(2,"Genaro")
miLista.extend([True,"Marta",5])
print(miLista[:])
print(miLista[0])
print(miLista[-2])
print(miLista[0:2])
print(miLista[:2])
print(miLista[1:2])
print(miLista[2:])
print(miLista.index("Genaro"))
print("Manuel" in miLista)
miLista.remove("Genaro")
print(miLista[:])
miLista.pop()
print(miLista[:])
miLista2 = ["MercedesBenz","Renault"]
miLista3 = miLista + miLista2
print(miLista3[:])
miLista3 * 3
print(miLista3[:])
