"""
Program koji na osnovu unesenog broja galeona, srpova i knutova
stampa broj knutova. Jedan galeon ima 17 srpova a jedan srp 29
knutova
"""
def iz_galeona_i_srpova_u_knutove(g,s,k):
    n_knutova = g*17*29+s*29+k
    return n_knutova

galeon=int(input('Galeoni: '))
srpovi=int(input('Srpovi: '))
knutovi=int(input('Knutovi: '))
print('Harry ima',iz_galeona_i_srpova_u_knutove(galeon,srpovi,knutovi),'knutova.')
