# Tuplas
# es una array inmutable, es decir, no se puede modificar

cocina = ('cuchara', 'cuchillo', 'tabla')
print(cocina)
print(len(cocina))

print(cocina[0])
print(cocina[-1])

print(cocina[0:2])

verduras = ('tomate',) # si no se pone la coma, no se considera tupla, sino es un string
print(verduras)


# recorrer tupla
for elem in cocina:
  print(elem, end=' ')
  

cocinaLista = list(cocina)
print(cocinaLista)
cocinaLista[0] = 'tenedor'
cocina = tuple(cocinaLista)
print(cocina)
cocina = ('te', 'cu', 'ta')
print(cocina)

