def apresentacao ():
    print("+----------------------------+")
    print("|                            |")
    print("| PROGRAMA PARA ESCREVER NA  |")
    print("| TELA O CONTORNO DE UM      |")
    print("| TRIANGULO                  |")
    print("|                            |")
    print("|Versão 1.0 de 13/04/2026    |")
    print("|                            |")
    print("+----------------------------+")

def obtem_quantidade_de_linhas ():
    chave_para_digitar_ate_acertar_ligada=True
    while chave_para_digitar_ate_acertar_ligada:
        try:
            qtd=int(input("Deseja um triângulo com quantas linhas? "))
        except ValueError:
            print("Deve-se digitar um numero inteiro maior do que 1; tente novamente!")
        else:
            if qtd<=1:
                print("Deve-se digitar um numero inteiro maior do que 1; tente novamente!")
            else:
                chave_para_digitar_ate_acertar_ligada=False
    return qtd

def  escreva (qual_caractere, qts_vezes, salta_linha=True):
    chars_escritos=0
    while chars_escritos<qts_vezes:
        print(qual_caractere,end="")
        chars_escritos+=1
        
    if salta_linha: print()
    
def triangulo (qts_linhas):
    qtd_esps_inic=qts_linhas-1
    
    escreva(qual_caractere=" ",qts_vezes=qtd_esps_inic,salta_linha=False)
    print("O")
    qtd_esps_inic-=1
    
    qtd_esps_meio=1
    linhas_escritas=1
    while linhas_escritas<qts_linhas-1:
        escreva(qual_caractere=" ",qts_vezes=qtd_esps_inic,salta_linha=False)
        print("O",end="")
        escreva(qual_caractere=" ",qts_vezes=qtd_esps_meio,salta_linha=False)
        print("O")
        linhas_escritas+=1
        qtd_esps_inic-=1
        qtd_esps_meio+=2
        
    escreva(qual_caractere="O",qts_vezes=2*qts_linhas-1)

def resposta_s_ou_n_para_pergunta (pergunta):
    chave_para_digitar_ate_acertar_ligada=True
    while chave_para_digitar_ate_acertar_ligada:
        resposta=input(pergunta).upper()
        if resposta!="S" and resposta!="N":
            print("Deve-se responder S ou N; tente novamente!")
        else:
            chave_para_digitar_ate_acertar_ligada=False
    return resposta
apresentacao()
chave_para_desenhar_ate_cansar_ligada=True
while chave_para_desenhar_ate_cansar_ligada:
    qts_linhas=obtem_quantidade_de_linhas()
    triangulo(qts_linhas)
    resposta=resposta_s_ou_n_para_pergunta("Deseja desenhar mais triângulos (S/N)? ")
    if resposta=="N": chave_para_desenhar_ate_cansar_ligada=False





