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


def obtem_temperatura_a_ser_convertida():

    chave_para_digitar_ate_acertar_ligada = True

    while chave_para_digitar_ate_acertar_ligada:
        try:
            GrausKelvin = float(input("Quantos Graus Kelvin voce quer converter: "))
        except ValueError:
            print("\nDEVE-SE DIGITAR UM NUMERO! TENTE NOVAMENTE...\n")
        else:
            if GrausKelvin < 0:
                print("\nERRO: Nenhuma temperatura pode ser menor que 0°K\n")
            else:
                GrausCelcius = GrausKelvin - 273.15
                print("O Grau Kelvin em Celcius e igual a",
                      GrausCelcius,
                      "Graus Celcius")
                chave_para_digitar_ate_acertar_ligada = False
    return GrausCelcius

def resposta_s_ou_n_para_pergunta(pergunta):
    chave_para_digitar_ate_acertar_ligada = True
    while chave_para_digitar_ate_acertar_ligada:
        resposta = input(pergunta).upper()
        if resposta != "S" and resposta != "N":
            print("\nDEVE-SE RESPONDER S OU N!\n")
        else:
            chave_para_digitar_ate_acertar_ligada = False
    return resposta


apresentacao()
chave_para_calcular_ate_parar = True
while chave_para_calcular_ate_parar:
    numero_converter = obtem_temperatura_a_ser_convertida()
    resposta = resposta_s_ou_n_para_pergunta(
        "\nDESEJA CONVERTER MAIS TEMPERATURAS? (S/N)\n"
    )
    if resposta == "N":
        chave_para_calcular_ate_parar = False
        print("PROGRAMA ENCERRADO! OBRIGADO POR UTILIZAR MEU HUMILDE PROGRAMA :)")