"""
Program koji odredjuje ukupan broj tackica na dominama
u skupu domina n.
n=2 -> broj tackica = 12
n=3 -> broj tackica = 30
n=15 -> broj tackica = 2040
"""
def broj_tackica(N):
    return N*(N+1)*(N+2)/2

n=int(input('N = '))
print('Broj  tackica iznosi',broj_tackica(n))