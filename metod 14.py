"""
Napisati metod koji vraća true ako je n stepen broja
2 i false ako n nije stepen broja 2. 
"""
def je_li_stepen_2(n):
    x=1
    while 2**x<=n:
        if 2**x==n:
            return True
        x+=1
    return False

n=int(input('n = '))
print(je_li_stepen_2(n))