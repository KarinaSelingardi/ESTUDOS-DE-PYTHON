from sympy import Matrix

 # Matriz aumentada [A | b]
A = Matrix([
     [2, 1, 1, 4],
     [4, 3, 1, 10],
    [-2, 2, 3, -6]
     ])
 
 # Aplica Gauss-Jordan
rref_matrix, pivots = A.rref()
 
print("Matriz reduzida (forma de Gauss-Jordan):")
print(rref_matrix)
  
