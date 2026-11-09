historico = {
    "energia": {
        "solar": [55, 58, 60, 57, 52, 50, 56, 60],      # geração solar
        "eolica": [21, 25, 29, 22, 28, 35, 32, 40],     # geração eólica
    },
    "clima": {
        "vento": [8, 10, 12, 9, 11, 14, 13, 16],        # velocidade do vento (m/s)
        "temperatura_externa": [22, 20, 18, 21, 19, 15, 17, 16],
    },
    "consumo": {
        "total": [75, 78, 80, 76, 78, 82, 85, 85],      # consumo total da colônia
    },
}


def registrar_dia(solar, eolica, vento, consumo, temperatura_externa):
    """Adiciona as leituras de um novo dia ao histórico.

    Confere tudo antes de gravar: se algum valor for inválido, nada é alterado.
    """
    for nome, valor in (("solar", solar), ("eólica", eolica),
                        ("vento", vento), ("consumo", consumo)):
        if valor < 0:
            raise ValueError(f"O valor de {nome} não pode ser negativo")

    historico["energia"]["solar"].append(solar)
    historico["energia"]["eolica"].append(eolica)
    historico["clima"]["vento"].append(vento)
    historico["clima"]["temperatura_externa"].append(temperatura_externa)
    historico["consumo"]["total"].append(consumo)


if __name__ == "__main__":
    from previsao.regressao import ajustar_reta, prever

    vento = historico["clima"]["vento"]
    eolica = historico["energia"]["eolica"]
    intercepto, inclinacao = ajustar_reta(vento, eolica)
    print(f"Reta: eólica = {intercepto:.2f} + {inclinacao:.2f} * vento")
    print(f"Vento 11 -> eólica prevista = {prever(intercepto, inclinacao, 11):.1f}")