texto = "abbcccddeeeffgg"

def maiorsequencia(texto):

    i = 0 
    atual = 1
    maior = 1

    while i < len(texto) - 1: 

        if texto[i] == texto[i + 1]:
            atual +=1 
        else:
            atual = 1

        if atual > maior:
            maior = atual
        
        i += 1

    return maior

print(maiorsequencia("abbcccddeeeffgg"))