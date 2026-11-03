import time
from sistema.modo_economico import verificar_dados, GerenciadorEnergia
def menu():
    print("Bem vindo ao sistema de navegação!")
    print("Escolha uma opção:")
    print("1.")
    print("2.")
    print("3. Verificar dados")
    print("4. Verificar sistema de decisão")
    print("5. Modo econômico")
    print("6.")
    print("7.")
    print("8.")
    print("9.")
    print("10.")
    print("0. Sair")


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
                    verificar_dados()
                case 4:
                    ...
                case 5:
                    gerenciador = GerenciadorEnergia()
                    print("1. Ativar modo econômico")
                    print("2. Desativar modo econômico")
                    sub_opcao = int(input("Digite a opção desejada: "))
                    if sub_opcao == 1:
                        gerenciador.ativar_modo_economico()
                    elif sub_opcao == 2:
                        gerenciador.desativar_modo_economico()
                    else:
                        print("Opção inválida. Tente novamente.")
                case 6:
                    ...
                case 0:
                    print("Saindo do sistema...")
                    time.sleep(3)
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()