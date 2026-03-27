print("PROGRAMA PARA CALCULAR A AREA DE QUADRADOS\n")

chave_para_calcular_muitas_areas_ligada = True

while chave_para_calcular_muitas_areas_ligada:
    
    # loop para digitar o lado corretamente
    chave_para_digitar_lado_ate_acertar_ligada = True
    while chave_para_digitar_lado_ate_acertar_ligada:
        try: 
            lado = float(input("Quanto mede em cm o lado? "))
        except ValueError:
            print("Medidas devem ser numericas! Tente novamente")
        else:
            if lado <= 0:
                print("Medidas devem ser numeros positivos! Tente novamente")
            else:
                chave_para_digitar_lado_ate_acertar_ligada = False
                area = lado ** 2 

    print("A area resultou", area, "centimetros quadrados\n")

    # loop para perguntar se quer continuar
    chave_para_responder = True
    while chave_para_responder:
        resposta = input("Deseja calcular a area de mais um quadrado (S/N)? ").upper()
        
        if resposta != "S" and resposta != "N":
            print("Deve-se responder S ou N. Tente novamente")
        else:
            chave_para_responder = False

    if resposta == "N":
        chave_para_calcular_muitas_areas_ligada = False

print("PROGRAMA ENCERRADO")

#usa o try puro só quando não precisa validar multiplos erros! 
#quando tiver que validar varios erros usar IF
#while = laço de repetição