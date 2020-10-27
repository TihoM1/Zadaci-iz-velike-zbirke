"""
 Dat je četvorocifreni prirodan broj. Ako su mu cifra jedinica i cifra hiljada jednake,
štampati kvadrat dvocifrenog broja koji se dobije kada se uklone cifra jedinica i cifra
hiljada. Ako te dvije cifre nisu jednake, štampati zbir kvadrata svih cifara. 
Npr. 1151 -> 225
2345 -> 54
"""
def racunanje_izraza(abcd):
    jedinice=abcd%10
    desetice=(abcd//10)%10
    stotine=(abcd//100)%10
    hiljade=abcd//1000
    if jedinice==hiljade:
        bc=desetice+stotine*10
        return bc**2
    else:
        return jedinice**2+desetice**2+stotine**2+hiljade**2

x=int(input('Unesite cetvorocifren broj: '))
print('Rezultat je: ', racunanje_izraza(x))


