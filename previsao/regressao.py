#Previsão com regressão linear simples.

def media(valores):
    # Média de uma lista de números.
    if len(valores) == 0:
        raise ValueError("A lista está vazia: não dá para calcular a média.")
    return sum(valores) / len(valores)


def ajustar_reta(x, y):
    # Calcula a reta que melhor representa os dados (mínimos quadrados).
    # x -> lista com a variável que explica (ex.: vento)
    # y -> lista com a variável que queremos prever (ex.: energia)
    # Devolve (intercepto, inclinacao).
    
    if len(x) != len(y):
        raise ValueError("As listas x e y precisam ter o mesmo tamanho.")
    if len(x) < 2:
        raise ValueError("É preciso ter pelo menos 2 pontos para ajustar uma reta.")

    media_x = media(x)
    media_y = media(y)

    numerador = 0
    denominador = 0
    for i in range(len(x)):
        numerador += (x[i] - media_x) * (y[i] - media_y)
        denominador += (x[i] - media_x) ** 2

    if denominador == 0:
        raise ValueError("Todos os valores de x são iguais: não dá para ajustar uma reta.")

    inclinacao = numerador / denominador
    intercepto = media_y - inclinacao * media_x
    return intercepto, inclinacao


def prever(intercepto, inclinacao, x_novo):
    # Usa a reta para estimar o valor de y para um x novo.
    return intercepto + inclinacao * x_novo


if __name__ == "__main__":
    # Exemplo do enunciado: vento (m/s) e energia gerada
    vento = [8, 10, 12]
    energia = [20, 25, 30]

    intercepto, inclinacao = ajustar_reta(vento, energia)
    print(f"Reta: energia = {intercepto:.2f} + {inclinacao:.2f} * vento")

    vento_novo = 11
    previsao = prever(intercepto, inclinacao, vento_novo)
    print(f"Vento = {vento_novo} -> previsão de energia = {previsao:.1f}")