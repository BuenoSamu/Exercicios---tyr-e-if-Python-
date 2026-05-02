def apresentacao():
    print("+----------------------------+")
    print("|                            |")
    print("| PROGRAMA PARA CONVERTER    |")
    print("| TEMPERATURAS               |")
    print("|                            |")
    print("|                            |")
    print("|Versão 2.0 de 28/04/2026    |")
    print("|                            |")
    print("+----------------------------+")


def obtem_temperatura_a_ser_convertida ():
    chave_para_digitar_ate_acertar_ligada = True
    while chave_para_digitar_ate_acertar_ligada:
        try:
            GrausFahrenheit = float(input("Quantos Graus Fahrenheit voce quer converter: "))
        except ValueError:
         print("\n DEVE-SE DIGITAR UM NUMERO! TENTE NOVAMENTE... ")
        else:
         if GrausFahrenheit < -459.67: print("\n ERRO: Nenhuma temperatura pode ser menor que -459,67°F")
         else:
           GrausCelcius = (GrausFahrenheit - 32) / 1.8
           print("O Grau Fahrenheit em Celcius e igual a", GrausCelcius, "Graus Celcius")
           chave_para_digitar_ate_acertar_ligada = False
    return obtem_temperatura_a_ser_convertida

def resposta_s_ou_n_para_uma_pergunta(pergunta):
   chave_para_digitar_ate_acertar_ligada = True
   while chave_para_digitar_ate_acertar_ligada:
      resposta = input(pergunta).upper()
      if resposta != "S" and resposta != "N":
         print("\n DEVE-SE RESPONDER SIM OU NÄO PARA ESSA PERGUNTA! \n")
      else: 
         chave_para_digitar_ate_acertar_ligada = False
   return resposta

apresentacao()
chave_para_calcular_ate_parar_ligada = True
while chave_para_calcular_ate_parar_ligada:
   numero_converter = obtem_temperatura_a_ser_convertida()
   resposta = resposta_s_ou_n_para_uma_pergunta ("\n DESEJA CONVERTER MAIS TEMPERATURAS? (S/N) \n", )
   if resposta == "N": chave_para_calcular_ate_parar_ligada = False
   print("PROGRAMA ENCERRADO! OBRIGADO POR UTILIZAR MEU HUMILDE PROGRAMA :)")