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
        if y.count ("True") and y.count ("Uno") :
            uno = uno + 1
        if y.count ("True") and y.count ("Ducato"):
            ducato = ducato + 1
        if y.count ("True") and y.count ("Prisma"):
            prisma = prisma + 1
        if y.count ("True") and y.count ("Ka+"):
            kam = kam + 1
        if y.count ("True") and y.count ("Gol"):
            gol = gol + 1
        if y.count ("True") and y.count ("Civic"):
            civic = civic + 1
        if y.count ("True") and y.count ("Sprinter"):
            sprinter = sprinter + 1
        if y.count ("True") and y.count ("Spin"):
            spin = spin + 1
        if y.count ("True") and y.count ("Sandero"):
            sandero = sandero + 1
        if y.count ("True") and y.count ("Ka"):
            ka = ka + 1
        if y.count ("True") and y.count ("Onix"):
            onix = onix + 1
        if y.count ("True") and y.count ("Logan"):
            logan = logan + 1
        if y.count ("True") and y.count ("Corolla"):
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


