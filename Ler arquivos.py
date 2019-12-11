file = open ("veiculos.txt", "r")

##Quantidade de veiculos cadastados##    
file.seek(0)
x=len(file.readlines())
print('Veículos cadastrados:',x-1)

##Quantidade de veiculos disponiveis##     
file.seek(0)
i=1
reservados = 0
while i < x+1:
    y = file.readline ()
    reservados = reservados + y.count ("False")
    i += 1
print ('Veículos disponíveis:' ,reservados)

## Quantos Corollas? ##     
file.seek(0)
j=1
corollas = 0
while j < x+1:
    y = file.readline ()
    if y.count ("False") and y.count ("Corolla"): 
        corollas += 1 
    j += 1
print ('Corollas disponíveis:',corollas)

##Quantos carros de 2017?##        
file.seek(0)
k=1
ano = 0
while k < x+1:
    y = file.readline ()
    ano = ano + y.count ("2017")
    k += 1
print ('Veículos de 2017:' ,ano)

##Quantos veículos não iniciam a placa com inicial P?##      
file.seek(0)
l = 0
placa = 0
lista = []
line=file.readline()
while (line != ""):
    l += 1
    y = file.readline ()
    lista = y.split("\t")
    if (l < 20001):
        plaka = lista[6]
        if plaka.startswith("P") == False:
            placa = placa + 1
    else:
        break
print ('Quantidade de veículos que não inicial a placa com a letra P:' ,placa)

veiculos_cadastrados = str(x-1)
veiculos_disponiveis = str(reservados)
corollas_disponiveis = str(corollas)
veiculos_ano = str(ano)
veiculos_placa = str(placa)

##Gravando em resultado.txt
fh = open("resultados.txt","w")
fh.write("Veículos cadastrados: ")
fh.write(veiculos_cadastrados + "\n")
fh.write("Veículos disponíveis: ")
fh.write(veiculos_disponiveis  + "\n")
fh.write("Corollas disponíveis: ")
fh.write(corollas_disponiveis + "\n")
fh.write("Veículos de 2017: ")
fh.write(veiculos_ano + "\n")
fh.write("Quantidade de veículos que não inicial a placa com a letra P: ")
fh.write(veiculos_placa + "\n")
fh.close()

########################################################################################
########################################################################################
########################################################################################

##Quantidade de carros vans e utilitarios##
file.seek(0)
l = 0
carro = 0
van = 0
ute = 0
lista = []
line=file.readline()
while (line != ""):
    l += 1
    y = file.readline ()
    lista = y.split("\t")
    if (l < 20001):
        plaka = lista[0]
        if plaka.startswith("carro") == True:
            carro = carro + 1
        if plaka.startswith("van") == True:
            van = van + 1
        if plaka.startswith("ute") == True:
            ute = ute + 1
    else:
        break
#print (carro)
#print (van)
#print (ute)

##Falta plotar o gráfico ACIMA


##Quantidade de veiculos reservados por modelo## 

file.seek(0)
l = 0
uno = 0
ducato = 0
prisma = 0
kam = 0
gol = 0
civic = 0
sprinter = 0
spin = 0
sandero = 0
ka = 0
onix = 0
logan = 0
corolla = 0


lista = []
line=file.readline()
while (line != ""):
    l += 1
    y = file.readline ()
    lista = y.split("\t")
    if (l < 20001):
        plaka = lista[2]
        reservacarro = lista[9]
        if reservacarro.count ("True") and plaka.count ("Uno") :
            uno = uno + 1
        if reservacarro.count ("True") and plaka.count ("Ducato"):
            ducato = ducato + 1
        if reservacarro.count ("True") and plaka.count ("Prisma"):
            prisma = prisma + 1
        if reservacarro.count ("True") and plaka.count ("Ka+"):
            kam = kam + 1
        if reservacarro.count ("True") and plaka.count ("Gol"):
            gol = gol + 1
        if reservacarro.count ("True") and plaka.count ("Civic"):
            civic = civic + 1
        if reservacarro.count ("True") and plaka.count ("Sprinter"):
            sprinter = sprinter + 1
        if reservacarro.count ("True") and plaka.count ("Spin"):
            spin = spin + 1
        if reservacarro.count ("True") and plaka.count ("Sandero"):
            sandero = sandero + 1
        if reservacarro.count ("True") and plaka.count ("Ka"):
            ka = ka + 1
        if reservacarro.count ("True") and plaka.count ("Onix"):
            onix = onix + 1
        if reservacarro.count ("True") and plaka.count ("Logan"):
            logan = logan + 1
        if reservacarro.count ("True") and plaka.count ("Corolla"):
            corolla = corolla + 1
    else:
        break

print(uno)
print(ducato)
print(prisma)
print(kam)
print(gol)
print(civic)
print(sprinter)
print(spin)
print(sandero)
print(ka)
print(onix)
print(logan)
print(corolla)


##Quantidade de veiculos por ano de fabricação##


file.seek(0)
l = 0
uno_2017 = 0
ducato_2017 = 0
prisma_2017 = 0
kam_2017 = 0
gol_2017 = 0
civic_2017 = 0
sprinter_2017 = 0
spin_2017 = 0
sandero_2017 = 0
ka_2017 = 0
onix_2017 = 0
logan_2017 = 0
corolla_2017 = 0


lista = []
line=file.readline()
while (line != ""):
    l += 1
    y = file.readline ()
    lista = y.split("\t")
    if (l < 20001):
        plaka = lista[2]
        reservacarro = lista[O DO ANO]
        if reservacarro.count ("True") and plaka.count ("Uno") :
            uno_2017 = uno_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Ducato"):
            ducato_2017 = ducato_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Prisma"):
            prisma_2017 = prisma_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Ka+"):
            kam_2017 = kam_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Gol"):
            gol_2017 = gol_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Civic"):
            civic_2017 = civic_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Sprinter"):
            sprinter_2017 = sprinter_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Spin"):
            spin_2017 = spin_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Sandero"):
            sandero_2017 = sandero_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Ka"):
            ka_2017 = ka_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Onix"):
            onix_2017 = onix_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Logan"):
            logan_2017 = logan_2017 + 1
        if reservacarro.count ("True") and plaka.count ("Corolla"):
            corolla_2017 = corolla_2017 + 1
    else:
        break


print(uno_2017)
print(ducato_2017)
print(prisma_2017)
print(kam_2017)
print(gol_2017)
print(civic_2017)
print(sprinter_2017)
print(spin_2017)
print(sandero_2017)
print(ka_2017)
print(onix_2017)
print(logan_2017)
print(corolla_2017)