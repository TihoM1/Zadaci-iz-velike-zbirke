"""
Napisati metod koji vraća zbir pozitivnih 
djelilaca broja n manjih od n. 
"""
def djelioci(n):
    d=[]
    for i in range(1, n):
        if n % i == 0:
            d.append(i)
    return d
def zbir_djelilaca_manjih_od_n(dj):
    return sum(dj)

N=int(input('n = '))
print('Zbir djelioca manjih od n:',zbir_djelilaca_manjih_od_n(djelioci(N)))