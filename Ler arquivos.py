file = open ("veiculos.txt", "r")

##Quantidade de veiculos cadastados##    OK
file.seek(0)
x=len(file.readlines())
print('Veículos cadastrados:',x-1)

##Quantidade de veiculos disponiveis##     OK
file.seek(0)
i=1
reservados = 0
while i < x+1:
    y = file.readline (i)
    reservados = reservados + y.count ("False")
    i += 1
print ('Veículos disponíveis:' ,reservados)

## Quantos Corollas? ##     OK
file.seek(0)
j=1
corollas = 0
while j < x+1:
    y = file.readline (j)
    if y.count ("False") and y.count ("Corolla"): 
        corollas += 1 
    j += 1
print ('Corollas disponíveis:',corollas)

##Quantos carros de 2017?##       ok   
file.seek(0)
k=1
ano = 0
while k < x+1:
    y = file.readline (k)
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