print("EXERCICIO 2")

print("DIGITE AQUI O PRIMEIRO NUMERO")
primeiro_numero = float(input())

print("DIGITE AQUI O SEGUNDO NUMERO")
segundo_numero = float(input())

print("DIGITE AQUI O TERCEIRO NUMERO")
terceiro_numero = float(input())

numeros = [primeiro_numero, segundo_numero, terceiro_numero]
numeros.sort() #O sort() serve para ordenar os elementos de uma lista em Python

print("NUMEROS EM ORDEM CRESCENTE:", numeros)