print("Códigos de produtos:")
print("1 - Pizza de Frango")
print("2 - Pizza de Calabresa")
print("3 - Pizza de Queijo")
print("4 - Refrigerante")
print("5 - Água")
print("6 - Suco")
print("0 - Sair")

codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1:
        print("Você escolheu: Pizza de Frango")
    case 2:
        print("Você escolheu: Pizza de Calabresa")
    case 3:
        print("Você escolheu: Pizza de Queijo")
    case 4:
        print("Você escolheu: Refrigerante")
    case 5:
        print("Você escolheu: Água")
    case 6:
        print("Você escolheu: Suco")
    case 0:
        print("Saindo...")
    case _:
        print("INVALIDO")