# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lista = []
    for sublista in matrix:
        for elem in sublista:
            lista.append(elem)
    return lista

print(flatten([[1, 2], [3, 4], [5, 6]]))

def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    lista = []
    
    for i in range(len(matrix)):
        lista.append(sum(matrix[i]))
    return lista
            
print(row_sums([[1, 2, 3], [4, 5, 6]]))

def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    lista = []
    for j in range(len(matrix[0])):
        suma = 0
        for i in range(len(matrix)):
            suma += matrix[i][j]
        lista.append(suma)
    
    return lista
print(col_sums([[1, 2, 3], [4, 5, 6]]))
