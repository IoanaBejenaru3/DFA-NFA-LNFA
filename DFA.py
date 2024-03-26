import sys
#CITIREA DATELOR IN DFA

def verificare(cuv,graf,stare_initiala,stari_finale):
    stare=stare_initiala
    for c in cuv:
        gasit=False
        if graf[stare]==[]:
            return False
        for tuplu in graf[stare]:
            if tuplu[0]==c:
                gasit=True
                stare=tuplu[1]
                break
        print(stare)
        if gasit is False:
            return False
    if stare in stari_finale:
        return True
    return False



f=open("fisier1.in")
nr_stari=int(f.readline().strip())
graf={}
for nod in f.readline().strip().split():
    graf[nod]=[]
nr_litere=int(f.readline().strip())
alfabet=[]
for litera in f.readline().strip().split():
    alfabet.append(litera)
stare_initiala=f.readline().strip()
nr_stari_finale=int(f.readline().strip())
stari_finale=[]
for s in f.readline().strip().split():
    stari_finale.append(s)
tranzitii=int(f.readline().strip())
for i in range(tranzitii):
    cheie,litera,destinatie=f.readline().strip().split()
    if litera not in alfabet:
        sys.exit(0)
    graf[cheie].append((litera,destinatie))
cuvinte=int(f.readline().strip())
for i in range(cuvinte):
    cuv=f.readline().strip()
    val=verificare(cuv,graf,stare_initiala,stari_finale)
    if val is True:
        print("DA")
    else:
        print("NU")