# Consumo de energia de cada sistema da colônia.

consumo_sistemas = {
    "suporte_vida": 35,
    "laboratorio": 30,
    "iluminacao": 20,
}


def consumo_atual(sistemas):
    """Soma o consumo dos sistemas ligados (valor True no dicionário)."""
    total = 0
    for nome in sistemas:
        if sistemas[nome] and nome in consumo_sistemas:
            total += consumo_sistemas[nome]
    return total


def geracao_atual(energia):
    """Geração atual = energia solar + energia eólica."""
    return energia["solar"] + energia["eolica"]


if __name__ == "__main__":
    sistemas = {"suporte_vida": True, "laboratorio": True, "iluminacao": True}
    print("Consumo com tudo ligado:", consumo_atual(sistemas))
    sistemas["laboratorio"] = False
    print("Sem o laboratório:", consumo_atual(sistemas))