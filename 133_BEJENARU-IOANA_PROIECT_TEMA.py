

#CALCULUL LAMBDA-TRANZITIILOR
def DFS(stare_initiala, stare, graf):
    global L_inchideri
    for tuplu in graf[stare]:
        if tuplu[0]=='.' and tuplu[1] not in L_inchideri[stare_initiala]:
            L_inchideri[stare_initiala].append(tuplu[1])
            DFS(stare_initiala, tuplu[1], graf)


#SIMULAREA ALGORITMULUI PT VERIFICAREA UNUI CUVANT CU LAMBDA INCHIDERI

def Verificare(multime_stari, cuv, poz, graf, L_inchideri, stari_finale):
    #intai lambda inchiderea pt a ne asigura ca o avem si la inceput si la final
    lista = []
    for stare in multime_stari:
        lista.extend(L_inchideri[stare])
    lista = set(lista)

    if poz<len(cuv):
        lista2=[]
        for stare in lista:
            for tuplu in graf[stare]:
                if tuplu[0]==cuv[poz]:
                    lista2.append(tuplu[1])
        lista2=set(lista2)
        lista2=list(lista2)
        Verificare(lista2, cuv, poz+1, graf, L_inchideri, stari_finale)
    elif poz==len(cuv):
        for elem in lista:
            if elem in stari_finale:
                print("DA")
                break
        else:
            print("NU")



f=open("fisier1.in")
nr_stari=int(f.readline().strip())
graf={}                             #dictionar in care fiecare stare reprezinta o cheie si are o lista de tupluri de forma (litera,stare in care ajungem)
for nod in f.readline().strip().split():
    graf[nod]=[]        #initializam cu lista vida
nr_litere=int(f.readline().strip())
alfabet=[]
for litera in f.readline().strip().split():
    alfabet.append(litera)      #ne formam alfabetul
alfabet.append('.')
stare_initiala=f.readline().strip()
nr_stari_finale=int(f.readline().strip())
stari_finale=[]
for s in f.readline().strip().split():
    stari_finale.append(s)
tranzitii=int(f.readline().strip())
lambda_=0
for i in range(tranzitii):
    cheie,litera,destinatie=f.readline().strip().split()
    if litera=='.':
        lambda_+=1
    if litera in alfabet:     #daca primim cumva muchii cu litere care nu sunt in alfabet nu are sens sa le adaugam
       graf[cheie].append((litera,destinatie))
cuvinte=int(f.readline().strip())

L_inchideri={}

for stare in graf:
    L_inchideri[stare]=[stare]
    DFS(stare, stare, graf)

for i in range(cuvinte):
    cuv=f.readline().strip()
    Verificare([stare_initiala], cuv, 0, graf, L_inchideri, stari_finale)