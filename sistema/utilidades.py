def input_numero(tipo, mensagem):
    while True:
        try:
            if tipo == "int":
                return int(input(mensagem))
            elif tipo == "float":
                return float(input(mensagem))
            else: 
                raise TypeError("Tipo de número não suportado.")
        except ValueError:
            print("Por favor, digite um número válido.")