import math
"""
Date su koordinate tri tacke u koordinatnom sistemu.
Izracunati obim i povrsinu tog trougla:
A(-3,4) B(1,-2) C(5,5)- Obim = , Povrsina = 26
"""
def povrsina_trougla(Ax,Ay,Bx,By,Cx,Cy):
    povrsina = 1/2*abs(Ax*(By-Cy)+Bx*(Cy-Ay)+Cx*(Ay-By))
    return povrsina

def obim_trougla(Ax,Ay,Bx,By,Cx,Cy):
    str_AB=math.sqrt((Bx-Ax)**2+(By-Ax)**2)
    str_BC=math.sqrt((Cx-Bx)**2+(Cy-By)**2)
    str_CA=math.sqrt((Ax-Cx)**2+(Ay-Cy)**2)
    obim = str_AB + str_BC + str_CA
    return obim

x1=int(input('Koordinate tacke A: '))
y1=int(input())
x2=int(input('Koordinate tacke B: '))
y2=int(input())
x3=int(input('Koordinate tacke C: '))
y3=int(input())
print("Povrsina trougla je: ",povrsina_trougla(x1,y1,x2,y2,x3,y3))
print("Obim trougla je: ", obim_trougla(x1,y1,x2,y2,x3,y3)) 