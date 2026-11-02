import time

def menu():
    print("Bem vindo ao sistema de navegação!")
    print("Escolha uma opção:")
    print("1. Verificar energia")
    print("2. Verificar combustível")
    print("3. Verificar dados")
    print("4. Verificar sistema de decisão")
    print("5. Sair")


def main():
    while True:
        menu()
        try:
            opcao = int(input("Digite a opção desejada: "))

            match opcao:
                case 1:
                    ...
                case 2:
                    ...
                case 3:
                    ...
                case 4:
                    ...
                case 5:
                    print("Saindo do sistema...")
                    time.sleep(3)
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()