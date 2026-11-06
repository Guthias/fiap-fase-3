# Eventos: situações que mudam o quadro da colônia e pedem uma reação.

EVENTOS = ["tempestade_de_areia", "vento_forte", "queda_de_temperatura"]


def tratar_evento(evento, energia):
    """Devolve a ação recomendada para o evento, usando o estado da energia."""
    if evento == "tempestade_de_areia":
        if energia["reserva"] < 50:
            return "CRÍTICO: tempestade com reserva baixa -> ativar modo econômico"
        return "ALERTA: tempestade reduz a geração solar -> usar a reserva"
    elif evento == "vento_forte":
        return "SUGESTÃO: vento forte aumenta a geração eólica -> armazenar excedente"
    elif evento == "queda_de_temperatura":
        return "ALERTA: aquecimento consome mais -> monitorar a energia"
    else:
        raise ValueError("Evento desconhecido: " + str(evento))


if __name__ == "__main__":
    energia = {"solar": 60, "eolica": 40, "reserva": 50}
    for evento in EVENTOS:
        print(evento, "->", tratar_evento(evento, energia))
    energia["reserva"] = 30
    print(tratar_evento("tempestade_de_areia", energia))