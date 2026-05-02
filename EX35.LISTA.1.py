#Programa que adiciona segundos a um horário perguntado.

print('Início do programa! Seja bem-vindo(a)')


# Definir segundos
try:
    segundos = int(input('Digite os segundos: '))
except ValueError:
    print('Dígite apenas números inteiros, por favor!')

else:
    if segundos < 0 or segundos > 59 :
        print('Segundos podem ser de 0 à 59 apenas!')
    
    else:
        print(f'Você definiu segundos como {segundos}.')
   
   
# Definir minutos     
try:
    minutos  = int(input('Digite os minutos: '))
except ValueError:
    print('Dígite apenas números inteiros, por favor!')
            
else:
    if minutos < 0 or minutos > 59:
        print('Minutos podem ser de 0 à 59 apenas!')
    else:
        print(f'Você definiu minutos como {minutos}.')
                


# Definir hora
try:
    horas = int(input('Digite as horas: '))
except ValueError:
   print('Dígite apenas números inteiros, por favor!')
else:
    if horas < 0 or horas > 23:
        print('Horas podem ser de 0 à 23 apenas!')
    else:
        print(f'Você definiu o horário como: {horas}:{minutos}:{segundos}')
        
# Transformar horário completo em segundos

horas_em_segundos = horas * 3600
minutos_em_segundos = minutos * 60
horário_em_segundos = segundos + minutos_em_segundos + horas_em_segundos

try:
    adicionar_segundos = int(input('Quantos segundos você quer adicionar ao seu horário? '))
except ValueError:
    print('Digite apenas números inteiros, por favor!')


segundos_totais = horário_em_segundos + adicionar_segundos

horas_final = segundos_totais // 3600
resto_de_horas = segundos_totais % 3600

minutos_final = resto_de_horas // 60
resto_de_minutos = resto_de_horas % 60

segundos_final = resto_de_minutos

print(f'Seu novo horário é: {horas_final}:{minutos_final}:{segundos_final}')