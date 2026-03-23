#Bibliotecas


# Definição de variáveis

temperatura = float(input("Qual a temperatura atual?"));

conversao = int(input("Escolha o modo de conversão:" \
" 1 - Celsius |"\
" 2 - Fahrenheit"));

match conversao:

    case 1: 
        temperatura_celsius = ((temperatura - 32)/1.8)
        print("A temperatura em Celsius é: ", temperatura_celsius);

    case 2:
        temperatura_fahrenheit = ((temperatura * 1.8) + 32);
        print("A temperatura em Fahrenheit é: ", temperatura_fahrenheit);

    case _:
        print("Opção inválida. Tente novamente.");