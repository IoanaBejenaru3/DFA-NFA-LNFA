import sys

def verificare(cuv,poz,graf,stare,stari_finale):
    global ok
    if poz==len(cuv):
        if stare in stari_finale:
            ok=True
    elif graf[stare]==[]:
        pass
    elif poz < len(cuv):
        for tuplu in graf[stare]:
            if ok == False:
                if tuplu[0]==cuv[poz]:
                    verificare(cuv,poz+1,graf,tuplu[1],stari_finale)


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
ok=None
for i in range(cuvinte):
    cuv=f.readline().strip()
    ok=False
    verificare(cuv,0,graf,stare_initiala,stari_finale)
    if ok==True:
        print("DA")
    else:
        print("NU")
