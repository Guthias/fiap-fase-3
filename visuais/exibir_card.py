import os
import subprocess

def limpar_tela():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def exibir_card(titulo, subtitulo, conteudo):
    limpar_tela()
    
    largura = 50
    print("\033[H\033[J", end="")
    print()
    print("╔" + "═" * largura + "╗")
    print("║" + " COLÔNIA DE MARTE".center(largura) + "║")
    print("╠" + "═" * largura + "╣")
    print("║" + titulo.center(largura) + "║")
    print("║" + subtitulo.center(largura) + "║")
    print("╠" + "═" * largura + "╣")

    for linha in conteudo:
        print("║" + linha.ljust(largura)[:largura] + "║")

    print("╚" + "═" * largura + "╝")