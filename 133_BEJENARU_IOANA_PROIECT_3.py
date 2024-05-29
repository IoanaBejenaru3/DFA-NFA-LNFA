#ALGORITMUL LUI CYK - se bazeaza pe FNC (forma normala chomsky)

#citim din fisier gramatica
#inputul va fi de forma -> terminalele (unde primul neterminal este si cel initial si toate neterminalele sunt pe o sg linie), productiile (cate una pe rand), cuvant de verificat

f = open("fisier1.in")
#citim neterminalele
cuv = f.readline().strip()
cuv = list('0'+cuv)
neterminale = []
for n in f.readline().strip().split():
    neterminale.append(n)
#citim productiile
productii = []
for line in f:
    n,exp = line.strip().split()
    productii.append((n,exp))
print(cuv)
print(neterminale)
print(productii)

#se creeaza initial o lista de tupluri de forma (x,y,z) unde x eeste lungimea cuv, in cazul nostru 1, y este indicele literei din cuvant
# si z reprezinta simbolul ce reprezinta neterminalul prin cacre obtinem acea litera
lista_valide = []
for i in range(len(cuv)):
    for j in range(len(neterminale)):
        if (neterminale[j],cuv[i]) in productii:
            lista_valide.append((1,i,neterminale[j]))
print(lista_valide)
#urmeaza sa simulam completarea tabelului de pe foaie cu cateva foruri
n = len(cuv)
for i in range(2,n+1):
    for j in range(1,n - i + 2):
        for k in range(1,i):
            for p in productii:
                if len(p[1]) > 1:
                    if (k,j,p[1][0]) in lista_valide and (i-k,j+k,p[1][1]) in lista_valide:
                        lista_valide.append((i,j,p[0]))
print(lista_valide)
#verificam daca am ajuns sa gasim cumva solutie pentru intreg cuvantul
if (n-1,1,neterminale[0]) in lista_valide: #stim ca pe prima pozitie in lista de neterminale se afla simbolul initial
    print("Cuvantul APARTINE gramaticii independente de context")
else:
    print("Cuvantul NU apartine gramaticii independente de context")




