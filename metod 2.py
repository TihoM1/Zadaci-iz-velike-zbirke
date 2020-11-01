"""
Napisati metod  koji vraća zbir svih cijelih
brojeva iz intervala [a,b]
"""
def zbir_intervala(a,b):
    zbir=0
    i=a
    while i<=b:
        zbir+=i
        i+=1
    return zbir

a=int(input('a = '))
b=int(input('b = '))
print(zbir_intervala(a,b))