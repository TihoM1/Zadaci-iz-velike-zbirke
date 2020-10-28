"""
Kod koji provjerava da li je godina prestupna.
Godina je prestupna ako je djeljiva sa 4 i 100 ili sa 4,100 i 400.
"""
def da_li_je_prestupna(godina):
    if godina%4==0:
        if godina%100==0:
            if godina%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

god=int(input("Unesite godinu: "))
print(da_li_je_prestupna(god))