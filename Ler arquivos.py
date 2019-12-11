from matplotlib import pyplot

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
control=0
corollas = 0
while j < x+1:
    y = file.readline ()
    control = y.count ("False") + y.count ("Corolla")
    if control == 2: 
        corollas += 1 
    j += 1
print ('Corollas disponíveis:',corollas)

##Quantos carros de 2017?##        
file.seek(0)
k=1
ano = 0
lista = []
while k < x+1:
    y = file.readline ()
    lista = y.split("\t")
    ano = ano + lista[5].count ("2017")
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
print ('Quantidade de veículos que não iniciam a placa com a letra P:' ,placa)

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

tipos = ["carro","utilitário","van"]
quantidade = [carro,ute,van]

pyplot.figure(1)
pyplot.bar(tipos,quantidade)
pyplot.ylabel("Quantidade")
pyplot.title("Quantidades de cada tipo de veículo")
pyplot.savefig('tipo carro.jpg')



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

control = 0
lista = []
line=file.readline()
while (line != ""):
    l += 1
    y = file.readline ()
    lista = y.split("\t")
    if (l < 20001):
        plaka = lista[2]
        reservacarro = lista[9]
        control = reservacarro.count ("True")
        if control == 1:
            if plaka == "Uno" :
                uno = uno + 1
            if plaka == "Ducato":
                ducato = ducato + 1
            if plaka == "Prisma":
                prisma = prisma + 1
            if plaka == "Ka+":
                kam = kam + 1
            if plaka == "Gol":
                gol = gol + 1
            if plaka == "Civic":
                civic = civic + 1
            if plaka == "Sprinter":
                sprinter = sprinter + 1
            if plaka == "Spin":
                spin = spin + 1
            if plaka == "Sandero":
                sandero = sandero + 1
            if plaka == "Ka":
                ka = ka + 1
            if plaka == "Onix":
                onix = onix + 1
            if plaka == "Logan":
                logan = logan + 1
            if plaka == "Corolla":
                corolla = corolla + 1
    else:
        break

#print(uno)
#print(ducato)
#print(prisma)
#print(kam)
#print(gol)
#print(civic)
#print(sprinter)
#print(spin)
#print(sandero)
#print(ka)
#print(onix)
#print(logan)
#print(corolla)

tipos = ["uno","Ducato","Prisma","Ka+","Gol","Civic","Sprinter","Spin","Sandero","Ka","Onix","Logan","Corolla"]
quantidade = [uno,ducato,prisma,kam,gol,civic,sprinter,spin,sandero,ka,onix,logan,corolla]

pyplot.figure(2)
pyplot.bar(tipos,quantidade)
pyplot.ylabel("Quantidade")
pyplot.title("Quantidades de veículos reservados por modelo")
pyplot.savefig('reservados por modelo.jpg')

##Quantidade de veiculos por ano de fabricação##


file.seek(0)
l = 0
carro_2017 = 0
carro_2016 = 0
carro_2015 = 0
carro_2014 = 0


l = 0
lista = []
line=file.readline()
while (line != ""):
    l += 1
    y = file.readline ()
    lista = y.split("\t")
    if (l < 20001):
        if lista[5] == "2014":
            carro_2014 += 1
        if lista[5] == "2015":
            carro_2015 += 1
        if lista[5] == "2016":
            carro_2016 += 1
        if lista[5] == "2017":
            carro_2017 += 1
    else:
        break

#print(carro_2014)
#print(carro_2015)
#print(carro_2016)
#print(carro_2017)


tipos = ["2014","2015","2016","2017"]
quantidade = [carro_2014,carro_2015,carro_2016,carro_2017]


pyplot.figure(3)
pyplot.bar(tipos,quantidade)
pyplot.ylabel("Quantidade")
pyplot.title("Quantidades veículos por ano de fabricação")
pyplot.savefig('tipo carro por ano.jpg')


##Média da autonomia por ano de fabricação em carros##


file.seek(0)
l = 0
lista_2014 = []
lista_2015 = []
lista_2016 = []
lista_2017 = []
media_2014 = 0
media_2015 = 0
media_2016 = 0
media_2017 = 0


######autonomia = lista[4]
l = 0
lista = []
line=file.readline()
while (line != ""):
    l += 1
    y = file.readline ()
    lista = y.split("\t")
    if (l < 20001):
        if lista[0] == "carro":
            if lista[5] == "2014":
                lista_2014.append(float(lista[4]))
            if lista[5] == "2015":
                lista_2015.append(float(lista[4]))
                media_2015 = media_2015 + float(lista[4])
            if lista[5] == "2016":
                lista_2016.append(float(lista[4]))
            if lista[5] == "2017":
                lista_2017.append(float(lista[4]))
    else:
        break

media_2014 = sum(lista_2014) / len(lista_2014)
media_2015 = sum(lista_2015) / len(lista_2015)
media_2016 = sum(lista_2016) / len(lista_2016)
media_2017 = sum(lista_2017) / len(lista_2017)

#print(media_2014)
#print(media_2015)
#print(media_2016)
#print(media_2017)

tipos = ["2014","2015","2016","2017"]
quantidade = [media_2014,media_2015,media_2016,media_2017]


pyplot.figure(4)
pyplot.bar(tipos,quantidade)
pyplot.ylabel("Média")
pyplot.title("Média de autonomia por ano de fabricação, para carros")
pyplot.savefig('media por ano defabricação.jpg')


## tem q dar um pip intall pillow pra pegar jpg##
pyplot.show()
#pyplot.savefig('image.jpg')


