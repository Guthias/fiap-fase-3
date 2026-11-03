from dados.dados import colonia
from dados.limite import economico


def verificar_dados():
    for energia in colonia["energia"]:

        if colonia["energia"][energia] < 10:
            print(f"Atenção: Nível de energia {energia} está baixo ({colonia['energia'][energia]}%).")
        else:
            print(f"Nível de energia {energia} está dentro da faixa segura ({colonia['energia'][energia]}%).")

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

                        if colonia["sistema"]["suporte_vida"] == False:
                            print("Atenção: Sistema de suporte de vida está desligado.")
                        else:
                            print("Sistema de suporte de vida está ligado.")
class GerenciadorEnergia:
    def __init__(self):
        self.modo_economico_ativo = False

    def ativar_modo_economico(self):
        print("Ativando modo econômico...")
        for energia in colonia["energia"]:
            colonia["energia"][energia] = max(colonia["energia"][energia] - 10, 0)
        colonia["combustivel"]["gasolina"] = max(colonia["combustivel"]["gasolina"] - 10, 0)
        self.modo_economico_ativo = True
        print("Modo econômico ativado. Níveis de energia e combustível reduzidos em 10%.")

    def desativar_modo_economico(self):
        print("Desativando modo econômico...")
        for energia in colonia["energia"]:
            colonia["energia"][energia] = min(colonia["energia"][energia] + 10, 100)
        colonia["combustivel"]["gasolina"] = min(colonia["combustivel"]["gasolina"] + 10, 100)
        self.modo_economico_ativo = False
        print("Modo econômico desativado. Níveis de energia e combustível restaurados em 10%.")