def verificare(cuv,poz,graf,stare,stari_finale,ct):
    global ok   #ne ajuta sa stim daca am gasit deja o stare pt a nu pune apeluri recursive pe stiva degeaba
    global nr_stari
    if ct-poz+1>nr_stari:  #pentru cazurile in care avem cicluri, sa trecem peste ele (daca nu am inaintat deloc cu poz
        pass               #inseamna ca am mers doar pe lambda-uri si daca mergem in mai multe de nr de stari sigur a aparut un ciclu si trebuie sa-l evitam
    elif poz==len(cuv): #doar daca am parcurs toate literele verificam starea
        if stare in stari_finale:
            ok=True  #daca e finala e perfect
        elif graf[stare]!=[]:   #alfel verificam daca putem sa ne folosim de lambda sa ajungem intr-o stare finala
            for tuplu in graf[stare]:
                if ok==False:       #doar daca n-am gasit inca un drum care accepta cuvantul
                    if tuplu[0]=='.':   #doar daca este lambda continuam sa facem lambda miscari
                        verificare(cuv, poz, graf, tuplu[1], stari_finale,ct+1)  #nu modificam poz
    elif graf[stare]==[]:   #daca n-am parcurs tot cuvantul si ne blocam, adica nu avem o muchie pe care sa mergem
        pass                #pass
    elif poz<len(cuv):  #daca inca avem litere de parcurs
        for tuplu in graf[stare]:
            if ok == False:
                if tuplu[0]==cuv[poz]:
                    verificare(cuv,poz+1,graf,tuplu[1],stari_finale,ct+1) #poz+1 ne mutam la urmatoarea litera
                elif tuplu[0]=='.':
                    verificare(cuv, poz, graf, tuplu[1], stari_finale,ct+1) #putem sa mergem si pe o muchie cu lambda dar nu modificam pozitia/ramanem la ac litera


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
ok=None
for i in range(cuvinte):
    cuv=f.readline().strip()
    ok=False        #inainte de verificarea oricarui cuvant presupunem ca nu avem niciun drum din care reiese ca este acceptat
    verificare(cuv,0,graf,stare_initiala,stari_finale,0) #incepem de pe pozitia 0
    if ok==True:
        print("DA")
    else:
        print("NU")
