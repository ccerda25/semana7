from opm import (
    mostrar_matriz,
    escalar_matriz,
    crear_matriz,
    crear_matriz_3x3,
    sumar_matrices,
    multiplicar_matrices,
    matriz_identidad
)


def ejercicio_1():
    print("\n--- MULTIPLICACIÓN POR ESCALAR ---")

    matriz = [
        [1, 2],
        [3, 4]
    ]

    k = 5

    print("Matriz original:")
    mostrar_matriz(matriz)

    matrizB = escalar_matriz(matriz, k)

    print("=" * 13)
    print("Escalar:", k)

    print("Matriz resultante:")
    mostrar_matriz(matrizB)


def ejercicio_2():
    print("\n--- CREAR MATRIZ 2x2 ---")

    matriz = crear_matriz()

    print("\nMatriz ingresada:")
    mostrar_matriz(matriz)


def ejercicio_3():
    print("\n--- SUMA DE MATRICES 3x3 ---")

    print("\nDigite los valores de la matriz 1:")
    matriz1 = crear_matriz_3x3()

    print("\nDigite los valores de la matriz 2:")
    matriz2 = crear_matriz_3x3()

    matriz_resultado = sumar_matrices(matriz1, matriz2)

    print("\nMatriz 1:")
    mostrar_matriz(matriz1)

    print("\nMatriz 2:")
    mostrar_matriz(matriz2)

    print("\nMatriz Resultado:")
    mostrar_matriz(matriz_resultado)


def ejercicio_4():
    print("\n--- MULTIPLICACIÓN DE MATRICES 2x2 ---")

    print("\nDigite los valores de la matriz A:")
    matrizA = crear_matriz()

    print("\nDigite los valores de la matriz B:")
    matrizB = crear_matriz()

    matrizC = multiplicar_matrices(matrizA, matrizB)

    print("\nMatriz A:")
    mostrar_matriz(matrizA)

    print("\nMatriz B:")
    mostrar_matriz(matrizB)

    print("\nLa matriz resultante es:")
    mostrar_matriz(matrizC)


def ejercicio_5():
    print("\n--- MATRIZ DE IDENTIDAD ---")

    n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

    matriz = matriz_identidad(n)

    print("\nLa matriz de identidad es:")
    mostrar_matriz(matriz)


def menu():
    while True:
        print("\n==============================")
        print("       MENÚ DE MATRICES")
        print("==============================")
        print("1. Multiplicar matriz por escalar")
        print("2. Crear matriz 2x2")
        print("3. Sumar matrices 3x3")
        print("4. Multiplicar matrices 2x2")
        print("5. Crear matriz de identidad")
        print("6. Salir")
        print("==============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejercicio_1()

        elif opcion == "2":
            ejercicio_2()

        elif opcion == "3":
            ejercicio_3()

        elif opcion == "4":
            ejercicio_4()

        elif opcion == "5":
            ejercicio_5()

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


menu()