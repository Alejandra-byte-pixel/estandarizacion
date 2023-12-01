def procesar_direccion(cadena):
    palabras = cadena.split()
    campo1 = " ".join(palabras)
    campo2 = " ".join(palabras[:-2])
    campo3 = palabras[-2]
    campo4 = "si"
    return [ADDRESS, ADDR_LINE_ONE, ADDR_LINE_TWO, ADDR_LINE_THREE]

