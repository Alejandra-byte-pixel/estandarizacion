def estandarizar(cadena):
    palabras = cadena.split()
    ADDRESS = " ".join(palabras)
    ADDR_LINE_ONE = " ".join(palabras[:-2])
    ADDR_LINE_TWO = palabras[-2]
    ADDR_LINE_THREE = "si"
    result = [ADDRESS, ADDR_LINE_ONE, ADDR_LINE_TWO, ADDR_LINE_THREE]
    print(f"Resultado: {result}")
    return result
