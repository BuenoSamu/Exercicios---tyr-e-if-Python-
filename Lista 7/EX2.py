frase = "eu sou um medico e sou otorinolaringnologista"


def tamanhodamaiorpalavradeumafrase(frase): 
    i = 0 
    tamanhomaior = 0 
    iniciopalavra = 0 

    while i < len(frase): 

        if frase[i] == " ": 
            palavra = frase[iniciopalavra:i]

            if len(palavra) > tamanhomaior:
                tamanhomaior = len(palavra)

            iniciopalavra = i + 1

        i += 1
        
    ultimapalavra = frase[iniciopalavra:]

    if len(ultimapalavra) > tamanhomaior:
        tamanhomaior = len(ultimapalavra)

    return tamanhomaior


print(tamanhodamaiorpalavradeumafrase("eu sou um medico e sou otorinolaringnologista"))
