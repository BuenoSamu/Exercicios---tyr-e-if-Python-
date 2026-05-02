def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    if c < -273.15:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return c + 273.15

def celsius_para_rankine(c):
    if c < -273.15:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return (c + 273.15) * 9/5

def fahrenheit_para_celsius(f):
    if f < -459.67:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    if f < -459.67:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return (f - 32) * 5/9 + 273.15

def fahrenheit_para_rankine(f):
    if f < -459.67:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return f + 459.67

def kelvin_para_celsius(k):
    if k < 0:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return k - 273.15

def kelvin_para_fahrenheit(k):
    if k < 0:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return (k - 273.15) * 9/5 + 32

def kelvin_para_rankine(k):
    if k < 0:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return k * 9/5

def rankine_para_celsius(r):
    if r < 0:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return (r - 491.67) * 5/9

def rankine_para_fahrenheit(r):
    if r < 0:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return r - 459.67

def rankine_para_kelvin(r):
    if r < 0:
        raise ValueError("Temperatura abaixo do zero absoluto!")
    return r * 5/9

def main():
    while True:
        print("\nPROGRAMA PARA CONVERTER TEMPERATURAS")
        print("1) DE CELSIUS    PARA FAHRENHEIT")
        print("2) DE CELSIUS    PARA KELVIN")
        print("3) DE CELSIUS    PARA RANKINE")
        print("4) DE FAHRENHEIT PARA CELSIUS")
        print("5) DE FAHRENHEIT PARA KELVIN")
        print("6) DE FAHRENHEIT PARA RANKINE")
        print("7) DE KELVIN    PARA CELSIUS")
        print("8) DE KELVIN    PARA FAHRENHEIT")
        print("9) DE KELVIN    PARA RANKINE")
        print("10) DE RANKINE    PARA CELSIUS")
        print("11) DE RANKINE    PARA FAHRENHEIT")
        print("12) DE RANKINE    PARA KELVIN")
        
        try:
            opcao = int(input("\nSua opcao? "))
            
            if opcao == 0:
                break
            
            temperatura = float(input("Temperatura original: "))
            
            if opcao == 1:
                resultado = celsius_para_fahrenheit(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 2:
                resultado = celsius_para_kelvin(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 3:
                resultado = celsius_para_rankine(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 4:
                resultado = fahrenheit_para_celsius(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 5:
                resultado = fahrenheit_para_kelvin(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 6:
                resultado = fahrenheit_para_rankine(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 7:
                resultado = kelvin_para_celsius(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 8:
                resultado = kelvin_para_fahrenheit(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 9:
                resultado = kelvin_para_rankine(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 10:
                resultado = rankine_para_celsius(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 11:
                resultado = rankine_para_fahrenheit(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 12:
                resultado = rankine_para_kelvin(temperatura)
                print(f"Temperatura convertida: {resultado:.2f}")
            
            else:
                print("Opcao invalida!")
                
        except ValueError as e:
            if str(e):
                print(f"Erro: {e}")
            else:
                print("Erro: Digite um número válido!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()