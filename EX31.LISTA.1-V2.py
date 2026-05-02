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
                resultado = (temperatura * 9/5) + 32
                print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 2:  
                if temperatura < -273.15:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = temperatura + 273.15
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 3:  
                if temperatura < -273.15:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = (temperatura + 273.15) * 9/5
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 4: 
                if temperatura < -459.67:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = (temperatura - 32) * 5/9
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 5: 
                if temperatura < -459.67:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = (temperatura - 32) * 5/9 + 273.15
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 6:
                if temperatura < -459.67:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = temperatura + 459.67
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 7: 
                if temperatura < 0:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = temperatura - 273.15
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 8:
                if temperatura < 0:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = (temperatura - 273.15) * 9/5 + 32
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 9:
                if temperatura < 0:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = temperatura * 9/5
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 10: 
                if temperatura < 0:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = (temperatura - 491.67) * 5/9
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 11:
                if temperatura < 0:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = temperatura - 459.67
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            elif opcao == 12:
                if temperatura < 0:
                    print("Erro: Temperatura abaixo do zero absoluto!")
                else:
                    resultado = temperatura * 5/9
                    print(f"Temperatura convertida: {resultado:.2f}")
            
            else:
                print("Opcao invalida!")
                
        except ValueError:
            print("Erro: Digite um número válido!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()