print("PROGRAMA PARA ESCREVER POR EXTENSO INTEIROS ENTRE 0 E 99")

try:
    numero=int(input("Digite um inteiro entre 0 e 99: "))
except ValueError:
    print("Nao foi digitado um numero inteiro!")
else:
    if numero<0 or numero>99:
        print("Foi digitado um inteiro fora da faixa solicitada!")
    else:            
        if numero==0:
            print("zero")
        elif numero==10:
            print("dez")
        elif numero==11:
            print("onze")
        elif numero==12:
            print("doze")
        elif numero==13:
            print("treze")
        elif numero==14:
            print("quatorze")
        elif numero==15:
            print("quinze")
        elif numero==16:
            print("dezesseis")
        elif numero==17:
            print("dezessete")
        elif numero==18:
            print("dezoito")
        elif numero==19:
            print("dezenove")
        else:
            dezena=numero//10
            unidade=numero%10

            if dezena==2:
                print("vinte",end="")
            elif dezena==3:
                print("trinta",end="")
            elif dezena==4:
                print("quarenta",end="")
            elif dezena==5:
                print("cinquenta",end="")
            elif dezena==6:
                print("sessenta",end="")
            elif dezena==7:
                print("setenta",end="")
            elif dezena==8:
                print("oitenta",end="")
            elif dezena==9:
                print("noventa",end="")
    
            if dezena>=2 and unidade!=0:
                print(" e ",end="")
  
            if unidade==0:
                print()
            elif unidade==1:
                print("um")
            elif unidade==2:
                print("dois")
            elif unidade==3:
                print("tres")
            elif unidade==4:
                print("quatro")
            elif unidade==5:
                print("cinco")
            elif unidade==6:
                print("seis")
            elif unidade==7:
                print("sete")
            elif unidade==8:
                print("oito")
            elif unidade==9:
                print("nove")

print("PROGRAMA ENCERRADO!")