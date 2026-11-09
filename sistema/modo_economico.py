from dados.dados import colonia
from dados.limite import limite
from sistema.decisao import sistemas_no_modo_economia


def verificar_dados(colonia):
    # Os valores de comparação vêm do dicionário "limite" (dados/limite.py)
    if colonia["energia"]["solar"] < limite["energia"]["solar"]:
        print(f"Atenção: Nível de energia solar está baixo ({colonia['energia']['solar']}%).")
    else:
        print(f"Nível de energia solar está dentro da faixa segura ({colonia['energia']['solar']}%).")

    if colonia["energia"]["eolica"] < limite["energia"]["eolica"]:
        print(f"Atenção: Nível de energia eólica está baixo ({colonia['energia']['eolica']}%).")
    else:
        print(f"Nível de energia eólica está dentro da faixa segura ({colonia['energia']['eolica']}%).")

    if colonia["combustivel"]["gasolina"] < limite["combustivel"]["gasolina"]:
        print(f"Atenção: Nível de combustível está baixo ({colonia['combustivel']['gasolina']}%).")
    else:
        print(f"Nível de combustível está dentro da faixa segura ({colonia['combustivel']['gasolina']}%).")

    interna = colonia["clima"]["temperatura_interna"]
    limite_interna = limite["clima"]["temperatura_interna"]
    if interna[0] < limite_interna[0] or interna[1] > limite_interna[1]:
        print(f"Atenção: Temperatura interna fora da faixa segura ({interna[0]}°C - {interna[1]}°C).")
    else:
        print(f"Temperatura interna está dentro da faixa segura ({interna[0]}°C - {interna[1]}°C).")

    externa = colonia["clima"]["temperatura_externa"]
    limite_externa = limite["clima"]["temperatura_externa"]
    if externa[0] < limite_externa[0] or externa[1] > limite_externa[1]:
        print(f"Atenção: Temperatura externa fora da faixa segura ({externa[0]}°C - {externa[1]}°C).")
    else:
        print(f"Temperatura externa está dentro da faixa segura ({externa[0]}°C - {externa[1]}°C).")

    if not colonia["sistema"]["suporte_vida"]:
        print("Atenção: Sistema de suporte de vida está desligado.")
    else:
        print("Sistema de suporte de vida está ligado.")

    if not colonia["sistema"]["laboratorio"]:
        print("Atenção: Sistema de laboratorio está desligado.")
    else:
        print("Sistema de laboratorio está ligado.")

    if not colonia["sistema"]["iluminacao"]:
        print("Atenção: Sistema de iluminacao está desligado.")
    else:
        print("Sistema de iluminacao está ligado.")


class GerenciadorEnergia:
    """Modo econômico: desliga os sistemas não essenciais para reduzir o consumo.

    Só o suporte à vida continua ligado. Ao desativar, o estado anterior é restaurado.
    """

    def __init__(self):
        self.modo_economico_ativo = False
        self.sistemas_antes = {}

    def ativar_modo_economico(self):
        if self.modo_economico_ativo:
            print("Modo econômico já está ativado.")
            return

        self.sistemas_antes = dict(colonia["sistema"])
        novos = sistemas_no_modo_economia(colonia["sistema"])
        for nome in novos:
            colonia["sistema"][nome] = novos[nome]

        self.modo_economico_ativo = True
        print("Modo econômico ativado. Sistemas não essenciais desligados.")

    def desativar_modo_economico(self):
        if not self.modo_economico_ativo:
            print("O modo econômico já está desativado.")
            return

        for nome in self.sistemas_antes:
            colonia["sistema"][nome] = self.sistemas_antes[nome]

        self.modo_economico_ativo = False
        print("Modo econômico desativado. Sistemas restaurados.")
