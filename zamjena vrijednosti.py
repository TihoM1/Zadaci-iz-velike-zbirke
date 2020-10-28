"""
 Napisati kod koji mijenja mjesta vrijednostima u
promjenljivim x i y.
"""
def zamjena_mjesta(a,b):
    a,b=b,a
    return a,b

A=int(input())
B=int(input())
print(zamjena_mjesta(A,B))