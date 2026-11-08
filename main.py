import os
from time import sleep
import subprocess
from dados.dados import colonia
from sistema.modo_economico import verificar_dados, GerenciadorEnergia
from sistema.utilidades import input_numero
from visuais.exibir_card import exibir_card


def limpar_tela():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def pausa():
    input("\nPressione Enter para continuar...")


def exibir_menu():
    exibir_card(
        "Menu Principal",
        "Selecione uma opção",
        [
            "1.",
            "2.",
            "3. Verificar dados",
            "4. Verificar sistema de decisão",
            "5. Modo econômico",
            "",
            "0. Sair"
        ])


def executar_menu():
    while True:
        exibir_menu()
        opcao = input_numero("int", "Digite a opção desejada: ")

        match opcao:
            case 3:
                limpar_tela()
                verificar_dados(colonia)
                pausa()

            case 5:
                limpar_tela()
                print("1. Ativar modo econômico")
                print("2. Desativar modo econômico")
                sub_opcao = int(input("Digite a opção desejada: "))
                if sub_opcao == 1:
                    gerenciador.ativar_modo_economico()

                elif sub_opcao == 2:
                    gerenciador.desativar_modo_economico()

                else:
                    print("Opção inválida. Tente novamente.")
                pausa()

def main():
    gerenciador = GerenciadorEnergia()
    while True:
        limpar_tela()
        exibir_menu()
        pausa()
        try:
            opcao = int(input("Digite a opção desejada: "))

            match opcao:
                case 1:
                    limpar_tela()
                    print("Opção 1 selecionada.")
                    pausa()
                case 2:
                    limpar_tela()
                    print("Opção 2 selecionada.")
                    pausa()
                case 3:
                    limpar_tela()
                    verificar_dados(colonia)
                    pausa()
                case 4:
                    limpar_tela()
                    print("Opção 4 selecionada.")
                    pausa()
                case 5:
                    limpar_tela()
                    print("1. Ativar modo econômico")
                    print("2. Desativar modo econômico")
                    sub_opcao = int(input("Digite a opção desejada: "))
                    if sub_opcao == 1:
                        gerenciador.ativar_modo_economico()

                    elif sub_opcao == 2:
                        gerenciador.desativar_modo_economico()

                    else:
                        print("Opção inválida. Tente novamente.")
                    pausa()

                case 6:
                    limpar_tela()
                    print("Opção 6 selecionada.")
                    pausa()
                case 7:
                    limpar_tela()
                    print("Opção 7 selecionada.")
                    pausa()
                case 8:
                    limpar_tela()
                    print("Opção 8 selecionada.")
                    pausa()
                case 9:
                    limpar_tela()
                    print("Opção 9 selecionada.")
                    pausa()
                case 0:
                    limpar_tela()
                    print("Saindo do sistema...")
                    pausa()
                    break
                case _:
                    limpar_tela()
                    print("Opção inválida. Tente novamente.")
                    pausa()

        except ValueError:
            limpar_tela()
            print("Entrada inválida. Por favor, digite um número.")
            pausa()


if __name__ == "__main__":
    main()
