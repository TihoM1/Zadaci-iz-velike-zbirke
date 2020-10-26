import math
"""
U zbirci su data 5 izraza koje treba izracunati.
Za svaki izraz koriste se druge varijable
"""
def prvi_izraz(x,y):
    vrijednost_izraza1=x**3/3-3*y**2+(x+1)/(2*y+3)
    return vrijednost_izraza1

def drugi_izraz(x,y):
    vrijednost_izraza2=-5*math.sqrt(x+math.sqrt(y))
    return vrijednost_izraza2

def treci_izraz():
    vrijednost_izraza3=1+1/(2+1/(3+1/4))
    print(vrijednost_izraza3)

def cetvrti_izraz(α, β):
    vrijednost_izraza4=3*math.sin(2*α)*math.cos(2*β)-5*math.tan(α+β)**2
    return vrijednost_izraza4

def peti_izraz(a,b,α):
    vrijednost_izraza5=math.sqrt(a**2+b**2-2*a*b*math.sin(α))
    return vrijednost_izraza5

xx=int(input('x = '))
yy=int(input('y = '))
alfa=int(input('α = '))
beta=int(input('β = '))
aa=int(input('a = '))
bb=int(input('b = '))
print("Rezultat prvog izraza: ", prvi_izraz(xx,yy))
print("Rezultat drugog izraza: ",drugi_izraz(xx,yy))
print("Rezultat treceg izraza: ", treci_izraz())
print("Rezultat cetvrtog izraza: ",cetvrti_izraz(alfa,beta))
print("Rezultat petog izraza: ", peti_izraz(aa,bb,alfa))