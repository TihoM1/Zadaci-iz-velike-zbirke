"""
Napisati metod koji vraća broj pozitivnih djelilaca broja n.
"""
def djelioci(n):
    d=[]
    for i in range(1, n + 1):
        if n % i == 0:
            d.append(i)
    return len(d)

n=int(input('n = '))
print('Broj djelioca iznosi:',djelioci(n)) 