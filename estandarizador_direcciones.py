import estandarizador_escenario_1
import estandarizador_escenario2
import re

def estandarizar(cadena):

    resultado = [cadena,'','','']
    diccionario_escenario_1 = estandarizador_escenario_1.estandarizar_direccion(cadena)
    lista_componentes_escenario_1 = [
                        diccionario_escenario_1["TipoVia"],
                        diccionario_escenario_1["ViaPrincipal"],
                        diccionario_escenario_1["LetraViaPrincipal"],
                        diccionario_escenario_1["Prefijo"],
                        diccionario_escenario_1["LetraPrefijo"],
                        diccionario_escenario_1["Cuadrante"],
                        diccionario_escenario_1["NumeroViaGeneradora"],
                        diccionario_escenario_1["LetraViaGeneradora"],
                        diccionario_escenario_1["Sufijo"],
                        diccionario_escenario_1["LetraSufijo"],
                        diccionario_escenario_1["NumeroPlaca"],
                        diccionario_escenario_1["CuadranteAdicional"]
    ]

    addr_line_one = ' '.join(lista_componentes_escenario_1)
    addr_line_one_trf = re.sub(r'\s+', ' ', addr_line_one)
    resultado[1] = addr_line_one_trf

    diccionario_escenario_2 = estandarizador_escenario2.estandarizar_direccion(diccionario_escenario_1["UnhandledData"])
    lista_componentes_escenario_2 = [
        diccionario_escenario_2["Manzana"],
        diccionario_escenario_2["TipoPredio"],
        diccionario_escenario_2["Casa"],
        diccionario_escenario_2["TipoPiso"],
        diccionario_escenario_2["Urbanizacion"],
        diccionario_escenario_2["NombreUrbanizacion"]
    ]

    addr_line_two = ' '.join(lista_componentes_escenario_2)
    addr_line_two_trf = re.sub(r'\s+', ' ', addr_line_two)
    resultado[2] = addr_line_two_trf

    #String 3
    resultado[3] = diccionario_escenario_2["UnhandledData"]







    return resultado

