# Regras de decisão: transformam os dados da colônia em uma ação clara.
# As regras estão em ordem de importância: a primeira que for verdadeira vence.

ENERGIA_MINIMA = 50   # abaixo disso, é preciso reduzir o consumo
CONSUMO_ALTO = 80     # a partir daqui o consumo é considerado alto


def decidir(energia, consumo, geracao=None):
    if energia < 0 or consumo < 0 or (geracao is not None and geracao < 0):
        raise ValueError("Energia, consumo e geração não podem ser negativos")

    if energia < ENERGIA_MINIMA and consumo >= CONSUMO_ALTO:
        return "MODO ECONOMIA: desligar sistemas não essenciais"
    elif energia < ENERGIA_MINIMA:
        return "ALERTA: reduzir consumo"
    elif geracao is not None and consumo > geracao:
        return "ALERTA: consumo maior que geração"
    elif geracao is not None and geracao > consumo:
        return "SUGESTÃO: armazenar energia excedente"
    else:
        return "NORMAL: operação estável"


def sistemas_no_modo_economia(sistemas, essenciais=("suporte_vida",)):
    novos = {}
    for nome in sistemas:
        novos[nome] = nome in essenciais
    return novos


if __name__ == "__main__":
    # Exemplos do enunciado, só para testar este arquivo
    print(decidir(40, 70))        # ALERTA: reduzir consumo
    print(decidir(40, 90))        # MODO ECONOMIA
    print(decidir(80, 30, 40))    # SUGESTÃO: armazenar energia excedente
    print(decidir(80, 70, 40))    # ALERTA: consumo maior que geração

    sistemas = {"suporte_vida": True, "laboratorio": True, "iluminacao": True}
    print(sistemas_no_modo_economia(sistemas))