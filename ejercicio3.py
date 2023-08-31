#imprima una matriz y luego sumar en diagonal

M = [[2,2,3,4,10],
    [6,3,9,0,2],
    [8,4,10,6,5],
    [1,0,1,6,6],
    [3,4,5,1,1]]

suma = 0
suma1 = 0
#diagonal principal
print("diagonal principal")
for d in range(len(M)):
    diagonal = M[d][d]
    print(diagonal)
    suma +=diagonal

print(f"suma:{suma}")

#diagonal secundaria
print("diagonal secundaria")
for i in range(len(M)):
    diag = M[i][-i-1]
    print(diag)
    suma1 +=diag

print(f"suma:{suma1}")
