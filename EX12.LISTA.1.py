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

def obtem_a_temperatura_a_ser_convertida():
    chave_pra_digitar_ate_acertar = True
    while chave_pra_digitar_ate_acertar:
        try:
            GrausRankine = float(input("\n Digite a temperatura que voce deseja converter: \n"))
        except ValueError:
            print("\n DEVE-SE DIGITAR UM NUMERO! TENTE NOVAMENTE...\n")
        else: 
            if GrausRankine < 0: print("\n ERRO: Nenhuma temperatura pode ser menor que 0°Ra \n")
            else: 
                GrausKelvin = GrausRankine / 1.8
                print("\n A temperatura em Rankine convertida em Kelvin é igual a: ", GrausKelvin)
                chave_pra_digitar_ate_acertar = False
    return GrausRankine

def resposta_s_ou_n_para_pergunta(pergunta):
    chave_pra_digitar_ate_acertar = True
    while chave_pra_digitar_ate_acertar:
        resposta = input(pergunta).upper()
        if resposta != "S" and resposta != "N":
            print("\n DEVE-SE RESPONDER S OU N! \n")
        else: 
            chave_pra_digitar_ate_acertar = False
    return resposta

apresentacao()
chave_para_calcular_temperatura_dnv = True
while chave_para_calcular_temperatura_dnv:
    numero_converter = obtem_a_temperatura_a_ser_convertida()
    resposta = resposta_s_ou_n_para_pergunta("\n QUER CONVERTER OUTRA TEMPERATURA? (S/N) \n")
    if resposta == "N":
        chave_para_calcular_ate_parar = False
        print("\n PROGRAMA ENCERRADO! OBRIGADO POR UTILIZAR MEU HUMILDE PROGRAMA :) \n")
