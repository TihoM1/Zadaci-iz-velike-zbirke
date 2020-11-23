import math
"""
Napisati metod koji vraća true ako postoji trougao sa
tjemenima (x1,y1), (x2,y2), (x3,y3) i false ako trougao ne postoji. 
A=(-1, 2)
B=(1, 1)   => postoji
C=(2, 3)

D = (-1, -1)
E = (0, -1)   => ne postoji
F = (1 , -1)
"""
def postoji(x1, y1, x2, y2, x3, y3):
    if math.sqrt(abs(x2-x1)**2+abs(y2-y1)**2) < math.sqrt(abs(x3-x2)**2+abs(y3-y2)**2) + math.sqrt(abs(x1-x3)**2+abs(y1-y3)**2) and \
       math.sqrt(abs(x3-x2)**2+abs(y3-y2)**2) < math.sqrt(abs(x2-x1)**2+abs(y2-y1)**2) + math.sqrt(abs(x1-x3)**2+abs(y1-y3)**2) and \
       math.sqrt(abs(x1-x3)**2+abs(y1-y3)**2) < math.sqrt(abs(x2-x1)**2+abs(y2-y1)**2) + math.sqrt(abs(x3-x2)**2+abs(y3-y2)**2):
        return True
    else: 
        return False 

X1=int(input())
Y1=int(input())
X2=int(input())
Y2=int(input())
X3=int(input())
Y3=int(input())
print(postoji(X1, Y1, X2, Y2, X3, Y3))