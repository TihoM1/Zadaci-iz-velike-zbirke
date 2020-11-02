"""
Napisati metod  koji štampa sve pozitivne djelioce
broja n. 
"""
def djelioci(n):
    d=[]
    for i in range(1, n + 1):
        if n % i == 0:
            d.append(i)
    return d
N=int(input('n = '))
print('Djelioci broja n su:',djelioci(N))