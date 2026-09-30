matriz = []

n = int(input("Digite la cantidad de filas y columnas: "))

for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)

    matriz.append(fila)
    
print("Matriz de identidad:")
for fila in matriz:
    print(fila)