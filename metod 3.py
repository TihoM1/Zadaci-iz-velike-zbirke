import math
"""
Napisati metod d koji vraća dužinu duži 
čije su krajnje tačke A(x1, y1) i B(x2,y2). 
"""
def duzina_duzi(X1,Y1,X2,Y2):
    duzina = math.sqrt((X2-X1)**2+(Y2-Y1)**2)
    return duzina

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print('Duzina duzi:',duzina_duzi(x1,y1,x2,y2))