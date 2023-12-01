def procesar_direccion(cadena):
    palabras = cadena.split()
    ADDRESS = " ".join(palabras)
    ADDR_LINE_ONE = " ".join(palabras[:-2])
    ADDR_LINE_TWO = palabras[-2]
    ADDR_LINE_THREE = "si"
    return [ADDRESS, ADDR_LINE_ONE, ADDR_LINE_TWO, ADDR_LINE_THREE]

