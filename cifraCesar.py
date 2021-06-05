print ("_____________________")
print("Cifra de César")
print("----------------------")
print(" ")

base = 'abcdefghijklmnopqrstuvwxyz'
base2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
base3 = ' '

#Opções
modo = int(input("Deseja encriptar(1) ou descriptar(2)?: "))

#insere o texto / Entrada de dados
text = input("Digite o texto para ser executado a opção desejada: \n\n")

cripto =''
if (modo == 1):
    for x in text:
        if (x == 'á' or x == 'ã' or x == 'â' or x == 'à' or x == 'Á' or x == 'Ã' or x == 'Â' or x == 'À'):
            cripto = cripto + base[3]
        elif (x == 'é' or x == 'ê' or x == 'É' or x == 'Ê'):
            cripto = cripto + base[7]
        elif (x == 'Í' or x == 'í'):
            cripto = cripto + base[11]
        elif (x == 'ó' or x == 'õ' or x == 'ô' or x == 'Ó' or x == 'Ô' or x == 'Õ'):
            cripto = cripto + base[17]
        elif (x == 'ú' or x == 'Ú'):
            cripto = cripto + base[23]
        elif (x == 'ç' or x == 'Ç'):
            cripto = cripto + base[5]

        elif x.isupper():
            posicao = base2.find(x) 
            posicao = posicao + 3
            if (posicao >= len(base)):
                posicao = posicao - len(base)
            cripto = cripto + base2[posicao]
        elif x.islower():
            posicao = base.find(x)
            posicao = posicao + 3
            if (posicao >= len(base)):
                posicao = posicao - len(base)
            cripto = cripto + base[posicao]
        elif x.isspace():
            posicao = base3.find(x)
            cripto = cripto + base3[posicao]
            
elif (modo == 2):
    for x in text:
        if x.isupper():
            posicao = base2.find(x) 
            posicao = posicao - 3
            if (posicao >= len(base)):
                posicao = posicao + (len(base) - posicao)

            cripto = cripto + base2[posicao]
        elif x.islower():
            posicao = base.find(x)
            posicao = posicao - 3
            cripto = cripto + base[posicao]
        elif x.isspace():
            posicao = base3.find(x)
            cripto = cripto + base3[posicao]

print("\nMENSAGEM FINAL: \n" + cripto)
