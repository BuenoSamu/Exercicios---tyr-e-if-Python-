# validação de datas

import sys

print('Início do programa! Seja bem-vindo(a)')

# Dia
try:
    dia = int(input('Digite o dia: '))
except ValueError:
    print('Erro: a entrada não é um dia válido')
    sys.exit("Programa encerrado!")

if dia < 1 or dia > 31:
    print('Não existe dia menor que 1 ou maior que 31')
    sys.exit("Programa encerrado!")

print(f'Você definiu o dia como {dia}.')

# Mês
try:
    mes = int(input('Digite o mês: '))
except ValueError:
    print('Erro: a entrada não é um mês válido')
    sys.exit("Programa encerrado!")

if mes < 1 or mes > 12:
    print('Não existe mês menor que 1 ou maior que 12')
    sys.exit("Programa encerrado!")

if mes == 2 and dia > 29:
    print("Fevereiro só aceita até 29 dias")
    sys.exit("Programa encerrado!")

print(f'Você definiu o mês como {mes}.')

# Ano
try:
    ano = int(input('Digite o ano: '))
except ValueError:
    print('Erro: a entrada não é um ano válido')
    sys.exit("Programa encerrado!")

if ano <= -45:
    print('Ano inválido (antes de 45 a.C)')
    sys.exit("Programa encerrado!")

print(f'Você definiu o ano como {ano}.')

# Ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")

print(f'Sua data: {dia}/{mes}/{ano} é VÁLIDA')