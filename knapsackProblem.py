# Autor: Juan Jose Restrepo Rosero
# Intern Veevart 2023

elementos = [(2, 3), (3, 4), (4, 5), (5, 6)]
vi = []
wi = []
maxCap = 8


def solveKnapsack(elementos, maxCap, n):
    n = len(elementos)
    # Creamos una tabla para almacenar los resultados de los subproblemas
    table = [[0 for _ in range(maxCap + 1)] for _ in range(n + 1)]

    # Resolvemos los subproblemas de forma iterativa
    for i in range(1, n + 1):
        for j in range(1, maxCap + 1):
            wi, vi = elementos[i - 1]
            if wi > j:
                # Si el peso del elemento i es mayor que la capacidad j, no podemos llevarlo
                table[i][j] = table[i - 1][j]
            else:
                # Si podemos llevar el elemento i, debemos decidir si lo llevamos o no
                table[i][j] = max(table[i - 1][j], vi + table[i - 1][j - wi])

    # Recuperamos los elementos seleccionados y el valor total obtenido elementos_seleccionados
    elementos_seleccionados = []
    j = maxCap
    for i in range(n, 0, -1):
        if table[i][j] != table[i - 1][j]:

            elementos_seleccionados.append(elementos[i - 1])
            j -= elementos[i - 1][0]

            if j == 0:
                break

    valorTotal = table[n][maxCap]

    return elementos_seleccionados[::-1], valorTotal


def separarPesoValor(elementos, wi, vi):
    for peso, valor in elementos:
        wi.append(peso)
        vi.append(valor)
    
    return wi, vi

wi, vi = separarPesoValor(elementos, wi, vi)

print("\nPesos Elementos (wi): ", wi)
print("Valores Elementos (vi): ", vi)
n = len(vi)
print("Tam lista valores: ", n)
solucion = solveKnapsack(elementos, maxCap, n)

print("Combinacion mas optima: ", solucion)
