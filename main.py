import os
import subprocess
from dados.dados import colonia
from dados.historico import historico, registrar_dia
from dados.consumo import consumo_atual, geracao_atual
from dados.navegacao import mostrar_hierarquia, buscar_valor
from sistema.modo_economico import verificar_dados, GerenciadorEnergia
from sistema.decisao import decidir
from sistema.utilidades import input_numero
from previsao.regressao import ajustar_reta, prever
from previsao.gastos import analisar_gastos
from previsao.eventos import EVENTOS, tratar_evento




def pausa():
    input("\nPressione Enter para continuar...")


def ler_positivo(mensagem):
    """Lê um número decimal maior ou igual a zero."""
    while True:
        valor = input_numero("float", mensagem)
        if 0 <= valor < float("inf"):
            return valor
        print("Digite um valor maior ou igual a zero.")


def ler_opcao(mensagem, minimo, maximo):
    """Lê um número inteiro entre minimo e maximo."""
    while True:
        valor = input_numero("int", mensagem)
        if minimo <= valor <= maximo:
            return valor
        print(f"Digite um número entre {minimo} e {maximo}.")


def menu():
    print("Bem vindo ao sistema de navegação!")
    print("Escolha uma opção:")
    print("1. Ver hierarquia da colônia")
    print("2. Consultar um valor (ex: colonia/energia/solar)")
    print("3. Verificar dados")
    print("4. Verificar sistema de decisão")
    print("5. Modo econômico")
    print("6. Previsão de energia eólica (regressão)")
    print("7. Análise geração x consumo")
    print("8. Eventos da colônia")
    print("9. Registrar novo dia no histórico")
    print("0. Sair")


def mostrar_decisao():
    print("1. Usar os dados atuais da colônia")
    print("2. Digitar valores para simular")
    escolha = ler_opcao("Escolha: ", 1, 2)
    if escolha == 1:
        energia = colonia["energia"]["reserva"]
        consumo = consumo_atual(colonia["sistema"])
        geracao = geracao_atual(colonia["energia"])
    else:
        energia = ler_positivo("Energia (0 a 100): ")
        consumo = ler_positivo("Consumo: ")
        geracao = ler_positivo("Geração: ")
    print(f"Energia: {energia} | Consumo: {consumo} | Geração: {geracao}")
    print("Decisão:", decidir(energia, consumo, geracao))


def mostrar_previsao():
    vento = historico["clima"]["vento"]
    eolica = historico["energia"]["eolica"]
    intercepto, inclinacao = ajustar_reta(vento, eolica)
    print(f"Reta ajustada: eólica = {intercepto:.2f} + {inclinacao:.2f} * vento")
    novo = ler_positivo("Velocidade do vento prevista (m/s): ")
    print(f"Energia eólica prevista: {prever(intercepto, inclinacao, novo):.1f}")
    if novo < min(vento) or novo > max(vento):
        print(f"Aviso: fora da faixa observada ({min(vento)} a {max(vento)} m/s); previsão pouco confiável.")


def mostrar_gastos():
    r = analisar_gastos(colonia["energia"], colonia["sistema"])
    print(f"Geração: {r['geracao']} | Consumo: {r['consumo']} | Saldo: {r['saldo']}")
    print(r["parecer"])
    nome, valor = r["maior_consumidor"]
    if nome is not None:
        print(f"Maior consumidor: {nome} ({valor})")


def menu_eventos():
    for i in range(len(EVENTOS)):
        print(f"{i + 1}. {EVENTOS[i]}")
    escolha = ler_opcao("Escolha o evento: ", 1, len(EVENTOS))
    print(tratar_evento(EVENTOS[escolha - 1], colonia["energia"]))


def novo_dia():
    solar = ler_positivo("Energia solar do dia: ")
    eolica = ler_positivo("Energia eólica do dia: ")
    vento = ler_positivo("Vento do dia (m/s): ")
    consumo = ler_positivo("Consumo do dia: ")
    temperatura = input_numero("float", "Temperatura externa (°C): ")
    registrar_dia(solar, eolica, vento, consumo, temperatura)
    print(f"Dia registrado. Total de dias no histórico: {len(historico['clima']['vento'])}")


def main():
    gerenciador = GerenciadorEnergia()
    while True:
        menu()
        opcao = input_numero("int", "Digite a opção desejada: ")

        match opcao:
            case 1:
                mostrar_hierarquia({"colonia": colonia})
                pausa()
            case 2:
                caminho = input("Caminho: ")
                valor = buscar_valor({"colonia": colonia}, caminho)
                if valor is None:
                    print("Caminho não encontrado.")
                else:
                    print("Valor:", valor)
                pausa()
            case 3:
                verificar_dados(colonia)
                pausa()
            case 4:
                mostrar_decisao()
                pausa()
            case 5:
                print("1. Ativar modo econômico")
                print("2. Desativar modo econômico")
                sub_opcao = input_numero("int", "Digite a opção desejada: ")
                if sub_opcao == 1:
                    gerenciador.ativar_modo_economico()
                elif sub_opcao == 2:
                    gerenciador.desativar_modo_economico()
                else:
                    print("Opção inválida. Tente novamente.")
                pausa()
            case 6:
                mostrar_previsao()
                pausa()
            case 7:
                mostrar_gastos()
                pausa()
            case 8:
                menu_eventos()
                pausa()
            case 9:
                novo_dia()
                pausa()
            case 0:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                pausa()


if __name__ == "__main__":
    main()
