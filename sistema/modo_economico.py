from dados.dados import colonia


def verificar_dados(colonia):
    if colonia["energia"]["solar"] < 30:
        print(f"Atenção: Nível de energia solar está baixo ({colonia['energia']['solar']}%).")
    else:
        print(f"Nível de energia solar está dentro da faixa segura ({colonia['energia']['solar']}%).")

    if colonia["energia"]["eolica"] < 20:
        print(f"Atenção: Nível de energia eólica está baixo ({colonia['energia']['eolica']}%).")
    else:
        print(f"Nível de energia eólica está dentro da faixa segura ({colonia['energia']['eolica']}%).")

    if colonia["combustivel"]["gasolina"] < 10:
        print(f"Atenção: Nível de combustível está baixo ({colonia['combustivel']['gasolina']}%).")
    else:
        print(f"Nível de combustível está dentro da faixa segura ({colonia['combustivel']['gasolina']}%).")

    if colonia["clima"]["temperatura_interna"][0] < 10 or colonia["clima"]["temperatura_interna"][1] > 45:
        print(f"Atenção: Temperatura interna fora da faixa segura ({colonia['clima']['temperatura_interna'][0]}°C  - {colonia['clima']['temperatura_interna'][1]}°C).")
    else:
        print(f"Temperatura interna está dentro da faixa segura ({colonia['clima']['temperatura_interna'][0]}°C  - {colonia['clima']['temperatura_interna'][1]}°C).")

    if colonia["clima"]["temperatura_externa"][0] < 0 or colonia["clima"]["temperatura_externa"][1] > 50:
        print(f"Atenção: Temperatura externa fora da faixa segura ({colonia['clima']['temperatura_externa'][0]}°C - {colonia['clima']['temperatura_externa'][1]}°C).")
    else:
        print(f"Temperatura externa está dentro da faixa segura ({colonia['clima']['temperatura_externa'][0]}°C - {colonia['clima']['temperatura_externa'][1]}°C).")

    if not colonia["sistema"]["suporte_vida"]:
        print("Atenção: Sistema de suporte de vida está desligado.")
    else:
        print("Sistema de suporte de vida está ligado.")


REDUCAO = 10  # Redução de 10% nos níveis de energia e combustível
class GerenciadorEnergia:
    def __init__(self):
        self.modo_economico_ativo = False
        self.solar_antes = 0
        self.eolica_antes = 0
        self.gasolina_antes = 0

    def ativar_modo_economico(self):
        if self.modo_economico_ativo:
            print("Modo econômico já está ativado.")
            return

        self.solar_antes = colonia["energia"]["solar"]
        self.eolica_antes = colonia["energia"]["eolica"]  
        self.gasolina_antes = colonia["combustivel"]["gasolina"]

        colonia["energia"]["solar"] = max(0, self.solar_antes - REDUCAO, 0)
        colonia["energia"]["eolica"] = max(0, self.eolica_antes - REDUCAO, 0)
        colonia["combustivel"]["gasolina"] = max(0, self.gasolina_antes - REDUCAO, 0)

        self.modo_economico_ativo = True
        print("Modo econômico ativado. Níveis de energia e combustível reduzidos em 10%.")


    def desativar_modo_economico(self):
        if not self.modo_economico_ativo:
            print("O modo econômico já está desativado.")
            return

        colonia["energia"]["solar"] = self.solar_antes
        colonia["energia"]["eolica"] = self.eolica_antes
        colonia["combustivel"]["gasolina"] = self.gasolina_antes

        self.modo_economico_ativo = False
        print("Modo econômico desativado. Valores restaurados.")