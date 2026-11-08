import os
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


def executar_menu(gerenciador):
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

            case 0:
                exibir_card("Obrigado por utilizar o sistema!", "Desenvolvido Por", [
                    "Gustavo Mathias",
                    "Daniel Turatti",
                    "Clara Mei",
                    "Vinicius de Souza",
                    "Evellyn Soares",
                ])
                break

def main():
    gerenciador = GerenciadorEnergia()
    executar_menu(gerenciador)

if __name__ == "__main__":
    main()
