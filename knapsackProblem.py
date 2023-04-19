

elementos = [(2, 3), (3, 4), (4, 5), (5, 6)]
vi = []
wi = []
maxCapacidad = 8


def solveKnapsack(maxCap, wi, val, n):

    if n == 0 or maxCap == 0 :
        return 0

    # si el peso del n_avo elemento es mayor que la capacidad de la mochila
    # entonces no se incluye 
    if (wi[n-1] > maxCap):
        return solveKnapsack(maxCap, wi, val, n-1)

    else:
        return max(val[n-1] + solveKnapsack(maxCap - wi[n-1], wi, val, n-1), solveKnapsack(maxCap, wi, val, n-1))

def separarPesoValor(elementos, wi, vi):
    for peso, valor in elementos:
        wi.append(peso)
        vi.append(valor)
    
    return wi, vi


wi, vi = separarPesoValor(elementos, wi, vi)

print(wi)
print(vi)
n = len(vi)

#print(n)
solucion = solveKnapsack(maxCapacidad, wi, vi, n)
#solucion = solveKnapsack(0, wi, vi, 0)

print("Valor Total: ", solucion)





"""

def knapSack(W, wt, val, n):
  
    # Base Case
    if n == 0 or W == 0 :
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
  
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))
  
  

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapSack(W, wt, val, n)
  

"""