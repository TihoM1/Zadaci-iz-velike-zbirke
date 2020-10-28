"""
Za uneseni redni broj mjeseca i godinu stampati broj
dana u mjesecu.
npr. 1, 2020 -> 31 dana
2, 2020 -> 29 dana
2, 2021 -> 28 dana
4, 2020 -> 30 dana
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

def broj_dana(redni_broj_mjeseca, god):
    mjeseci_sa_31_danom = [1,3,5,7,8,10,12]
    mjeseci_sa_30_dana = [4,6,9,11]
    if god==True and redni_broj_mjeseca==2:
        print('29 dana')
    elif god==False and redni_broj_mjeseca==2:
        print('28 dana')
    elif redni_broj_mjeseca in mjeseci_sa_31_danom:
        print('31 dan')
    elif redni_broj_mjeseca in mjeseci_sa_30_dana:
        print('30 dana')
    else:
        print('Nepostojeci mjesec')

n=int(input('Unesite redni broj mjeseca: '))
g=int(input('Unesite godinu: '))
broj_dana(n,da_li_je_prestupna(g))