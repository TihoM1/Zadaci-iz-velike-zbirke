"""
Napisati metod koji vraća najveću cifru broja n. 
"""
def naj_cifra(n):#razdvaja broj na niz cifara i uz pomoc funkcije max vraca naj cifru
    d=[]
    for i in range(1, n ):
            d.append(n % 10)
            n//=10
    return max(d)

n=int(input('n = '))
print("Najveca cifra broja n je:",naj_cifra(n))
