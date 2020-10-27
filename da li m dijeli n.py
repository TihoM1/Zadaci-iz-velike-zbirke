"""
Napisati kod koji učitava dva cijela broja m i n 
i štampa poruku „x je djeljiv sa y” ili „x nije
djeljiv sa y“.
Npr. 
15 je djeljiv sa 3
15 nije djeljiv sa 4
"""
def da_li_je_djeljiv(x,y):
    if x%y==0:
        print(x,' je djeljiv sa ', y)
    else:
        print (x,' nije djeljiv sa ', y)

m=int(input())
n=int(input())
da_li_je_djeljiv(m,n)
