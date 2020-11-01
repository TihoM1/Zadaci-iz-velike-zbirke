"""
Napisati metod  koji vraća true ako broj x pripada 
intervalu [a, b] i vraća false ako ne pripada. 
"""
def pripada_intervalu(a,b,x):
    i=a
    while i<=b:
        if x==i:
            return True
        i+=1
    return False

a=int(input())
b=int(input())
x=int(input())
print(pripada_intervalu(a,b,x))