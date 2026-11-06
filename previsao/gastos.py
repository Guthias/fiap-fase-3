# Análise de gastos de energia: quanto cada sistema consome e como está
# o balanço entre geração e consumo.
from dados.consumo import consumo_sistemas, consumo_atual, geracao_atual
from sistema.energia import analisar_energia


def maior_consumidor(sistemas):
    """Devolve (nome, consumo) do sistema LIGADO que mais consome."""
    maior_nome = None
    maior_valor = 0
    for nome in sistemas:
        if sistemas[nome] and nome in consumo_sistemas:
            if consumo_sistemas[nome] > maior_valor:
                maior_nome = nome
                maior_valor = consumo_sistemas[nome]
    return maior_nome, maior_valor


def analisar_gastos(energia, sistemas):
    """Monta um resumo com geração, consumo, saldo e o parecer da análise."""
    geracao = geracao_atual(energia)
    consumo = consumo_atual(sistemas)
    return {
        "geracao": geracao,
        "consumo": consumo,
        "saldo": geracao - consumo,
        "parecer": analisar_energia(geracao, consumo),
        "maior_consumidor": maior_consumidor(sistemas),
    }


if __name__ == "__main__":
    energia = {"solar": 60, "eolica": 40, "reserva": 50}
    sistemas = {"suporte_vida": True, "laboratorio": True, "iluminacao": True}
    print(analisar_gastos(energia, sistemas))
    sistemas["laboratorio"] = False
    print(analisar_gastos(energia, sistemas))