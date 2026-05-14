def apresentacao ():
    print("+----------------------------+")
    print("|                            |")
    print("| PROGRAMA PARA VERIFICAR SE |")
    print("| UM PAR DE NUMEROS NATURAIS |")
    print("| É AMIGO                    |")
    print("|                            |")
    print("|Versão 1.0 de 07/04/2026    |")
    print("|                            |")
    print("+----------------------------+")

# soma_dos_divisores: N -> N
def soma_dos_divisores (X):
    # soma os divisores de sem incluir X
    soma_dos_divisores_de_X=1
    possivel_divisor_de_X=2
    metade_de_X=X//2
    
    while possivel_divisor_de_X<=metade_de_X:
        if X%possivel_divisor_de_X==0:
            soma_dos_divisores_de_X+=possivel_divisor_de_X # soma_dos_divisores_de_X = soma_dos_divisores_de_X+possivel_divisor_de_X
        possivel_divisor_de_X+=1 # possivel_dividor_de_X = possivel_divisor_de_X+1
        
    return soma_dos_divisores_de_X
'''  
# sao_amigos: NxN -> {True,False}  
def sao_amigos (A,B):
    soma_dos_divisores_de_A=soma_dos_divisores(A)
    soma_dos_divisores_de_B=soma_dos_divisores(B)
    
    if A==soma_dos_divisores_de_B and B==soma_dos_divisores_de_A
        return True
    else:
        return False
'''    
def sao_amigos (A,B):
    if soma_dos_divisores(A)==B and soma_dos_divisores(B)==A:
        return True
    else:
        return False
'''
def sao_amigos (A,B):
    return soma_dos_divisores(A)==B and soma_dos_divisores(B)==A
'''
def resposta_s_ou_n_para_uma_pergunta (pergunta):
    chave_para_digitar_ate_acertar_ligada=True
    while chave_para_digitar_ate_acertar_ligada:
        resposta=input(pergunta)
        resposta=resposta.upper()
        # if len(resposta)!=1 or resposta not in "SN":
        # if resposta not in ["S","N"]
        if resposta!="S" and resposta!="N":
            print("Deve-se responder S ou N; tente novamente!")
        else:
            chave_para_digitar_ate_acertar_ligada=False 
            
    return resposta

# daqui para cima definimos subprogramas (que, neste caso, sao todos funcoes)
# daqui para baixo é o programa que chama tudo que foi definido acima
    
apresentacao()

chave_para_descobrir_pares_de_amigos_ate_cansar_ligada=True
while chave_para_descobrir_pares_de_amigos_ate_cansar_ligada:
    # obtendo o primeiro_numero
    chave_para_digitar_ate_acertar_ligada=True
    while chave_para_digitar_ate_acertar_ligada:
        try:
            primeiro_numero=int(input("Digite um número natural: "))
        except ValueError:
            print("Deve-se digitar um número natural; tente novamente!")
        else:
            if primeiro_numero<0:
                print("Negativos não são números naturais; tente novamente!")
            else:
                chave_para_digitar_ate_acertar_ligada=False
        
    # obtendo o segundo_numero
    chave_para_digitar_ate_acertar_ligada=True
    while chave_para_digitar_ate_acertar_ligada:
        try:
            segundo_numero=int(input("Digite OUTRO número natural: "))
        except ValueError:
            print("Deve-se digitar um número natural; tente novamente!")
        else:
            if segundo_numero<0:
                print("Negativos não são números naturais; tente novamente!")
            elif segundo_numero==primeiro_numero:
                print("Foi solicitado um OUTRO numero, nao o anteriormente digitado; tente novamente!")
            else:
                chave_para_digitar_ate_acertar_ligada=False
        
    # se a soma dos divisores de um deu igual ao outro e vice-versa diga que são amigos
    # senão, diga que não são amigos
    if sao_amigos(primeiro_numero,segundo_numero):
        print(primeiro_numero,"e",segundo_numero,"SÃO amigos!")
    else:
        print(primeiro_numero,"e",segundo_numero,"NÃO são amigos!")
        
    if resposta_s_ou_n_para_uma_pergunta("Deseja verificar se outro par de números é amigo (S/N)? ")=="N":
        chave_para_descobrir_pares_de_amigos_ate_cansar_ligada=False
        
print("PROGRAMA ENCERRADO")