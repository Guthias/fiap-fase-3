# Navegação pela hierarquia da colônia.

def mostrar_hierarquia(no, nivel=0):
    """Mostra a hierarquia completa (função recursiva).

    Se o valor é outro dicionário, mostra o nome e chama a si mesma para os filhos.
    Se não é, chegou ao fim do ramo (caso-base) e mostra o valor.
    """
    for chave in no:
        valor = no[chave]
        if isinstance(valor, dict):
            print("  " * nivel + "- " + chave)
            mostrar_hierarquia(valor, nivel + 1)
        else:
            print("  " * nivel + f"- {chave}: {valor}")


def buscar_valor(no, caminho):
    """Navega por um caminho como 'colonia/energia/solar'.

    Devolve o valor encontrado ou None se o caminho não existir.
    """
    atual = no
    for chave in caminho.strip().strip("/").split("/"):
        if not isinstance(atual, dict) or chave not in atual:
            return None
        atual = atual[chave]
    return atual


if __name__ == "__main__":
    exemplo = {"energia": {"solar": 60, "eolica": 40}, "sistema": {"suporte_vida": True}}
    mostrar_hierarquia(exemplo)
    print(buscar_valor(exemplo, "energia/solar"))      # 60
    print(buscar_valor(exemplo, "energia/nuclear"))    # None