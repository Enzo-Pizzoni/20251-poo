def menu():
    while True:
        # Exibe o menu
        print("\nEscolha uma opção:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")
        
        # Solicita a escolha do usuário
        escolha = input("Digite o número da opção: ")
        
        # Verifica a opção escolhida
        if escolha == "1":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
            except ValueError:
                print("Por favor, digite apenas números válidos.")
        
        elif escolha == "2":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
            except ValueError:
                print("Por favor, digite apenas números válidos.")
        
        elif escolha == "3":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
            except ValueError:
                print("Por favor, digite apenas números válidos.")
        
        elif escolha == "4":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                if num2 == 0:
                    print("Erro: Não é possível dividir por zero.")
                else:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
            except ValueError:
                print("Por favor, digite apenas números válidos.")
        
        elif escolha == "0":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

# Chama a função menu
menu()





