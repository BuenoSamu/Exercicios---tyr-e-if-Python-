print("PROGRAMA PARA CALCULAR RAIZES DE EQUACOES DE 2º GRAU\n")

try:
    a=float(input('Coeficiente "a"? '))
except ValueError:
    print("Coeficientes de uma equacao de 2º grau devem ser numericos!")
else:
    if a==0:
        print('Equacoes de 2º grau nao podem ter o coeficiente "a" igual a 0')
    else:
        try:
            b=float(input('Coeficiente "b"? '))
        except ValueError:
            print("Coeficientes de uma equacao de 2º grau devem ser numericos!")
        else:
            try:
                c=float(input('Coeficiente "c"? '))
            except ValueError:
                print("Coeficientes de uma equacao de 2º grau devem ser numericos!")
            else:
                delta=b**2-4*a*c

                if delta<0:
                    print("Equacao sem raizes reais!")
                elif delta==0:
                    x=-b/(2*a)
                    print("Equacao com uma raiz que vale",x)
                else: # delta>0
                    x1=(-b-delta**0.5)/(2*a)
                    x2=(-b+delta**0.5)/(2*a)
                    print("Equacao com duas raize que valem",x1,"e",x2)

print("\nPROGRAMA ENCERRADO!")
