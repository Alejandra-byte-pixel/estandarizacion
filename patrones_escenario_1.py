import re
from itertools import product
import diccionarios_escenario_1

diccionario_Z_Full = diccionarios_escenario_1.get_z()
diccionario_T_Full = diccionarios_escenario_1.get_t()
diccionario_D = diccionarios_escenario_1.get_d()
diccionario_B = diccionarios_escenario_1.get_b()
diccionario_C = diccionarios_escenario_1.get_c()

def get_diccionario_T_mejorado(cadena):
    diccionario_T = {}
    for t,t2 in product(diccionario_T_Full.keys(),diccionario_T_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(t),re.escape(t2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_T[t] = diccionario_T_Full[t]
            diccionario_T[t2] = diccionario_T_Full[t2]

    for t in diccionario_T_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(t))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_T[t] = diccionario_T_Full[t]

    return diccionario_T

def get_diccionario_Z_mejorado(cadena):
    diccionario_Z = {}
    for z,z2 in product(diccionario_Z_Full.keys(),diccionario_Z_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(z),re.escape(z2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_Z[z] = diccionario_Z_Full[z]
            diccionario_Z[z2] = diccionario_Z_Full[z2]

    for z in diccionario_Z_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(z))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_Z[z] = diccionario_Z_Full[z]
    print(diccionario_Z)
    return diccionario_Z


def verificar_patron(cadena, patron):
    busqueda = re.search(patron, cadena)
    if busqueda:
        return busqueda.groups()
    else:
        return None


def extraer_componentes_direccion(cadena):
    componentes_direccion = {
        "TipoDireccion": "",
        "TipoVia": "",
        "ViaPrincipal": "",
        "LetraViaPrincipal": "",
        "Prefijo": "",
        "LetraPrefijo": "",
        "Cuadrante": "",
        "NumeroViaGeneradora": "",
        "LetraViaGeneradora": "",
        "Sufijo": "",
        "LetraSufijo": "",
        "NumeroPlaca": "",
        "CuadranteAdicional": "",
        "UnhandledPattern": "",
        "UnhandledData": "",
        "InputPattern": "",
        "UserOverrideFlag": "",
        "InputPattern": "",
        "LineaPatron": "",
        "DireccionEjemplo": "",
        "UnhandledData": ""
    }

    diccionario_T = get_diccionario_T_mejorado(cadena)

    if diccionario_T is None:
        return None

    diccionario_Z = get_diccionario_Z_mejorado(cadena)

    if diccionario_Z is not None:

        for T, D, D2, Z, Z2 in product(diccionario_T.keys(), diccionario_D.keys(), diccionario_D.keys(),
                                       diccionario_Z.keys(), diccionario_Z.keys()):
            patron_147 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(Z),
                re.escape(D2),
                re.escape(Z2))
            componentes_147 = verificar_patron(cadena, patron_147)
            if componentes_147 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_147[0])
                componentes_direccion["ViaPrincipal"] = componentes_147[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_147[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_147[3])
                componentes_direccion["LetraPrefijo"] = componentes_147[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_147[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_147[6]
                componentes_direccion["LetraViaGeneradora"] = componentes_147[7]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_147[8])
                componentes_direccion["LetraSufijo"] = componentes_147[9]
                componentes_direccion["NumeroPlaca"] = componentes_147[10]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_147[11])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '2833'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4 A BIS A SUR 3 A BIS A 3 ESTE'
                componentes_direccion["UnhandledData"] = componentes_147[12]
                return componentes_direccion

            patron_148 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(Z),
                re.escape(D2),
                re.escape(Z2))

            componentes_148 = verificar_patron(cadena, patron_148)
            if componentes_148 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_148[0])
                componentes_direccion["ViaPrincipal"] = componentes_148[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_148[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_148[3])
                componentes_direccion["LetraPrefijo"] = componentes_148[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_148[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_148[6]
                componentes_direccion["LetraViaGeneradora"] = componentes_148[7]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_148[8])
                componentes_direccion["NumeroPlaca"] = componentes_148[9]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_148[10])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '2862'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS E SUR 4 A BIS 78 ESTE'
                componentes_direccion["UnhandledData"] = componentes_148[11]
                return componentes_direccion

            patron_153 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z), re.escape(D2), re.escape(Z2))
            componentes_153 = verificar_patron(cadena, patron_153)
            if componentes_153 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_153[0])
                componentes_direccion["ViaPrincipal"] = componentes_153[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_153[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_153[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_153[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_153[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_153[6]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_153[7])
                componentes_direccion["LetraSufijo"] = componentes_153[8]
                componentes_direccion["NumeroPlaca"] = componentes_153[9]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_153[10])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '2981'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS SUR 4 A BIS A 3 SUR'
                componentes_direccion["UnhandledData"] = componentes_153[11]
                return componentes_direccion

            patron_154 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z), re.escape(D2), re.escape(Z2))
            componentes_154 = verificar_patron(cadena, patron_154)
            if componentes_154 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_154[0])
                componentes_direccion["ViaPrincipal"] = componentes_154[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_154[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_154[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_154[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_154[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_154[6]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_154[7])
                componentes_direccion["NumeroPlaca"] = componentes_154[8]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_154[9])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3008'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4 A BIS SUR 78 A BIS 78 ESTE'
                componentes_direccion["UnhandledData"] = componentes_154[10]
                return componentes_direccion

        for T, D, Z, Z2 in product(diccionario_T.keys(), diccionario_D.keys(), diccionario_Z.keys(), diccionario_Z.keys()):

            patron_43 = r'^({})\s+(\d{{1,3}})\s+({})\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                        re.escape(D),
                                                                                                        re.escape(Z),
                                                                                                        re.escape(Z2))
            componentes_43 = verificar_patron(cadena, patron_43)
            if componentes_43 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_43[0])
                componentes_direccion["ViaPrincipal"] = componentes_43[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_43[2])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_43[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_43[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_43[5])
                componentes_direccion["NumeroPlaca"] = componentes_43[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|Z|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '740'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 BIS SUR 47 ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_43[7]
                return componentes_direccion
            patron_58 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z), re.escape(Z2))
            componentes_58 = verificar_patron(cadena, patron_58)
            if componentes_58 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_58[0])
                componentes_direccion["ViaPrincipal"] = componentes_58[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_58[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_58[3])
                componentes_direccion["LetraPrefijo"] = componentes_58[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_58[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_58[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_58[7])
                componentes_direccion["NumeroPlaca"] = componentes_58[8]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1100'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS B SUR 45 ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_58[9]
                return componentes_direccion

            patron_61 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})$'.format(
                re.escape(T), re.escape(D), re.escape(Z), re.escape(Z2))
            componentes_61 = verificar_patron(cadena, patron_61)
            if componentes_61 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_61[0])
                componentes_direccion["ViaPrincipal"] = componentes_61[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_61[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_61[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_61[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_61[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_61[6])
                componentes_direccion["NumeroPlaca"] = componentes_61[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1165'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS SUR 45 ESTE 76'
                return componentes_direccion

            patron_64 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(Z),
                re.escape(Z2))
            componentes_64 = verificar_patron(cadena, patron_64)
            if componentes_64 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_64[0])
                componentes_direccion["ViaPrincipal"] = componentes_64[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_64[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_64[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_64[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_64[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_64[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_64[7])
                componentes_direccion["NumeroPlaca"] = componentes_64[8]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1224'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS SUR 45 A ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_64[9]
                return componentes_direccion
            patron_74 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(D), re.escape(Z2))
            componentes_74 = verificar_patron(cadena, patron_74)
            if componentes_74 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_74[0])
                componentes_direccion["ViaPrincipal"] = componentes_74[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_74[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_74[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_74[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_D.get(componentes_74[5])
                componentes_direccion["NumeroPlaca"] = diccionario_Z.get(componentes_74[6])
                componentes_direccion["UnhandledData"] = componentes_74[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1431'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A BIS ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_74[8]
                return componentes_direccion
            patron_77 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(D), re.escape(Z2))
            componentes_77 = verificar_patron(cadena, patron_77)
            if componentes_77 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_77[0])
                componentes_direccion["ViaPrincipal"] = componentes_77[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_77[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_77[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_77[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_77[5])
                componentes_direccion["LetraSufijo"] = componentes_77[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_77[7])
                componentes_direccion["NumeroPlaca"] = componentes_77[8]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1543'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A BIS B ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_77[9]
                return componentes_direccion
            patron_80 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(D), re.escape(Z2))
            componentes_80 = verificar_patron(cadena, patron_80)
            if componentes_80 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_80[0])
                componentes_direccion["ViaPrincipal"] = componentes_80[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_80[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_80[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_80[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_80[5])
                componentes_direccion["LetraSufijo"] = componentes_80[6]
                componentes_direccion["NumeroPlaca"] = componentes_80[7]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_80[8])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1608'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A BIS A 76 ESTE'
                componentes_direccion["UnhandledData"] = componentes_80[9]
                return componentes_direccion
            patron_81 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(D), re.escape(Z2))
            componentes_81 = verificar_patron(cadena, patron_81)
            if componentes_81 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_81[0])
                componentes_direccion["ViaPrincipal"] = componentes_81[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_81[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_81[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_81[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_81[5])
                componentes_direccion["NumeroPlaca"] = componentes_81[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_81[7])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1631'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A BIS 76 ESTE'
                componentes_direccion["UnhandledData"] = componentes_81[8]
                return componentes_direccion

            patron_143 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(Z),
                re.escape(Z2))
            componentes_143 = verificar_patron(cadena, patron_143)
            if componentes_143 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_143[0])
                componentes_direccion["ViaPrincipal"] = componentes_143[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_143[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_143[3])
                componentes_direccion["LetraPrefijo"] = componentes_143[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_143[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_143[6]
                componentes_direccion["NumeroPlaca"] = componentes_143[7]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_143[8])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '2733'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS A SUR 4 3 ESTE'
                componentes_direccion["UnhandledData"] = componentes_143[9]
                return componentes_direccion

            patron_144 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(Z),
                re.escape(Z2))
            componentes_144 = verificar_patron(cadena, patron_144)
            if componentes_144 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_144[0])
                componentes_direccion["ViaPrincipal"] = componentes_144[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_144[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_144[3])
                componentes_direccion["LetraPrefijo"] = componentes_144[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_144[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_144[6]
                componentes_direccion["LetraViaGeneradora"] = componentes_144[7]
                componentes_direccion["NumeroPlaca"] = componentes_144[8]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_144[9])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '2756'
                componentes_direccion["DireccionEjemplo"] = 'CARRERA 8 A BIS A SUR 4 A 6 ESTE'
                componentes_direccion["UnhandledData"] = componentes_144[10]
                return componentes_direccion

            patron_149 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z), re.escape(Z2))
            componentes_149 = verificar_patron(cadena, patron_149)
            if componentes_149 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_149[0])
                componentes_direccion["ViaPrincipal"] = componentes_149[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_149[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_149[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_149[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_149[5]
                componentes_direccion["NumeroPlaca"] = componentes_149[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_149[7])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '2889'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS SUR 4 3 ESTE'
                componentes_direccion["UnhandledData"] = componentes_149[8]
                return componentes_direccion

            patron_151 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z), re.escape(Z2))
            componentes_151 = verificar_patron(cadena, patron_151)
            if componentes_151 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_151[0])
                componentes_direccion["ViaPrincipal"] = componentes_151[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_151[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_151[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_151[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_151[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_151[6]
                componentes_direccion["NumeroPlaca"] = componentes_151[7]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_151[8])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '2933'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS SUR 4 A 3 ESTE'
                componentes_direccion["UnhandledData"] = componentes_151[9]
                return componentes_direccion

            patron_168 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z),re.escape(Z2))
            componentes_168 = verificar_patron(cadena, patron_168)
            if componentes_168 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_168[0])
                componentes_direccion["ViaPrincipal"] = componentes_168[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_168[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_168[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_168[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_168[5]
                componentes_direccion["NumeroPlaca"] = componentes_168[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_168[7])
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|Z|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3267'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 34D BIS SUR 4 6 ESTE'
                componentes_direccion["UnhandledData"] = componentes_168[8]
                return componentes_direccion

            patron_211 = r'^({})\s([A-Z]+)\s+({})\s+([A-Z]+)\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z), re.escape(D),re.escape(Z2))
            componentes_211 = verificar_patron(cadena, patron_211)
            if componentes_211 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_211[0])
                componentes_direccion["ViaPrincipal"] = componentes_211[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_211[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_211[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_211[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_211[5])
                componentes_direccion["LetraSufijo"] = componentes_211[6]
                componentes_direccion["NumeroPlaca"] = componentes_211[7]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_211[8])
                componentes_direccion["InputPattern"] = 'T|+|Z|+|+[{}len=1]|D|+[{}len=1]|+|Z'
                componentes_direccion["LineaPatron"] = '4365'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS SUR CELS A BIS R RT ESTE'
                componentes_direccion["UnhandledData"] = componentes_211[9]
                return componentes_direccion

            patron_212 = r'^({})\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+([A-Z]{{1}})\s+({})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z), re.escape(D), re.escape(Z2))
            componentes_212 = verificar_patron(cadena, patron_212)
            if componentes_212 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_212[0])
                componentes_direccion["ViaPrincipal"] = componentes_212[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_212[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_212[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_212[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_212[5])
                componentes_direccion["NumeroPlaca"] = componentes_212[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_212[7])
                componentes_direccion["InputPattern"] = 'T|+|Z|+|+[{}len=1]|D|+|Z'
                componentes_direccion["LineaPatron"] = '4388'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS SUR CELS A BIS RT ESTE'
                componentes_direccion["UnhandledData"] = componentes_212[8]
                return componentes_direccion

        for T, Z, Z2 in product(diccionario_T.keys(), diccionario_Z.keys(), diccionario_Z.keys()):

            patron_46 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(Z),
                                                                                                 re.escape(Z2))
            componentes_46 = verificar_patron(cadena, patron_46)
            if componentes_46 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_46[0])
                componentes_direccion["ViaPrincipal"] = componentes_46[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_46[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_46[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_46[4])
                componentes_direccion["NumeroPlaca"] = componentes_46[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '793'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 47 ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_46[6]
                return componentes_direccion
            patron_47 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z),
                                                                                                 re.escape(Z2))
            componentes_47 = verificar_patron(cadena, patron_47)
            if componentes_47 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_47[0])
                componentes_direccion["ViaPrincipal"] = componentes_47[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_47[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_47[3]
                componentes_direccion["NumeroPlaca"] = componentes_47[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_47[5])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '810'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 47 76 ESTE'
                componentes_direccion["UnhandledData"] = componentes_47[6]
                return componentes_direccion
            patron_49 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(Z2))
            componentes_49 = verificar_patron(cadena, patron_49)
            if componentes_49 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_49[0])
                componentes_direccion["ViaPrincipal"] = componentes_49[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_49[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_49[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_49[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_49[5])
                componentes_direccion["NumeroPlaca"] = componentes_49[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '859'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A SUR 47 ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_49[7]
                return componentes_direccion
            patron_51 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(Z2))
            componentes_51 = verificar_patron(cadena, patron_51)
            if componentes_51 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_51[0])
                componentes_direccion["ViaPrincipal"] = componentes_51[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_51[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_51[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_51[4]
                componentes_direccion["NumeroPlaca"] = componentes_51[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_51[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '950'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A SUR 47 76 ESTE'
                componentes_direccion["UnhandledData"] = componentes_51[7]
                return componentes_direccion

            patron_69 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(Z2))
            componentes_69 = verificar_patron(cadena, patron_69)
            if componentes_69 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_69[0])
                componentes_direccion["ViaPrincipal"] = componentes_69[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_69[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_69[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_69[4]
                componentes_direccion["NumeroPlaca"] = componentes_69[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_69[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1321'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A 76 ESTE'
                componentes_direccion["UnhandledData"] = componentes_69[7]
                return componentes_direccion
            patron_71 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(Z2))
            componentes_71 = verificar_patron(cadena, patron_71)
            if componentes_71 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_71[0])
                componentes_direccion["ViaPrincipal"] = componentes_71[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_71[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_71[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_71[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_71[5])
                componentes_direccion["NumeroPlaca"] = componentes_71[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1359'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_71[7]
                return componentes_direccion

            patron_173 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z), re.escape(Z2))
            componentes_173 = verificar_patron(cadena, patron_173)
            if componentes_173 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_173[0])
                componentes_direccion["ViaPrincipal"] = componentes_173[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_173[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_173[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_173[4]
                componentes_direccion["NumeroPlaca"] = componentes_173[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_173[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|>[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3361'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4 SUR 45D 45 ESTE'
                componentes_direccion["UnhandledData"] = componentes_173[7]
                return componentes_direccion

            patron_176 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z), re.escape(Z2))
            componentes_176 = verificar_patron(cadena, patron_176)
            if componentes_176 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_176[0])
                componentes_direccion["ViaPrincipal"] = componentes_176[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_176[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_176[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_176[4]
                componentes_direccion["LetraViaGeneradora"] = componentes_176[5]
                componentes_direccion["NumeroPlaca"] = componentes_176[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_176[7])
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|Z|>[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3418'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 45D SUR 34D 34 ESTE'
                componentes_direccion["UnhandledData"] = componentes_176[8]
                return componentes_direccion

            patron_184 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z), re.escape(Z2))
            componentes_184 = verificar_patron(cadena, patron_184)
            if componentes_184 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_184[0])
                componentes_direccion["ViaPrincipal"] = componentes_184[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_184[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_184[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_184[4]
                componentes_direccion["LetraViaGeneradora"] = componentes_184[5]
                componentes_direccion["NumeroPlaca"] = componentes_184[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_184[7])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}LEN=1]|Z|>[{}LEN<=4]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3567 - 3587'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 45 A SUR 45S 45 ESTE'
                componentes_direccion["UnhandledData"] = componentes_184[8]
                return componentes_direccion

        for T, D, Z in product(diccionario_T.keys(), diccionario_D.keys(), diccionario_Z.keys()):

            patron_40 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]+)\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T),
                                                                                                            re.escape(D),
                                                                                                            re.escape(Z))
            componentes_40 = verificar_patron(cadena, patron_40)
            if componentes_40 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_40[0])
                componentes_direccion["ViaPrincipal"] = componentes_40[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_40[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_40[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_40[4]
                componentes_direccion["NumeroPlaca"] = componentes_40[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_40[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|^[{}LEN<=3]|+|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '692'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 BIS 47 LADO 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_40[7]
                return componentes_direccion
            patron_41 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D),
                                                                                                 re.escape(Z))
            componentes_41 = verificar_patron(cadena, patron_41)
            if componentes_41 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_41[0])
                componentes_direccion["ViaPrincipal"] = componentes_41[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_41[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_41[3]
                componentes_direccion["NumeroPlaca"] = componentes_41[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_41[5])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '708'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 BIS 47 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_41[6]
                return componentes_direccion
            patron_44 = r'^({})\s+(\d{{1,3}})\s+({})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D),
                                                                                                 re.escape(Z))
            componentes_44 = verificar_patron(cadena, patron_44)
            if componentes_44 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_44[0])
                componentes_direccion["ViaPrincipal"] = componentes_44[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_44[2])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_44[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_44[4]
                componentes_direccion["NumeroPlaca"] = componentes_44[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '759'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 BIS SUR 47 76'
                componentes_direccion["UnhandledData"] = componentes_44[6]
                return componentes_direccion
            patron_45 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D), \
                                                                                                 re.escape(Z))
            componentes_45 = verificar_patron(cadena, patron_45)
            if componentes_45 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_45[0])
                componentes_direccion["ViaPrincipal"] = componentes_45[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_45[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_45[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_45[4])
                componentes_direccion["NumeroPlaca"] = componentes_45[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '776 -- 842'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 BIS 47 SUR 76'
                componentes_direccion["UnhandledData"] = componentes_45[6]
                return componentes_direccion
            patron_54 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_54 = verificar_patron(cadena, patron_54)
            if componentes_54 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_54[0])
                componentes_direccion["ViaPrincipal"] = componentes_54[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_54[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_54[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_54[4]
                componentes_direccion["NumeroPlaca"] = componentes_54[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_54[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1024'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS 45 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_54[7]
                return componentes_direccion
            patron_56 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_56 = verificar_patron(cadena, patron_56)
            if componentes_56 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_56[0])
                componentes_direccion["ViaPrincipal"] = componentes_56[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_56[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_56[3])
                componentes_direccion["LetraPrefijo"] = componentes_56[4]
                componentes_direccion["NumeroViaGeneradora"] = componentes_56[5]
                componentes_direccion["NumeroPlaca"] = componentes_56[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_56[7])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1060'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS B 45 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_56[8]
                return componentes_direccion
            patron_59 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_59 = verificar_patron(cadena, patron_59)
            if componentes_59 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_59[0])
                componentes_direccion["ViaPrincipal"] = componentes_59[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_59[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_59[3])
                componentes_direccion["LetraPrefijo"] = componentes_59[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_59[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_59[6]
                componentes_direccion["NumeroPlaca"] = componentes_59[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1123'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS B SUR 45 76'
                componentes_direccion["UnhandledData"] = componentes_59[8]
                return componentes_direccion
            patron_60 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_60 = verificar_patron(cadena, patron_60)
            if componentes_60 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_60[0])
                componentes_direccion["ViaPrincipal"] = componentes_60[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_60[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_60[3])
                componentes_direccion["LetraPrefijo"] = componentes_60[4]
                componentes_direccion["NumeroViaGeneradora"] = componentes_60[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_60[6])
                componentes_direccion["NumeroPlaca"] = componentes_60[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1144'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS B 45 SUR 76'
                componentes_direccion["UnhandledData"] = componentes_60[8]
                return componentes_direccion
            patron_62 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_62 = verificar_patron(cadena, patron_62)
            if componentes_62 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_62[0])
                componentes_direccion["ViaPrincipal"] = componentes_62[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_62[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_62[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_62[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_62[5]
                componentes_direccion["NumeroPlaca"] = componentes_62[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1186'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS SUR 45 76'
                componentes_direccion["UnhandledData"] = componentes_62[7]
                return componentes_direccion
            patron_63 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_63 = verificar_patron(cadena, patron_63)
            if componentes_63 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_63[0])
                componentes_direccion["ViaPrincipal"] = componentes_63[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_63[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_63[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_63[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_63[5])
                componentes_direccion["NumeroPlaca"] = componentes_63[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1205'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS 45 SUR 76'
                componentes_direccion["UnhandledData"] = componentes_63[7]
                return componentes_direccion
            patron_65 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_65 = verificar_patron(cadena, patron_65)
            if componentes_65 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_65[0])
                componentes_direccion["ViaPrincipal"] = componentes_65[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_65[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_65[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_65[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_65[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_65[6]
                componentes_direccion["NumeroPlaca"] = componentes_65[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1247'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS SUR 45 B 76'
                componentes_direccion["UnhandledData"] = componentes_65[8]
                return componentes_direccion
            patron_66 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_66 = verificar_patron(cadena, patron_66)
            if componentes_66 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_66[0])
                componentes_direccion["ViaPrincipal"] = componentes_66[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_66[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_66[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_66[4]
                componentes_direccion["LetraViaGeneradora"] = componentes_66[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_66[6])
                componentes_direccion["NumeroPlaca"] = componentes_66[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1268'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS 45 B SUR 76'
                componentes_direccion["UnhandledData"] = componentes_66[8]
                return componentes_direccion
            patron_75 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(D))
            componentes_75 = verificar_patron(cadena, patron_75)
            if componentes_75 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_75[0])
                componentes_direccion["ViaPrincipal"] = componentes_75[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_75[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_75[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_75[4]
                componentes_direccion["NumeroPlaca"] = diccionario_D.get(componentes_75[5])
                componentes_direccion["UnhandledData"] = componentes_75[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1450'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A BIS 76'
                componentes_direccion["UnhandledData"] = componentes_75[7]
                return componentes_direccion
            patron_76 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_76 = verificar_patron(cadena, patron_76)
            if componentes_76 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_76[0])
                componentes_direccion["ViaPrincipal"] = componentes_76[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_76[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_76[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_D.get(componentes_76[4])
                componentes_direccion["NumeroPlaca"] = diccionario_Z.get(componentes_76[5])
                componentes_direccion["UnhandledData"] = componentes_76[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1467'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A BIS ESTE 76'
                componentes_direccion["UnhandledData"] = componentes_76[7]
                return componentes_direccion
            patron_78 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(D), )
            componentes_78 = verificar_patron(cadena, patron_78)
            if componentes_78 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_78[0])
                componentes_direccion["ViaPrincipal"] = componentes_78[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_78[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_78[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_78[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_78[5])
                componentes_direccion["LetraSufijo"] = componentes_78[6]
                componentes_direccion["NumeroPlaca"] = componentes_78[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1566'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 46 A BIS B 76'
                componentes_direccion["UnhandledData"] = componentes_78[8]
                return componentes_direccion
            patron_79 = r'({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})^\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_79 = verificar_patron(cadena, patron_79)
            if componentes_79 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_79[0])
                componentes_direccion["ViaPrincipal"] = componentes_79[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_79[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_79[3]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_79[4])
                componentes_direccion["LetraSufijo"] = componentes_79[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_79[6])
                componentes_direccion["NumeroPlaca"] = componentes_79[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1587'
                componentes_direccion["DireccionEjemplo"] = ' CALLE 80 45 A BIS B SUR 76'
                componentes_direccion["UnhandledData"] = componentes_79[8]
                return componentes_direccion
            patron_84 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_84 = verificar_patron(cadena, patron_84)
            if componentes_84 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_84[0])
                componentes_direccion["ViaPrincipal"] = componentes_84[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_84[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_84[3]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_84[4])
                componentes_direccion["LetraSufijo"] = componentes_84[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_84[6])
                componentes_direccion["NumeroPlaca"] = componentes_84[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1689'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A BIS B SUR 76'
                componentes_direccion["UnhandledData"] = componentes_84[8]
                return componentes_direccion
            patron_85 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_85 = verificar_patron(cadena, patron_85)
            if componentes_85 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_85[0])
                componentes_direccion["ViaPrincipal"] = componentes_85[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_85[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_85[3]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_85[4])
                componentes_direccion["LetraSufijo"] = componentes_85[5]
                componentes_direccion["NumeroPlaca"] = componentes_85[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_85[7])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1710'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A BIS B SUR 76'
                componentes_direccion["UnhandledData"] = componentes_85[8]
                return componentes_direccion
            patron_87 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_87 = verificar_patron(cadena, patron_87)
            if componentes_87 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_87[0])
                componentes_direccion["ViaPrincipal"] = componentes_87[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_87[2]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_87[3])
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_87[4])
                componentes_direccion["NumeroPlaca"] = componentes_87[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|D|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1746'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 BIS SUR 76'
                componentes_direccion["UnhandledData"] = componentes_87[6]
                return componentes_direccion
            patron_88 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_88 = verificar_patron(cadena, patron_88)
            if componentes_88 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_88[0])
                componentes_direccion["ViaPrincipal"] = componentes_88[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_88[2]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_88[3])
                componentes_direccion["NumeroPlaca"] = componentes_88[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_88[5])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1763'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 46 BIS 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_88[6]
                return componentes_direccion
            patron_89 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_89 = verificar_patron(cadena, patron_89)
            if componentes_89 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_89[0])
                componentes_direccion["ViaPrincipal"] = componentes_89[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_89[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_89[3]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_89[4])
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_89[5])
                componentes_direccion["NumeroPlaca"] = componentes_89[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1780'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A BIS SUR 76'
                componentes_direccion["UnhandledData"] = componentes_89[7]
                return componentes_direccion
            patron_90 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_90 = verificar_patron(cadena, patron_90)
            if componentes_90 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_90[0])
                componentes_direccion["ViaPrincipal"] = componentes_90[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_90[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_90[3]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_90[4])
                componentes_direccion["NumeroPlaca"] = componentes_90[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_90[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1799'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A BIS 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_90[7]
                return componentes_direccion
            patron_97 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_97 = verificar_patron(cadena, patron_97)
            if componentes_97 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_97[0])
                componentes_direccion["ViaPrincipal"] = componentes_97[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_97[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_97[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_97[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_97[5])
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_97[6])
                componentes_direccion["NumeroPlaca"] = componentes_97[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1933'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B BIS SUR 76'
                componentes_direccion["UnhandledData"] = componentes_97[8]
                return componentes_direccion
            patron_98 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_98 = verificar_patron(cadena, patron_98)
            if componentes_98 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_98[0])
                componentes_direccion["ViaPrincipal"] = componentes_98[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_98[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_98[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_98[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_98[5])
                componentes_direccion["NumeroPlaca"] = componentes_98[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_98[7])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1955'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B BIS 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_98[8]
                return componentes_direccion
            patron_99 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_99 = verificar_patron(cadena, patron_99)
            if componentes_99 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_99[0])
                componentes_direccion["ViaPrincipal"] = componentes_99[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_99[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_99[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_99[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_99[5])
                componentes_direccion["LetraSufijo"] = componentes_99[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_99[7])
                componentes_direccion["NumeroPlaca"] = componentes_99[8]
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1976'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B BIS C SUR 76'
                componentes_direccion["UnhandledData"] = componentes_99[9]
                return componentes_direccion
            patron_100 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_100 = verificar_patron(cadena, patron_100)
            if componentes_100 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_100[0])
                componentes_direccion["ViaPrincipal"] = componentes_100[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_100[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_100[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_100[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_100[5])
                componentes_direccion["LetraSufijo"] = componentes_100[6]
                componentes_direccion["NumeroPlaca"] = componentes_100[7]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_100[8])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1999'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B BIS C 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_100[8]
                return componentes_direccion

            patron_142 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(Z))
            componentes_142 = verificar_patron(cadena, patron_142)
            if componentes_142 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_142[0])
                componentes_direccion["ViaPrincipal"] = componentes_142[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_142[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_142[3])
                componentes_direccion["LetraPrefijo"] = componentes_142[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_142[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_142[6]
                componentes_direccion["LetraViaGeneradora"] = componentes_142[7]
                componentes_direccion["NumeroPlaca"] = componentes_142[8]
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '2710'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4 A BIS A SUR 4 A 3'
                componentes_direccion["UnhandledData"] = componentes_142[9]
                return componentes_direccion

            patron_161 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                              re.escape(D),
                                                                                                              re.escape(Z))
            componentes_161 = verificar_patron(cadena, patron_161)
            if componentes_161 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_161[0])
                componentes_direccion["ViaPrincipal"] = componentes_161[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_161[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_161[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_161[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_161[5])
                componentes_direccion["NumeroPlaca"] = componentes_161[6]
                componentes_direccion[
                    "InputPattern"] = 'T|>[{}LEN=4]|D|^[{}LEN<=3]|Z|^[{}LEN<=3] --- T|>[{}LEN<=3]|D|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3144 --- 3162'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 40B BIS 56 ESTE 45'
                componentes_direccion["UnhandledData"] = componentes_161[7]
                return componentes_direccion

            patron_163 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T),
                                                                                                              re.escape(D),
                                                                                                              re.escape(Z))
            componentes_163 = verificar_patron(cadena, patron_163)
            if componentes_163 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_163[0])
                componentes_direccion["ViaPrincipal"] = componentes_163[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_163[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_163[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_163[4]
                componentes_direccion["NumeroPlaca"] = componentes_163[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_163[6])
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3180'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 45B BIS 45 45 ESTE'
                componentes_direccion["UnhandledData"] = componentes_163[7]
                return componentes_direccion

            patron_165 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T),
                                                                                                              re.escape(D),
                                                                                                              re.escape(Z))
            componentes_165 = verificar_patron(cadena, patron_165)
            if componentes_165 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_165[0])
                componentes_direccion["ViaPrincipal"] = componentes_165[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_165[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_165[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_165[4]
                componentes_direccion["NumeroPlaca"] = componentes_165[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_165[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|>[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3214'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 34B BIS 56 45'
                componentes_direccion["UnhandledData"] = componentes_165[7]
                return componentes_direccion

            patron_169 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_169 = verificar_patron(cadena, patron_169)
            if componentes_169 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_169[0])
                componentes_direccion["ViaPrincipal"] = componentes_169[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_169[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_169[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_169[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_169[5]
                componentes_direccion["NumeroPlaca"] = componentes_169[6]
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3287'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4D BIS SUR 78 89'
                componentes_direccion["UnhandledData"] = componentes_169[7]
                return componentes_direccion

            patron_170 = r'^({})\s+(\d{{1,3}})\s+({})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_170 = verificar_patron(cadena, patron_170)
            if componentes_170 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_170[0])
                componentes_direccion["ViaPrincipal"] = componentes_170[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_170[2])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_170[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_170[4]
                componentes_direccion["LetraViaPrincipal"] = componentes_170[5]
                componentes_direccion["NumeroPlaca"] = componentes_170[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|Z|>[{}LEN<=3]|^[{}LEN<=3] - T|^[{}LEN<=3]|D|Z|>[{}LEN=4]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3305 - 3818'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4 BIS SUR 4D 45'
                componentes_direccion["UnhandledData"] = componentes_170[7]
                return componentes_direccion

            patron_171 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_171 = verificar_patron(cadena, patron_171)
            if componentes_171 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_171[0])
                componentes_direccion["ViaPrincipal"] = componentes_171[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_171[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_171[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_171[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_171[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_171[6]
                componentes_direccion["NumeroPlaca"] = componentes_171[7]
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|Z|>[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3323'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4D BIS SUR 34F 45'
                componentes_direccion["UnhandledData"] = componentes_171[8]
                return componentes_direccion

            patron_181 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_181 = verificar_patron(cadena, patron_181)
            if componentes_181 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_181[0])
                componentes_direccion["ViaPrincipal"] = componentes_181[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_181[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_181[3]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_181[4])
                componentes_direccion["NumeroPlaca"] = componentes_181[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_181[6])
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|^[{}LEN<=3]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3510'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 89R 45 BIS 45 SUR'
                componentes_direccion["UnhandledData"] = componentes_181[7]
                return componentes_direccion

            patron_182 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_182 = verificar_patron(cadena, patron_182)
            if componentes_182 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_182[0])
                componentes_direccion["ViaPrincipal"] = componentes_182[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_182[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_182[3]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_182[4])
                componentes_direccion["NumeroPlaca"] = componentes_182[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_182[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|>[{}LEN<=3]|D|^[{}LEN<=3]|Z - T|^[{}LEN<=3]|>[{}LEN=4]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3528 - 3887'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 45 78G BIS 45 ESTE'
                componentes_direccion["UnhandledData"] = componentes_182[7]
                return componentes_direccion

            patron_183 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_183 = verificar_patron(cadena, patron_183)
            if componentes_183 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_183[0])
                componentes_direccion["ViaPrincipal"] = componentes_183[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_183[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_183[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_183[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_183[5])
                componentes_direccion["NumeroPlaca"] = componentes_183[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_183[7])
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|>[{}LEN<=3]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3546'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 78W 23R BIS 23 ESTE'
                componentes_direccion["UnhandledData"] = componentes_183[8]
                return componentes_direccion

            patron_190 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_190 = verificar_patron(cadena, patron_190)
            if componentes_190 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_190[0])
                componentes_direccion["ViaPrincipal"] = componentes_190[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_190[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_190[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_190[4]
                componentes_direccion["LetraViaGeneradora"] = componentes_190[5]
                componentes_direccion["NumeroPlaca"] = componentes_190[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_190[7])
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|>[{}LEN=4]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3779'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 45D BIS 45R 45 SUR'
                componentes_direccion["UnhandledData"] = componentes_190[8]
                return componentes_direccion

            patron_192 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_192 = verificar_patron(cadena, patron_192)
            if componentes_192 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_192[0])
                componentes_direccion["ViaPrincipal"] = componentes_192[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_192[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_192[3])
                componentes_direccion["LetraPrefijo"] = componentes_192[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_192[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_192[6]
                componentes_direccion["NumeroPlaca"] = componentes_192[7]
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|+[{}LEN=1]|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3905'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 78F BIS A SUR 45 45'
                componentes_direccion["UnhandledData"] = componentes_192[8]
                return componentes_direccion

            patron_195 = r'^({})\s+(\d{{1,3}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z))
            componentes_195 = verificar_patron(cadena, patron_195)
            if componentes_195 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_195[0])
                componentes_direccion["ViaPrincipal"] = componentes_195[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_195[2])
                componentes_direccion["LetraPrefijo"] = componentes_195[3]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_195[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_195[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_195[6]
                componentes_direccion["NumeroPlaca"] = componentes_195[7]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|+[{}LEN=1]|Z|>[{}LEN=4]|^[{}LEN<=3] - T|^[{}LEN<=3]|D|+[{}LEN=1]|Z|>[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3978 - 3998'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 78 BIS A SUR 45D 78'
                componentes_direccion["UnhandledData"] = componentes_195[8]
                return componentes_direccion

            patron_196 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_196 = verificar_patron(cadena, patron_196)
            if componentes_196 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_196[0])
                componentes_direccion["ViaPrincipal"] = componentes_196[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_196[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_196[3])
                componentes_direccion["LetraPrefijo"] = componentes_196[4]
                componentes_direccion["NumeroViaGeneradora"] = componentes_196[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_196[6]
                componentes_direccion["NumeroPlaca"] = componentes_196[7]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_196[8])
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|+[{}LEN=1]|>[{}LEN=4]|^[{}LEN<=3]|Z - T|>[{}LEN<=3]|D|+[{}LEN=1]|>[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '4018 - 4041'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 78D BIS A 78R 45 ESTE'
                componentes_direccion["UnhandledData"] = componentes_196[9]
                return componentes_direccion

            patron_208 = r'^({})\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_208 = verificar_patron(cadena, patron_208)
            if componentes_208 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_208[0])
                componentes_direccion["ViaPrincipal"] = componentes_208[1]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_208[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_208[3]
                componentes_direccion["NumeroPlaca"] = componentes_208[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_208[5])
                componentes_direccion["InputPattern"] = 'T|+|D|+|+|Z'
                componentes_direccion["LineaPatron"] = '4310'
                componentes_direccion["DireccionEjemplo"] = 'CALLE AB BIS RT RTT SUR'
                componentes_direccion["UnhandledData"] = componentes_208[6]
                return componentes_direccion

            patron_209 = r'^({})\s+([A-Z]+)\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+([A-Z]+)\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_209 = verificar_patron(cadena, patron_209)
            if componentes_209 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_209[0])
                componentes_direccion["ViaPrincipal"] = componentes_209[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_209[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_209[3])
                componentes_direccion["LetraPrefijo"] = componentes_209[4]
                componentes_direccion["NumeroViaGeneradora"] = componentes_209[5]
                componentes_direccion["NumeroPlaca"] = componentes_209[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_209[7])
                componentes_direccion["InputPattern"] = 'T|+|+[{}len=1]|D|+[{}len=1]|+|+|Z'
                componentes_direccion["LineaPatron"] = '4327'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS T BIS R JIMENEZ ROJAS ESTE'
                componentes_direccion["UnhandledData"] = componentes_209[8]
                return componentes_direccion

            patron_213 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_213 = verificar_patron(cadena, patron_213)
            if componentes_213 is not None:
                componentes_direccion["TipoVia"] = componentes_213[0]
                componentes_direccion["ViaPrincipal"] = componentes_213[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_213[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_213[3]
                componentes_direccion["Sufijo"] = componentes_213[4]
                componentes_direccion["LetraSufijo"] = componentes_213[5]
                componentes_direccion["NumeroPlaca"] = componentes_213[6]
                componentes_direccion["CuadranteAdicional"] = componentes_213[7]
                componentes_direccion["InputPattern"] = 'T|+|+|+[{}len=1]|D|+[{}len=1]|+|Z'
                componentes_direccion["LineaPatron"] = '4409'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS JIMENEZ A BIS A ROJAS ESTE'
                componentes_direccion["UnhandledData"] = componentes_213[8]
                return componentes_direccion

            patron_214 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_214 = verificar_patron(cadena, patron_214)
            if componentes_214 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_214[0])
                componentes_direccion["ViaPrincipal"] = componentes_214[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_214[2]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_214[3])
                componentes_direccion["NumeroPlaca"] = componentes_214[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_214[5])
                componentes_direccion["InputPattern"] = 'T|+|+|D|+|Z'
                componentes_direccion["LineaPatron"] = '4430'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS JIMENEZ BIS ROJAS ESTE'
                componentes_direccion["UnhandledData"] = componentes_214[6]
                return componentes_direccion

            patron_215 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]{{1}})\s+({})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_215 = verificar_patron(cadena, patron_215)
            if componentes_215 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_215[0])
                componentes_direccion["ViaPrincipal"] = componentes_215[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_215[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_215[3]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_215[4])
                componentes_direccion["NumeroPlaca"] = componentes_215[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_215[6])
                componentes_direccion["InputPattern"] = 'T|+|+|+[{}len=1]|D|+|Z'
                componentes_direccion["LineaPatron"] = '4447'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS JIMENEZ A BIS DER ESTE'
                componentes_direccion["UnhandledData"] = componentes_215[7]
                return componentes_direccion

            patron_217 = r'^({})\s+([A-Z]+)\s+([A-Z]{{1}})\s+([A-Z]+)\s+([A-Z]{{1}})\s+({})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_217 = verificar_patron(cadena, patron_217)
            if componentes_217 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_217[0])
                componentes_direccion["ViaPrincipal"] = componentes_217[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_217[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_217[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_217[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_217[5])
                componentes_direccion["NumeroPlaca"] = componentes_217[6]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_217[7])
                componentes_direccion["InputPattern"] = 'T|+|+[{}len=1]|+|+[{}len=1]|D|+|Z'
                componentes_direccion["LineaPatron"] = '4485'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS A CELESTINO A BIS RMR ESTE'
                componentes_direccion["UnhandledData"] = componentes_217[8]
                return componentes_direccion

            patron_218 = r'^({})\s+([A-Z]+)\s+([A-Z]{{1}})\s+([A-Z]+)\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(D), re.escape(Z))
            componentes_218 = verificar_patron(cadena, patron_218)
            if componentes_218 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_218[0])
                componentes_direccion["ViaPrincipal"] = componentes_218[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_218[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_218[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_218[4]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_218[5])
                componentes_direccion["LetraSufijo"] = componentes_218[6]
                componentes_direccion["NumeroPlaca"] = componentes_218[7]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_218[8])
                componentes_direccion["InputPattern"] = 'T|+|+[{}len=1]|+|+[{}len=1]|D|+[{}len=1]|+|Z'
                componentes_direccion["LineaPatron"] = '4506'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS A CELESTINO Z BIS W RTR ESTE'
                componentes_direccion["UnhandledData"] = componentes_218[9]
                return componentes_direccion

        for T, D, D2, Z in product(diccionario_T.keys(), diccionario_D.keys(), diccionario_D.keys(), diccionario_Z.keys()):

            patron_141 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(D2), re.escape(Z))
            componentes_141 = verificar_patron(cadena, patron_141)
            if componentes_141 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_141[0])
                componentes_direccion["ViaPrincipal"] = componentes_141[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_141[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_141[3])
                componentes_direccion["LetraPrefijo"] = componentes_141[4]
                componentes_direccion["NumeroViaGeneradora"] = componentes_141[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_141[6]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_141[7])
                componentes_direccion["NumeroPlaca"] = componentes_141[8]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_141[9])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '2684'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS A 3 A BIS 3 SUR'
                componentes_direccion["UnhandledData"] = componentes_141[10]
                return componentes_direccion

            patron_145 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(Z),
                re.escape(D2))
            componentes_145 = verificar_patron(cadena, patron_145)
            if componentes_145 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_145[0])
                componentes_direccion["ViaPrincipal"] = componentes_145[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_145[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_145[3])
                componentes_direccion["LetraPrefijo"] = componentes_145[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_145[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_145[6]
                componentes_direccion["LetraViaGeneradora"] = componentes_145[7]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_145[8])
                componentes_direccion["NumeroPlaca"] = componentes_145[9]
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '2781'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 8 D BIS A SUR 4 A BIS 4'
                componentes_direccion["UnhandledData"] = componentes_145[10]
                return componentes_direccion

            patron_146 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T),
                re.escape(D),
                re.escape(Z),
                re.escape(D2))
            componentes_146 = verificar_patron(cadena, patron_146)
            if componentes_146 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_146[0])
                componentes_direccion["ViaPrincipal"] = componentes_146[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_146[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_146[3])
                componentes_direccion["LetraPrefijo"] = componentes_146[4]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_146[5])
                componentes_direccion["NumeroViaGeneradora"] = componentes_146[6]
                componentes_direccion["LetraViaGeneradora"] = componentes_146[7]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_146[8])
                componentes_direccion["LetraSufijo"] = componentes_146[9]
                componentes_direccion["NumeroPlaca"] = componentes_146[10]
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|Z|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '2806'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS A SUR 4 A BIS A 4'
                componentes_direccion["UnhandledData"] = componentes_146[11]
                return componentes_direccion

            patron_150 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z), re.escape(D2))
            componentes_150 = verificar_patron(cadena, patron_150)
            if componentes_150 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_150[0])
                componentes_direccion["ViaPrincipal"] = componentes_150[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_150[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_150[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_150[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_150[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_150[6]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_150[7])
                componentes_direccion["NumeroPlaca"] = componentes_150[8]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '2910'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS SUR 4 A BIS 4'
                componentes_direccion["UnhandledData"] = componentes_150[9]
                return componentes_direccion

            patron_152 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(D), re.escape(Z), re.escape(D2))
            componentes_152 = verificar_patron(cadena, patron_152)
            if componentes_152 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_152[0])
                componentes_direccion["ViaPrincipal"] = componentes_152[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_152[2]
                componentes_direccion["Prefijo"] = diccionario_D.get(componentes_152[3])
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_152[4])
                componentes_direccion["NumeroViaGeneradora"] = componentes_152[5]
                componentes_direccion["LetraViaGeneradora"] = componentes_152[6]
                componentes_direccion["Sufijo"] = diccionario_D.get(componentes_152[7])
                componentes_direccion["LetraSufijo"] = componentes_152[8]
                componentes_direccion["NumeroPlaca"] = componentes_152[9]
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|Z|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '2956'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 A BIS SUR 4 A BIS A 3'
                componentes_direccion["UnhandledData"] = componentes_152[10]
                return componentes_direccion


        for T, Z, C in product(diccionario_T.keys(), diccionario_Z.keys(), diccionario_C.keys()):
            patron_50 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(C))
            componentes_50 = verificar_patron(cadena, patron_50)
            if componentes_50 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_50[0])
                componentes_direccion["ViaPrincipal"] = componentes_50[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_50[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_50[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_50[4]
                componentes_direccion["NumeroPlaca"] = componentes_50[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_C.get(componentes_50[6])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]|^[{}LEN<=3]|+="S",+="N",+="O",+="E"'
                componentes_direccion["LineaPatron"] = '931'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A SUR 47 76 E'
                componentes_direccion["UnhandledData"] = componentes_XXX[X]
                return componentes_direccion
            patron_70 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z), re.escape(C))
            componentes_70 = verificar_patron(cadena, patron_70)
            if componentes_70 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_70[0])
                componentes_direccion["ViaPrincipal"] = componentes_70[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_70[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_70[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_70[4]
                componentes_direccion["NumeroPlaca"] = componentes_70[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_C.get(componentes_70[6])
                componentes_direccion[
                    "InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+="S",+="N",+="O",+="E"'
                componentes_direccion["LineaPatron"] = '1340'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A 76 E'
                componentes_direccion["UnhandledData"] = componentes_70[7]
                return componentes_direccion



        for T, Z in product(diccionario_T.keys(), diccionario_Z.keys()):

            patron_12 = r'^({})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_12 = verificar_patron(cadena, patron_12)
            if componentes_12 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_12[0])
                componentes_direccion["ViaPrincipal"] = diccionario_Z.get(componentes_12[1])
                componentes_direccion["NumeroViaGeneradora"] = componentes_12[2]
                componentes_direccion["NumeroPlaca"] = componentes_12[3]
                componentes_direccion["InputPattern"] = '*T|Z|^|^'
                componentes_direccion["LineaPatron"] = '188 '
                componentes_direccion["DireccionEjemplo"] = 'CARR SUR 34 76'
                componentes_direccion["UnhandledData"] = componentes_12[4]
                return componentes_direccion
            patron_21 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z))
            componentes_21 = verificar_patron(cadena, patron_21)
            if componentes_21 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_21[0])
                componentes_direccion["ViaPrincipal"] = componentes_21[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_21[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_21[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_21[4]
                componentes_direccion["NumeroPlaca"] = componentes_21[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_21[6])
                componentes_direccion["InputPattern"] = 'T>>^Z T|>[{}LEN<=3]|>[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '357'
                componentes_direccion["DireccionEjemplo"] = 'Calle 34A 456D 78 SUR'
                componentes_direccion["UnhandledData"] = componentes_21[7]
                return componentes_direccion
            patron_26 = r'^({})\s+([A-Z]+)\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_26 = verificar_patron(cadena, patron_26)
            if componentes_26 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_26[0])
                componentes_direccion["ViaPrincipal"] = componentes_26[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_26[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_26[4])
                componentes_direccion["UnhandledPattern"] = '+'
                componentes_direccion["UnhandledData"] = componentes_26[1] + ' ' + componentes_26[5]
                componentes_direccion["InputPattern"] = 'T+^^Z'
                componentes_direccion["LineaPatron"] = '463'
                componentes_direccion["DireccionEjemplo"] = 'Carrera rojas 34 45 SUR'
                return componentes_direccion
            patron_30 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T),
                                                                                                         re.escape(Z))
            componentes_30 = verificar_patron(cadena, patron_30)
            if componentes_30 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_30[0])
                componentes_direccion["ViaPrincipal"] = componentes_30[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_30[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_30[3]
                componentes_direccion["NumeroPlaca"] = componentes_30[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_30[5])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '529'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 34 A 89 78 SUR'
                componentes_direccion["UnhandledData"] = componentes_30[6]
                return componentes_direccion
            patron_31 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                         re.escape(Z))
            componentes_31 = verificar_patron(cadena, patron_31)
            if componentes_31 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_31[0])
                componentes_direccion["ViaPrincipal"] = componentes_31[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_31[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_31[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_31[4])
                componentes_direccion["NumeroPlaca"] = componentes_31[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '546 -- 893'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 SUR 78'
                componentes_direccion["UnhandledData"] = componentes_31[6]
                return componentes_direccion
            patron_32 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_32 = verificar_patron(cadena, patron_32)
            if componentes_32 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_32[0])
                componentes_direccion["ViaPrincipal"] = componentes_32[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_32[2]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_32[3])
                componentes_direccion["NumeroPlaca"] = componentes_32[4]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '563 -- 873 '
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 SUR 78'
                componentes_direccion["UnhandledData"] = componentes_32[5]
                return componentes_direccion
            patron_33 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_33 = verificar_patron(cadena, patron_33)
            if componentes_33 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_33[0])
                componentes_direccion["ViaPrincipal"] = componentes_33[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_33[2]
                componentes_direccion["NumeroPlaca"] = componentes_33[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_33[4])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '578'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 78 SUR'
                componentes_direccion["UnhandledData"] = componentes_33[5]
                return componentes_direccion
            patron_48 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_48 = verificar_patron(cadena, patron_48)
            if componentes_48 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_48[0])
                componentes_direccion["ViaPrincipal"] = componentes_48[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_48[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_48[3]
                componentes_direccion["NumeroPlaca"] = componentes_48[4]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '827'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 47 76'
                componentes_direccion["UnhandledData"] = componentes_48[5]
                return componentes_direccion
            patron_52 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                         re.escape(Z))
            componentes_52 = verificar_patron(cadena, patron_52)
            if componentes_52 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_52[0])
                componentes_direccion["ViaPrincipal"] = componentes_52[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_52[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_52[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_52[4]
                componentes_direccion["NumeroPlaca"] = componentes_52[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '969'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A SUR 47 76'
                componentes_direccion["UnhandledData"] = componentes_52[6]
                return componentes_direccion

            patron_67 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z))
            componentes_67 = verificar_patron(cadena, patron_67)
            if componentes_67 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_67[0])
                componentes_direccion["ViaPrincipal"] = componentes_67[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_67[2]
                componentes_direccion["LetraSufijo"] = componentes_67[3]
                componentes_direccion["NumeroPlaca"] = componentes_67[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_67[5])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1289'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_67[6]
                return componentes_direccion
            patron_72 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T),
                re.escape(Z))
            componentes_72 = verificar_patron(cadena, patron_72)
            if componentes_72 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_72[0])
                componentes_direccion["ViaPrincipal"] = componentes_72[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_72[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_72[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_72[4]
                componentes_direccion["NumeroPlaca"] = componentes_72[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1359'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 SUR 45 A 76'
                componentes_direccion["UnhandledData"] = componentes_72[6]
                return componentes_direccion
            patron_73 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T),
                re.escape(Z))
            componentes_73 = verificar_patron(cadena, patron_73)
            if componentes_73 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_73[0])
                componentes_direccion["ViaPrincipal"] = componentes_73[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_73[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_73[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_73[4])
                componentes_direccion["NumeroPlaca"] = componentes_73[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1414'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A SUR 76'
                componentes_direccion["UnhandledData"] = componentes_73[6]
                return componentes_direccion
            patron_91 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T),
                re.escape(Z))
            componentes_91 = verificar_patron(cadena, patron_91)
            if componentes_91 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_91[0])
                componentes_direccion["ViaPrincipal"] = componentes_91[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_91[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_91[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_91[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_91[5])
                componentes_direccion["NumeroPlaca"] = componentes_91[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '1818'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B SUR 76'
                componentes_direccion["UnhandledData"] = componentes_91[7]
                return componentes_direccion
            patron_92 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T),
                re.escape(Z))
            componentes_92 = verificar_patron(cadena, patron_92)
            if componentes_92 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_92[0])
                componentes_direccion["ViaPrincipal"] = componentes_92[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_92[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_92[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_92[4]
                componentes_direccion["NumeroPlaca"] = componentes_92[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_92[6])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '1837'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B 76 SUR'
                componentes_direccion["UnhandledData"] = componentes_92[7]
                return componentes_direccion

            patron_155 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T),
                                                                                                       re.escape(Z))
            componentes_155 = verificar_patron(cadena, patron_155)
            if componentes_155 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_155[0])
                componentes_direccion["ViaPrincipal"] = componentes_155[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_155[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_155[3]
                componentes_direccion["NumeroPlaca"] = componentes_155[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_155[5])
                componentes_direccion[
                    "InputPattern"] = 'T|>[{}LEN=4]|^[{}LEN<=3]|^[{}LEN<=3]|Z --- T|>[{}LEN<=3]|^[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3033 --- 3049'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 456A 45 45 ESTE'
                componentes_direccion["UnhandledData"] = componentes_155[6]
                return componentes_direccion

            patron_157 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T),
                                                                                                       re.escape(Z))
            componentes_157 = verificar_patron(cadena, patron_157)
            if componentes_157 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_157[0])
                componentes_direccion["ViaPrincipal"] = componentes_157[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_157[2]
                componentes_direccion["LetraViaGeneradora"] = componentes_157[3]
                componentes_direccion["NumeroPlaca"] = componentes_157[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_157[5])
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|>[{}LEN<=3]|^[{}LEN<=3]|Z - T|^[{}LEN<=3]|>[{}LEN=4]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3081 - 3694'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 3 45A 45 SUR'
                componentes_direccion["UnhandledData"] = componentes_157[6]
                return componentes_direccion

            patron_158 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
                re.escape(T), re.escape(Z))
            componentes_158 = verificar_patron(cadena, patron_158)
            if componentes_158 is not None:
                componentes_direccion["TipoVia"] = componentes_158[0]
                componentes_direccion["ViaPrincipal"] = componentes_158[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_158[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_158[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_158[4]
                componentes_direccion["NumeroPlaca"] = componentes_158[5]
                componentes_direccion["CuadranteAdicional"] = componentes_158[6]
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|>[{}LEN<=3]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '3097'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 45A 30A 12 ESTE'
                componentes_direccion["UnhandledData"] = componentes_158[7]
                return componentes_direccion

            patron_172 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_172 = verificar_patron(cadena, patron_172)
            if componentes_172 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_172[0])
                componentes_direccion["ViaPrincipal"] = componentes_172[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_172[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_172[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_172[4]
                componentes_direccion["NumeroPlaca"] = componentes_172[5]
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|Z|^[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3344'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4D SUR 5 6'
                componentes_direccion["UnhandledData"] = componentes_172[6]
                return componentes_direccion

            patron_174 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_174 = verificar_patron(cadena, patron_174)
            if componentes_174 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_174[0])
                componentes_direccion["ViaPrincipal"] = componentes_174[1]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_174[2])
                componentes_direccion["NumeroViaGeneradora"] = componentes_174[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_174[4]
                componentes_direccion["NumeroPlaca"] = componentes_174[5]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|Z|>[{}LEN<=3]|^[{}LEN<=3] - T|^[{}LEN<=3]|Z|>[{}LEN=4]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3380 - 3836'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4 SUR 45D 45'
                componentes_direccion["UnhandledData"] = componentes_174[6]
                return componentes_direccion

            patron_175 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+([OESN])\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_175 = verificar_patron(cadena, patron_175)
            if componentes_175 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_175[0])
                componentes_direccion["ViaPrincipal"] = componentes_175[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_175[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_175[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_175[4]
                componentes_direccion["LetraViaGeneradora"] = componentes_175[5]
                componentes_direccion["NumeroPlaca"] = componentes_175[6]
                componentes_direccion["CuadranteAdicional"] = componentes_175[7]
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|Z|>[{}LEN<=3]|^[{}LEN<=3]|+="S",+="N",+="O",+="E"'
                componentes_direccion["LineaPatron"] = '3397'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 4D SUR 34H 45 S'
                componentes_direccion["UnhandledData"] = componentes_175[8]
                return componentes_direccion

            patron_177 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_177 = verificar_patron(cadena, patron_177)
            if componentes_177 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_177[0])
                componentes_direccion["ViaPrincipal"] = componentes_177[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_177[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_177[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_177[4]
                componentes_direccion["LetraViaGeneradora"] = componentes_177[5]
                componentes_direccion["NumeroPlaca"] = componentes_177[6]
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|Z|>[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3440'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 45D SUR 23A 45'
                componentes_direccion["UnhandledData"] = componentes_177[7]
                return componentes_direccion

            patron_193 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
                re.escape(T), re.escape(Z))
            componentes_193 = verificar_patron(cadena, patron_193)
            if componentes_193 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_193[0])
                componentes_direccion["ViaPrincipal"] = componentes_193[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_193[2]
                componentes_direccion["Cuadrante"] = diccionario_Z.get(componentes_193[3])
                componentes_direccion["NumeroViaGeneradora"] = componentes_193[4]
                componentes_direccion["LetraViaGeneradora"] = componentes_193[5]
                componentes_direccion["NumeroPlaca"] = componentes_193[6]
                componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+|Z|>[{}LEN=4]|^[{}LEN<=3] - T|^[{}LEN<=3]|+|Z|>[{}LEN<=3]|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '3925 - 3943'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 45 A SUR 78E 45'
                componentes_direccion["UnhandledData"] = componentes_193[7]
                return componentes_direccion

            patron_197 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_197 = verificar_patron(cadena, patron_197)
            if componentes_197 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_197[0])
                componentes_direccion["ViaPrincipal"] = componentes_197[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_197[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_197[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_197[4]
                componentes_direccion["NumeroPlaca"] = componentes_197[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_197[6])
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|^[{}LEN<=3]|+[{}LEN=1]|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '4065'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 78D 78 A 78 SUR'
                componentes_direccion["UnhandledData"] = componentes_197[7]
                return componentes_direccion

            patron_199 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_199 = verificar_patron(cadena, patron_199)
            if componentes_199 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_199[0])
                componentes_direccion["ViaPrincipal"] = componentes_199[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_199[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_199[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_199[4])
                componentes_direccion["NumeroPlaca"] = componentes_199[5]
                componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|^[{}LEN<=3]|Z|^[{}LEN<=3]'
                componentes_direccion["LineaPatron"] = '4098'
                componentes_direccion["DireccionEjemplo"] = 'CALLE 78R 45 SUR 78'
                componentes_direccion["UnhandledData"] = componentes_199[6]
                return componentes_direccion

            patron_202 = r'^({})\s+([A-Z]+)\s+([A-Z]{{1}})\s+([A-Z]+)\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_202 = verificar_patron(cadena, patron_202)
            if componentes_202 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_202[0])
                componentes_direccion["ViaPrincipal"] = componentes_202[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_202[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_202[3]
                componentes_direccion["NumeroPlaca"] = componentes_202[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_202[5])
                componentes_direccion["InputPattern"] = 'T|+|+[{}LEN=1]|+|+|Z'
                componentes_direccion["LineaPatron"] = '4168'
                componentes_direccion["DireccionEjemplo"] = 'CALLE FABIAN A TR TY SUR'
                componentes_direccion["UnhandledData"] = componentes_202[6]
                return componentes_direccion

            patron_205 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_205 = verificar_patron(cadena, patron_205)
            if componentes_205 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_205[0])
                componentes_direccion["ViaPrincipal"] = componentes_205[1] + ' ' + componentes_205[2] + ' ' + \
                                                        componentes_205[3]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_205[4])
                componentes_direccion["InputPattern"] = 'T|+|+|+|Z'
                componentes_direccion["LineaPatron"] = '4239'
                componentes_direccion["DireccionEjemplo"] = 'CALLE JOSE CELESTINO MUTIS SUR'
                componentes_direccion["UnhandledData"] = componentes_205[5]
                return componentes_direccion

            patron_210 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]{{1}})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z))
            componentes_210 = verificar_patron(cadena, patron_210)
            if componentes_210 is not None:
                componentes_direccion["TipoVia"] = diccionario_Z.get(componentes_210[0])
                componentes_direccion["ViaPrincipal"] = componentes_210[1]
                componentes_direccion["NumeroViaGeneradora"] = componentes_210[2]
                componentes_direccion["LetraSufijo"] = componentes_210[3]
                componentes_direccion["NumeroPlaca"] = componentes_210[4]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_210[5])
                componentes_direccion["InputPattern"] = 'T|+|+|+[{}len=1]|+|Z'
                componentes_direccion["LineaPatron"] = '4338'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS CELESTINO B TRER SUR'
                componentes_direccion["UnhandledData"] = componentes_210[6]
                return componentes_direccion

            patron_216 = r'^({})\s+([A-Z]+)\s+([A-Z]{{1}})\s+([A-Z]+)\s+([A-Z]{{1}})\s+([A-Z]+)\s+({})\s*(.*)$'.format(re.escape(T), re.escape(Z), re.escape(Z2))
            componentes_216 = verificar_patron(cadena, patron_216)
            if componentes_216 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_216[0])
                componentes_direccion["ViaPrincipal"] = componentes_216[1]
                componentes_direccion["LetraViaPrincipal"] = componentes_216[2]
                componentes_direccion["NumeroViaGeneradora"] = componentes_216[3]
                componentes_direccion["LetraViaGeneradora"] = componentes_216[4]
                componentes_direccion["NumeroPlaca"] = componentes_216[5]
                componentes_direccion["CuadranteAdicional"] = diccionario_Z.get(componentes_216[6])
                componentes_direccion["InputPattern"] = 'T|+|+[{}len=1]|+|+[{}len=1]|+|Z'
                componentes_direccion["LineaPatron"] = '4466'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS A CELESTINO B ROJAS SUR'
                componentes_direccion["UnhandledData"] = componentes_216[7]
                return componentes_direccion

        for T, T2, Z in product(diccionario_T.keys(), diccionario_T.keys(), diccionario_Z.keys()):
            patron_201 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T),re.escape(T2),re.escape(Z))
            componentes_201 = verificar_patron(cadena, patron_201)
            if componentes_201 is not None:
                componentes_direccion["TipoVia"] = diccionario_T.get(componentes_201[0])
                componentes_direccion["ViaPrincipal"] = componentes_201[1] + ' ' + componentes_201[2] + ' ' + componentes_201[3]
                componentes_direccion["InputPattern"] = 'T|+|+|+|T|^[{}LEN<=3]|Z'
                componentes_direccion["LineaPatron"] = '4152'
                componentes_direccion["DireccionEjemplo"] = 'CALLE ROJAS JIMENEZ ROMERO AVENIDA 48 SUR'
                componentes_direccion["UnhandledData"] = componentes_201[6]
                return componentes_direccion


    for T, T2 in product(diccionario_T.keys(), diccionario_T.keys()):
        patron_11 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(T2))
        componentes_11 = verificar_patron(cadena, patron_11)
        if componentes_11 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_11[0])
            componentes_direccion["ViaPrincipal"] = componentes_11[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_11[3]
            componentes_direccion["NumeroPlaca"] = componentes_11[4]
            componentes_direccion["InputPattern"] = '*T|^|T[{}LEN<=2]|^|^'
            componentes_direccion["LineaPatron"] = '175'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 AV 45 54'
            componentes_direccion["UnhandledData"] = componentes_11[5]
            return componentes_direccion
        patron_15 = r'^([A-Z]+)\s+([A-Z]+)\s+({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                              re.escape(T2))
        componentes_15 = verificar_patron(cadena, patron_15)
        if componentes_15 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_15[2])
            componentes_direccion["ViaPrincipal"] = componentes_15[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_15[5]
            componentes_direccion["UnhandledPattern"] = '++'
            componentes_direccion["UnhandledData"] = componentes_15[0], componentes_15[1]
            componentes_direccion["InputPattern"] = '+|+|T|^[{}LEN<=3]|T|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '231'
            componentes_direccion["DireccionEjemplo"] = 'Conjunt claros Calle 67 AV 78'
            componentes_direccion["UnhandledData"] = componentes_15[6]
            return componentes_direccion
        patron_16 = r'^({})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(T2))
        componentes_16 = verificar_patron(cadena, patron_16)
        if componentes_16 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_16[0])
            componentes_direccion["ViaPrincipal"] = componentes_16[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_16[3]
            componentes_direccion["NumeroPlaca"] = componentes_16[4]
            componentes_direccion["InputPattern"] = 'TT^^^'
            componentes_direccion["LineaPatron"] = '257'
            componentes_direccion["DireccionEjemplo"] = 'AV CARRERA 56 78 89'
            componentes_direccion["UnhandledData"] = componentes_16[5]
            return componentes_direccion
        patron_17 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(T2))
        componentes_17 = verificar_patron(cadena, patron_17)
        if componentes_17 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_17[0])
            componentes_direccion["ViaPrincipal"] = componentes_17[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_17[3]
            componentes_direccion["InputPattern"] = 'T^T^'
            componentes_direccion["LineaPatron"] = '270'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 56 AV 89'
            componentes_direccion["UnhandledData"] = componentes_17[4]
            return componentes_direccion
        patron_34 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]+)\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]+)\s+(\d{{1,3}})\s+([A-Z]+)$'.format(
            re.escape(T), re.escape(T2))
        componentes_34 = verificar_patron(cadena, patron_34)
        if componentes_34 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_34[0])
            componentes_direccion["ViaPrincipal"] = componentes_34[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_34[2]
            componentes_direccion["NumeroPlaca"] = componentes_34[3]
            componentes_direccion["UnhandledPattern"] = '+T^^+^+'
            componentes_direccion[
                "InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|^[{}LEN<=3]|+|T|^[{}LEN<=3]|^[{}LEN<=3]|+|^[{}LEN<=3]|+'
            componentes_direccion["UserOverrideFlag"] = 'NO'
            componentes_direccion["LineaPatron"] = '595'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 78 LADO CARRERA 65 78 PISO 45 LLAMAR'
            componentes_direccion["UnhandledData"] = componentes_34[4] + " " + diccionario_T.get(
                componentes_34[5]) + " " + componentes_34[6] + " " + componentes_34[7] + " " + componentes_34[
                                                         8] + " " + componentes_34[9] + " " + componentes_34[10]
            return componentes_direccion


    for T, D, D2 in product(diccionario_T.keys(), diccionario_D.keys(), diccionario_D.keys()):
        patron_200 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D),re.escape(D2))
        componentes_200 = verificar_patron(cadena, patron_200)
        if componentes_200 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_200[0])
            componentes_direccion["ViaPrincipal"] = componentes_200[1]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_200[2])
            componentes_direccion["NumeroViaGeneradora"] = componentes_200[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_200[4]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_200[5])
            componentes_direccion["NumeroPlaca"] = componentes_200[6]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|>[{}LEN=4]|D|^[{}LEN<=3] - T|^[{}LEN<=3]|D|>[{}LEN<=3]|D|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '4114 - 4132'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 78 BIS 78E BIS 45'
            componentes_direccion["UnhandledData"] = componentes_200[7]
            return componentes_direccion

    for T, C in product(diccionario_T.keys(), diccionario_C.keys()):
        patron_35 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(re.escape(T), re.escape(C))
        componentes_35 = verificar_patron(cadena, patron_35)
        if componentes_35 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_35[0])
            componentes_direccion["ViaPrincipal"] = componentes_35[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_35[2]
            componentes_direccion["NumeroPlaca"] = componentes_35[3]
            componentes_direccion["CuadranteAdicional"] = diccionario_C.get(componentes_35[4])
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|^[{}LEN<=3]|+="S",+="N",+="O",+="E"'
            componentes_direccion["UserOverrideFlag"] = 'NO'
            componentes_direccion["LineaPatron"] = '639'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 78 E'
            componentes_direccion["UnhandledData"] = componentes_XXX[X]
            return componentes_direccion
        patron_37 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
            re.escape(T), re.escape(C))
        componentes_37 = verificar_patron(cadena, patron_37)
        if componentes_37 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_37[0])
            componentes_direccion["ViaPrincipal"] = componentes_37[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_37[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_37[3]
            componentes_direccion["NumeroPlaca"] = componentes_37[4]
            componentes_direccion["CuadranteAdicional"] = diccionario_C.get(componentes_37[5])
            componentes_direccion[
                "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|^[{}LEN<=3]|+="S",+="N",+="O",+="E"'
            componentes_direccion["LineaPatron"] = '640'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 47 78 S'
            componentes_direccion["UnhandledData"] = componentes_XXX[X]
            return componentes_direccion
        patron_93 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s*(.*)$'.format(
            re.escape(T),
            re.escape(C))
        componentes_93 = verificar_patron(cadena, patron_93)
        if componentes_93 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_93[0])
            componentes_direccion["ViaPrincipal"] = componentes_93[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_93[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_93[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_93[4]
            componentes_direccion["NumeroPlaca"] = componentes_93[5]
            componentes_direccion["CuadranteAdicional"] = diccionario_C.get(componentes_93[6])
            componentes_direccion[
                "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+="S",+="N",+="O",+="E"'
            componentes_direccion["LineaPatron"] = '1856'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B 76 S'
            componentes_direccion["UnhandledData"] = componentes_93[7]
            return componentes_direccion

    for T, D in product(diccionario_T.keys(), diccionario_D.keys()):

        patron_29 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                     re.escape(D))
        componentes_29 = verificar_patron(cadena, patron_29)
        if componentes_29 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_29[0])
            componentes_direccion["ViaPrincipal"] = componentes_29[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_29[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_29[3]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_29[4])
            componentes_direccion["NumeroPlaca"] = componentes_29[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|D|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '512'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 34 A 89 BIS 78'
            componentes_direccion["UnhandledData"] = componentes_29[6]
            return componentes_direccion
        patron_42 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D))
        componentes_42 = verificar_patron(cadena, patron_42)
        if componentes_42 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_42[0])
            componentes_direccion["ViaPrincipal"] = componentes_42[1]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_42[2])
            componentes_direccion["NumeroViaGeneradora"] = componentes_42[3]
            componentes_direccion["NumeroPlaca"] = componentes_42[4]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '725'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 BIS 47 76'
            componentes_direccion["UnhandledData"] = componentes_42[5]
            return componentes_direccion
        patron_53 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T), re.escape(D))
        componentes_53 = verificar_patron(cadena, patron_53)
        if componentes_53 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_53[0])
            componentes_direccion["ViaPrincipal"] = componentes_53[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_53[2]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_53[3])
            componentes_direccion["NumeroViaGeneradora"] = componentes_53[4]
            componentes_direccion["LetraViaGeneradora"] = componentes_53[5]
            componentes_direccion["NumeroPlaca"] = componentes_53[6]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|>[{}LEN<=4]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1004'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS 45B 76'
            componentes_direccion["UnhandledData"] = componentes_53[7]
            return componentes_direccion
        patron_55 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                     re.escape(D))
        componentes_55 = verificar_patron(cadena, patron_55)
        if componentes_55 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_55[0])
            componentes_direccion["ViaPrincipal"] = componentes_55[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_55[2]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_55[3])
            componentes_direccion["NumeroViaGeneradora"] = componentes_55[4]
            componentes_direccion["NumeroPlaca"] = componentes_55[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1043'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS 45 76'
            componentes_direccion["UnhandledData"] = componentes_55[6]
            return componentes_direccion
        patron_57 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T), re.escape(D))
        componentes_57 = verificar_patron(cadena, patron_57)
        if componentes_57 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_57[0])
            componentes_direccion["ViaPrincipal"] = componentes_57[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_57[2]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_57[3])
            componentes_direccion["LetraPrefijo"] = componentes_57[4]
            componentes_direccion["NumeroViaGeneradora"] = componentes_57[5]
            componentes_direccion["NumeroPlaca"] = componentes_57[6]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]|^[{}LEN<=3]|Z'
            componentes_direccion["LineaPatron"] = '1081'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A BIS B 45 76'
            componentes_direccion["UnhandledData"] = componentes_57[7]
            return componentes_direccion

        patron_82 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T), re.escape(D))
        componentes_82 = verificar_patron(cadena, patron_82)
        if componentes_82 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_82[0])
            componentes_direccion["ViaPrincipal"] = componentes_82[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_82[2]
            componentes_direccion["LetraViaGeneradora"] = componentes_82[3]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_82[4])
            componentes_direccion["NumeroPlaca"] = componentes_82[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1653'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A BIS 76'
            componentes_direccion["UnhandledData"] = componentes_82[6]
            return componentes_direccion
        patron_83 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T), re.escape(D))
        componentes_83 = verificar_patron(cadena, patron_83)
        if componentes_83 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_83[0])
            componentes_direccion["ViaPrincipal"] = componentes_83[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_83[2]
            componentes_direccion["LetraViaGeneradora"] = componentes_83[3]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_83[4])
            componentes_direccion["LetraSufijo"] = componentes_83[5]
            componentes_direccion["NumeroPlaca"] = componentes_83[6]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1670'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A BIS B 76'
            componentes_direccion["UnhandledData"] = componentes_83[7]
            return componentes_direccion
        patron_86 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T), re.escape(D))
        componentes_86 = verificar_patron(cadena, patron_86)
        if componentes_86 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_86[0])
            componentes_direccion["ViaPrincipal"] = componentes_86[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_86[2]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_86[3])
            componentes_direccion["NumeroPlaca"] = componentes_86[4]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|D|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1731'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 BIS 76'
            componentes_direccion["UnhandledData"] = componentes_86[5]
            return componentes_direccion
        patron_95 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T), re.escape(D))
        componentes_95 = verificar_patron(cadena, patron_95)
        if componentes_95 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_95[0])
            componentes_direccion["ViaPrincipal"] = componentes_95[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_95[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_95[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_95[4]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_95[5])
            componentes_direccion["NumeroPlaca"] = componentes_95[6]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|D|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1893'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B BIS 76'
            componentes_direccion["UnhandledData"] = componentes_95[7]
            return componentes_direccion
        patron_96 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T), re.escape(D))
        componentes_96 = verificar_patron(cadena, patron_96)
        if componentes_96 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_96[0])
            componentes_direccion["ViaPrincipal"] = componentes_96[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_96[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_96[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_96[4]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_96[5])
            componentes_direccion["LetraSufijo"] = componentes_96[6]
            componentes_direccion["NumeroPlaca"] = componentes_96[7]
            componentes_direccion[
                "InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|D|+[{}len=1]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1912'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B BIS C 76'
            componentes_direccion["UnhandledData"] = componentes_96[8]
            return componentes_direccion

        patron_164 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                   re.escape(D))
        componentes_164 = verificar_patron(cadena, patron_164)
        if componentes_164 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_164[0])
            componentes_direccion["ViaPrincipal"] = componentes_164[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_164[2]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_164[3])
            componentes_direccion["NumeroViaGeneradora"] = componentes_164[4]
            componentes_direccion["NumeroPlaca"] = componentes_164[5]
            componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3198'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 34B BIS 56 45'
            componentes_direccion["UnhandledData"] = componentes_164[6]
            return componentes_direccion

        patron_166 = r'^({})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                   re.escape(D))
        componentes_166 = verificar_patron(cadena, patron_166)
        if componentes_166 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_166[0])
            componentes_direccion["ViaPrincipal"] = componentes_166[1]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_166[2])
            componentes_direccion["NumeroViaGeneradora"] = componentes_166[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_166[4]
            componentes_direccion["NumeroPlaca"] = componentes_166[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|>[{}LEN<=3]|^[{}LEN<=3] - T|^[{}LEN<=3]|D|>[{}LEN=4]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3232 - 3763'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 4 BIS 45D 45'
            componentes_direccion["UnhandledData"] = componentes_166[6]
            return componentes_direccion

        patron_167 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T), re.escape(D))
        componentes_167 = verificar_patron(cadena, patron_167)
        if componentes_167 is not None:
            componentes_direccion["TipoVia"] = componentes_167[0]
            componentes_direccion["ViaPrincipal"] = componentes_167[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_167[2]
            componentes_direccion["Prefijo"] = componentes_167[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_167[4]
            componentes_direccion["LetraViaGeneradora"] = componentes_167[5]
            componentes_direccion["NumeroPlaca"] = componentes_167[6]
            componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|>[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3248'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 85D BIS 78M 48'
            componentes_direccion["UnhandledData"] = componentes_167[7]
            return componentes_direccion

        patron_178 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D))
        componentes_178 = verificar_patron(cadena, patron_178)
        if componentes_178 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_178[0])
            componentes_direccion["ViaPrincipal"] = componentes_178[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_178[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_178[3]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_178[4])
            componentes_direccion["NumeroPlaca"] = componentes_178[5]
            componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|^[{}LEN<=3]|D|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3459'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 45F 34 BIS 78'
            componentes_direccion["UnhandledData"] = componentes_178[6]
            return componentes_direccion

        patron_179 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D))
        componentes_179 = verificar_patron(cadena, patron_179)
        if componentes_179 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_179[0])
            componentes_direccion["ViaPrincipal"] = componentes_179[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_179[2]
            componentes_direccion["LetraViaGeneradora"] = componentes_179[3]
            componentes_direccion["Sufijo"] = diccionario_D.get(componentes_179[4])
            componentes_direccion["NumeroPlaca"] = componentes_179[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|>[{}LEN<=3]|D|^[{}LEN<=3] - '
            componentes_direccion["LineaPatron"] = '3475 - 3852'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 78 78E BIS 45'
            componentes_direccion["UnhandledData"] = componentes_179[6]
            return componentes_direccion

        patron_180 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D))
        componentes_180 = verificar_patron(cadena, patron_180)
        if componentes_180 is not None:
            componentes_direccion["TipoVia"] = componentes_180[0]
            componentes_direccion["ViaPrincipal"] = componentes_180[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_180[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_180[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_180[4]
            componentes_direccion["Sufijo"] = componentes_180[5]
            componentes_direccion["NumeroPlaca"] = componentes_180[6]
            componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|>[{}LEN<=3]|D|^[{}LEN<=3] - T|>[{}LEN<=3]|>[{}LEN=4]|D|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3491 - 3868'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 78M 23M BIS 45'
            componentes_direccion["UnhandledData"] = componentes_180[7]
            return componentes_direccion

        patron_191 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T), re.escape(D))
        componentes_191 = verificar_patron(cadena, patron_191)
        if componentes_191 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_191[0])
            componentes_direccion["ViaPrincipal"] = componentes_191[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_191[2]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_191[3])
            componentes_direccion["LetraPrefijo"] = componentes_191[4]
            componentes_direccion["NumeroViaGeneradora"] = componentes_191[5]
            componentes_direccion["NumeroPlaca"] = componentes_191[6]
            componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|D|+[{}LEN=1]|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3800'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 45D BIS A 45 45'
            componentes_direccion["UnhandledData"] = componentes_191[7]
            return componentes_direccion

        patron_194 = r'^({})\s+(\d{{1,3}})\s+({})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T),
                                                                                                      re.escape(D))
        componentes_194 = verificar_patron(cadena, patron_194)
        if componentes_194 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_194[0])
            componentes_direccion["ViaPrincipal"] = componentes_194[1]
            componentes_direccion["Prefijo"] = diccionario_D.get(componentes_194[2])
            componentes_direccion["LetraPrefijo"] = componentes_194[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_194[4]
            componentes_direccion["NumeroPlaca"] = componentes_194[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|D|+[{}LEN=1]|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3962'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 78 BIS A 78 45'
            componentes_direccion["UnhandledData"] = componentes_194[6]
            return componentes_direccion

    for T in diccionario_T.keys():

        patron_13 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{3}})\s*(.*)$'.format(
            re.escape(T))
        componentes_13 = verificar_patron(cadena, patron_13)
        if componentes_13 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_13[0])
            componentes_direccion["ViaPrincipal"] = componentes_13[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_13[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_13[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_13[4]
            componentes_direccion["NumeroPlaca"] = componentes_13[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}LEN=1]|>[{}LEN<=3]|>[{}LEN=6]'
            componentes_direccion["LineaPatron"] = '201'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 89G 345AQT'
            componentes_direccion["UnhandledData"] = componentes_13[7]
            return componentes_direccion
        patron_14 = r'^([A-Z]+)\s+([A-Z]+)\s+({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_14 = verificar_patron(cadena, patron_14)
        if componentes_14 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_14[2])
            componentes_direccion["ViaPrincipal"] = componentes_14[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_14[4]
            componentes_direccion["NumeroPlaca"] = componentes_14[5]
            componentes_direccion["UnhandledPattern"] = '++'
            componentes_direccion["UnhandledData"] = componentes_14[0] + " " + componentes_14[1]
            componentes_direccion["InputPattern"] = '+|+|T|^[{}LEN<=3]|^[{}len<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '218'
            componentes_direccion["DireccionEjemplo"] = 'Conjunt claros Calle 67 56 78'
            componentes_direccion["UnhandledData"] = componentes_14[6]
            return componentes_direccion
        patron_18 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T))
        componentes_18 = verificar_patron(cadena, patron_18)
        if componentes_18 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_18[0])
            componentes_direccion["ViaPrincipal"] = componentes_18[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_18[2] + ' ' + componentes_18[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_18[4]
            componentes_direccion["NumeroPlaca"] = componentes_18[5]
            componentes_direccion["InputPattern"] = 'T|^|+|+|^|^'
            componentes_direccion["LineaPatron"] = '285'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 67 A B 78 89'
            componentes_direccion["UnhandledData"] = componentes_18[6]
            return componentes_direccion
        patron_19 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]+)\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T))
        componentes_19 = verificar_patron(cadena, patron_19)
        if componentes_19 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_19[0])
            componentes_direccion["ViaPrincipal"] = componentes_19[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_19[2], componentes_19[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_19[4]
            componentes_direccion["LetraViaGeneradora"] = componentes_19[5]
            componentes_direccion["NumeroPlaca"] = componentes_19[6]
            componentes_direccion["InputPattern"] = 'T^++^+^'
            componentes_direccion["LineaPatron"] = '302'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 53 A B 78 A 90'
            componentes_direccion["UnhandledData"] = componentes_19[7]
            return componentes_direccion
        patron_20 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_20 = verificar_patron(cadena, patron_20)
        if componentes_20 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_20[0])
            componentes_direccion["ViaPrincipal"] = componentes_20[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_20[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_20[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_20[4]
            componentes_direccion["NumeroPlaca"] = componentes_20[5]
            componentes_direccion["InputPattern"] = 'T>>^ - T|>[{}LEN>=3]|>[{}LEN<=3]|^[{}LEN<=3] - T|>[{}LEN>=3]|>[{}LEN=4]|^[{}LEN<=3] - T|>[{}LEN>=3]|>[{}LEN>=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '306 - 3724 - 3738 - 3752'
            componentes_direccion["DireccionEjemplo"] = 'Calle 34A 456D 78'
            componentes_direccion["UnhandledData"] = componentes_20[6]
            return componentes_direccion
        patron_22 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+(\d{{1,3}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_22 = verificar_patron(cadena, patron_22)
        if componentes_22 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_22[0])
            componentes_direccion["ViaPrincipal"] = componentes_22[1] + " " + componentes_22[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_22[3]
            componentes_direccion["NumeroPlaca"] = componentes_22[4]
            componentes_direccion["UnhandledPattern"] = '^'
            componentes_direccion["UnhandledData"] = componentes_22[5]
            componentes_direccion["InputPattern"] = 'T++^^^'
            componentes_direccion["LineaPatron"] = '376'
            componentes_direccion["DireccionEjemplo"] = 'Calle celestino mutis 63 67 45'
            componentes_direccion["UnhandledData"] = componentes_22[6]
            return componentes_direccion
        patron_23 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T))
        componentes_23 = verificar_patron(cadena, patron_23)
        if componentes_23 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_23[0])
            componentes_direccion["ViaPrincipal"] = componentes_23[1] + " " + componentes_23[2] + " " + componentes_23[
                3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_23[4]
            componentes_direccion["LetraViaGeneradora"] = componentes_23[5]
            componentes_direccion["NumeroPlaca"] = componentes_23[6]
            componentes_direccion["InputPattern"] = 'T+++^+^'
            componentes_direccion["LineaPatron"] = '393'
            componentes_direccion["DireccionEjemplo"] = 'Calle jose celestino mutis 78 A 45'
            componentes_direccion["UnhandledData"] = componentes_23[7]
            return componentes_direccion
        patron_24 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_24 = verificar_patron(cadena, patron_24)
        if componentes_24 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_24[0])
            componentes_direccion["ViaPrincipal"] = componentes_24[1] + " " + componentes_24[2] + " " + componentes_24[
                3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_24[4]
            componentes_direccion["NumeroPlaca"] = componentes_24[5]
            componentes_direccion["InputPattern"] = 'T+++^^'
            componentes_direccion["LineaPatron"] = '433'
            componentes_direccion["DireccionEjemplo"] = 'AV jose celestino mutis 78  45'
            componentes_direccion["UnhandledData"] = componentes_24[6]
            return componentes_direccion
        patron_25 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_25 = verificar_patron(cadena, patron_25)
        if componentes_25 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_25[0])
            componentes_direccion["ViaPrincipal"] = componentes_25[1] + " " + componentes_25[2] + " " + \
                                                    componentes_25[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_25[4]
            componentes_direccion["InputPattern"] = 'T+++^'
            componentes_direccion["LineaPatron"] = '451'
            componentes_direccion["DireccionEjemplo"] = 'AV jose celestino mutis 78'
            componentes_direccion["UnhandledData"] = componentes_25[5]
            return componentes_direccion
        patron_27 = r'^({})\s+([A-Z]+)\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_27 = verificar_patron(cadena, patron_27)
        if componentes_27 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_27[0])
            componentes_direccion["ViaPrincipal"] = componentes_27[2]
            componentes_direccion["LetraViaGeneradora"] = componentes_27[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_27[4]
            componentes_direccion["UnhandledPattern"] = '+'
            componentes_direccion["UnhandledData"] = componentes_27[1]
            componentes_direccion["InputPattern"] = 'T|+|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '488'
            componentes_direccion["DireccionEjemplo"] = 'AV rojas 34 A 45'
            componentes_direccion["UnhandledData"] = componentes_27[5]
            return componentes_direccion
        patron_28 = r'^({})\s+([A-Z]+)\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_28 = verificar_patron(cadena, patron_28)
        if componentes_28 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_28[0])
            componentes_direccion["ViaPrincipal"] = componentes_28[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_28[2]
            componentes_direccion["NumeroPlaca"] = componentes_28[3]
            componentes_direccion["InputPattern"] = 'T|+|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '501'
            componentes_direccion["DireccionEjemplo"] = 'AV CHILE 63 67'
            componentes_direccion["UnhandledData"] = componentes_28[4]
            return componentes_direccion
        patron_36 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_36 = verificar_patron(cadena, patron_36)
        if componentes_36 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_36[0])
            componentes_direccion["ViaPrincipal"] = componentes_36[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_36[2]
            componentes_direccion["NumeroPlaca"] = componentes_36[3]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["UserOverrideFlag"] = 'NO'
            componentes_direccion["LineaPatron"] = '624'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 78'
            componentes_direccion["UnhandledData"] = componentes_36[4]
            return componentes_direccion
        patron_38 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_38 = verificar_patron(cadena, patron_38)
        if componentes_38 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_38[0])
            componentes_direccion["ViaPrincipal"] = componentes_38[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_38[2]
            componentes_direccion["Cuadrante"] = componentes_38[3]
            componentes_direccion["NumeroViaGeneradora"] = componentes_38[4]
            componentes_direccion["NumeroPlaca"] = componentes_38[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=2]|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '658'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 AB 47 78'
            componentes_direccion["UnhandledData"] = componentes_38[6]
            return componentes_direccion
        patron_39 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_39 = verificar_patron(cadena, patron_39)
        if componentes_39 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_39[0])
            componentes_direccion["ViaPrincipal"] = componentes_39[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_39[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_39[3]
            componentes_direccion["NumeroPlaca"] = componentes_39[4]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '677'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 47 78'
            componentes_direccion["UnhandledData"] = componentes_39[5]
            return componentes_direccion

        patron_68 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_68 = verificar_patron(cadena, patron_68)
        if componentes_68 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_68[0])
            componentes_direccion["ViaPrincipal"] = componentes_68[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_68[2]
            componentes_direccion["LetraViaGeneradora"] = componentes_68[3]
            componentes_direccion["NumeroPlaca"] = componentes_68[4]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1306'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 45 A 76'
            componentes_direccion["UnhandledData"] = componentes_68[5]
            return componentes_direccion
        patron_94 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(
            re.escape(T))
        componentes_94 = verificar_patron(cadena, patron_94)
        if componentes_94 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_94[0])
            componentes_direccion["ViaPrincipal"] = componentes_94[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_94[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_94[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_94[4]
            componentes_direccion["NumeroPlaca"] = componentes_94[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]|+[{}len=1]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '1875'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 80 A 45 B 76'
            componentes_direccion["UnhandledData"] = componentes_94[6]
            return componentes_direccion

        patron_156 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s+([NSOE])\s*(.*)$'.format(re.escape(T))
        componentes_156 = verificar_patron(cadena, patron_156)

        if componentes_156 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_156[0])
            componentes_direccion["ViaPrincipal"] = componentes_156[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_156[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_156[3]
            componentes_direccion["NumeroPlaca"] = componentes_156[4]
            componentes_direccion["CuadranteAdicional"] = componentes_156[5]
            componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|^[{}LEN<=3]|^[{}LEN<=3]|+="S",+="N",+="O",+="E"'
            componentes_direccion["LineaPatron"] = '3065'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 56A 45 45 S'
            componentes_direccion["UnhandledData"] = componentes_156[6]
            return componentes_direccion

        patron_159 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_159 = verificar_patron(cadena, patron_159)
        if componentes_159 is not None:
            componentes_direccion["TipoVia"] = componentes_159[0]
            componentes_direccion["ViaPrincipal"] = componentes_159[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_159[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_159[3]
            componentes_direccion["NumeroPlaca"] = componentes_159[4]
            componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3116'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 35B 56 56'
            componentes_direccion["UnhandledData"] = componentes_159[5]
            return componentes_direccion

        patron_160 = r'^({})\s+(\d{{1,3}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_160 = verificar_patron(cadena, patron_160)
        if componentes_160 is not None:
            componentes_direccion["TipoVia"] = componentes_160[0]
            componentes_direccion["ViaPrincipal"] = componentes_160[1]
            componentes_direccion["NumeroViaGeneradora"] = componentes_160[2]
            componentes_direccion["LetraViaGeneradora"] = componentes_160[3]
            componentes_direccion["NumeroPlaca"] = componentes_160[4]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|>[{}LEN<=3]|^[{}LEN<=3] - T|^[{}LEN<=3]|>[{}LEN=4]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3130 - 3710'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 3 45B 56'
            componentes_direccion["UnhandledData"] = componentes_160[5]
            return componentes_direccion

        patron_186 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})(.*)'.format(re.escape(T))
        componentes_186 = verificar_patron(cadena, patron_186)
        if componentes_186 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_186[0])
            componentes_direccion["ViaPrincipal"] = componentes_186[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_186[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_186[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_186[4]
            componentes_direccion["NumeroPlaca"] = componentes_186[5]
            componentes_direccion["UnhandledData"] = componentes_186[6]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}LEN=1]|^[{}LEN<=3]|+|>[{}LEN=6]'
            componentes_direccion["LineaPatron"] = '3629'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 45 F 45 A 78DRET'
            return componentes_direccion

        patron_187 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_187 = verificar_patron(cadena, patron_187)
        if componentes_187 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_187[0])
            componentes_direccion["ViaPrincipal"] = componentes_187[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_187[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_187[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_187[4]
            componentes_direccion["NumeroPlaca"] = componentes_187[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}LEN=1]|<[{}LEN=4]|^[{}LEN<=3] - T|^[{}LEN<=3]|+[{}LEN=1]|>[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3647 - 3678'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 4 A 78D 45'
            return componentes_direccion

        patron_188 = r'^({})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_188 = verificar_patron(cadena, patron_188)
        if componentes_188 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_188[0])
            componentes_direccion["ViaPrincipal"] = componentes_188[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_188[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_188[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_188[4]
            componentes_direccion["NumeroPlaca"] = componentes_188[5]
            componentes_direccion["InputPattern"] = 'T|^[{}LEN<=3]|+[{}LEN=1]|>[{}LEN=4]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '3662'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 78 A 89S 78'
            componentes_direccion["UnhandledData"] = componentes_188[6]
            return componentes_direccion

        patron_198 = r'^({})\s+(\d{{1,3}})([A-Z]{{1}})\s+(\d{{1,3}})\s+([A-Z]{{1}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_198 = verificar_patron(cadena, patron_198)
        if componentes_198 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_198[0])
            componentes_direccion["ViaPrincipal"] = componentes_198[1]
            componentes_direccion["LetraViaPrincipal"] = componentes_198[2]
            componentes_direccion["NumeroViaGeneradora"] = componentes_198[3]
            componentes_direccion["LetraViaGeneradora"] = componentes_198[4]
            componentes_direccion["NumeroPlaca"] = componentes_198[5]
            componentes_direccion["InputPattern"] = 'T|>[{}LEN<=3]|^[{}LEN<=3]|+[{}LEN=1]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '4082'
            componentes_direccion["DireccionEjemplo"] = 'CALLE 78D 78 A 78'
            componentes_direccion["UnhandledData"] = componentes_198[6]
            return componentes_direccion

        patron_203 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+(\d{{1,3}})\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_203 = verificar_patron(cadena, patron_203)
        if componentes_203 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_203[0])
            componentes_direccion["ViaPrincipal"] = componentes_203[1] + ' ' + componentes_203[2] + ' ' + \
                                                    componentes_203[3] + ' ' + componentes_203[4] + ' ' + \
                                                    componentes_203[5]
            componentes_direccion["NumeroViaGeneradora"] = componentes_203[6]
            componentes_direccion["NumeroPlaca"] = componentes_203[7]
            componentes_direccion["InputPattern"] = 'T|+|+|+|+|+|^[{}LEN<=3]|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '4185'
            componentes_direccion["DireccionEjemplo"] = 'CALLE JOSE ALFREDO JIMENEZ CELESTINO MUTIS 345 345'
            componentes_direccion["UnhandledData"] = componentes_203[8]
            return componentes_direccion

        patron_204 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+(\d{{1,3}})\s+([A-Z]+)\s+(\d{{1,3}})\s*(.*)$'.format(re.escape(T))
        componentes_204 = verificar_patron(cadena, patron_204)
        if componentes_204 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_204[0])
            componentes_direccion["ViaPrincipal"] = componentes_204[1] + ' ' + componentes_204[2] + ' ' + \
                                                    componentes_204[3] + ' ' + componentes_204[4] + ' ' + \
                                                    componentes_204[5]
            componentes_direccion["NumeroViaGeneradora"] = componentes_204[6]
            componentes_direccion["LetraViaGeneradora"] = componentes_204[7]
            componentes_direccion["NumeroPlaca"] = componentes_204[8]
            componentes_direccion["InputPattern"] = 'T|+|+|+|+|+|^[{}LEN<=3]|+|^[{}LEN<=3]'
            componentes_direccion["LineaPatron"] = '4211'
            componentes_direccion["DireccionEjemplo"] = 'CALLE JOSE CELESTINO MUTIS FABIAN ROMERO 345 AW 398'
            componentes_direccion["UnhandledData"] = componentes_204[9]
            return componentes_direccion

        patron_206 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s*(.*)$'.format(re.escape(T))
        componentes_206 = verificar_patron(cadena, patron_206)
        if componentes_206 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_206[0])
            componentes_direccion["ViaPrincipal"] = componentes_206[1] + ' ' + componentes_206[2] + ' ' +  componentes_206[3] +  ' ' + componentes_206[4]
            componentes_direccion["InputPattern"] = 'T|+|+|+|+'
            componentes_direccion["LineaPatron"] = '4258'
            componentes_direccion["DireccionEjemplo"] = 'CALLE JOSE CELESTINO MUTIS HERNANDEZ'
            componentes_direccion["UnhandledData"] = componentes_206[5]
            return componentes_direccion

        patron_207 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s*(.*)$'.format(re.escape(T))
        componentes_207 = verificar_patron(cadena, patron_207)
        if componentes_207 is not None:
            componentes_direccion["TipoVia"] = diccionario_T.get(componentes_207[0])
            componentes_direccion["ViaPrincipal}"] = componentes_207[1] + ' ' + componentes_207[2] + ' ' +  componentes_207[3]
            componentes_direccion["InputPattern"] = 'T|+|+|+'
            componentes_direccion["LineaPatron"] = '4277'
            componentes_direccion["DireccionEjemplo"] = 'CALLE JOSE CELESTINO MUTIS'
            componentes_direccion["UnhandledData"] = componentes_207[4]
            return componentes_direccion

    componentes_direccion["UnhandledData"] = cadena

    return componentes_direccion

