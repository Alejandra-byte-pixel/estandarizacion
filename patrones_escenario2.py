import re
from itertools import product
import diccionarios_escenario2

diccionario_B_Full = diccionarios_escenario2.get_b()
diccionario_U_Full = diccionarios_escenario2.get_u()
diccionario_M_Full = diccionarios_escenario2.get_m()
diccionario_L_Full = diccionarios_escenario2.get_l()
diccionario_R_Full = diccionarios_escenario2.get_r()
diccionario_F_Full = diccionarios_escenario2.get_f()
diccionario_C_Full = diccionarios_escenario2.get_c()
diccionario_T_Full = diccionarios_escenario2.get_t()


def get_diccionario_B(cadena):
    diccionario_B = {}
    for b, b2 in product(diccionario_B_Full.keys(), diccionario_B_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(b), re.escape(b2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_B[b] = diccionario_B_Full[b]
            diccionario_B[b2] = diccionario_B_Full[b2]

    for b in diccionario_B_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(b))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_B[b] = diccionario_B_Full[b]

    print('B = ')
    print(diccionario_B)
    return diccionario_B


def get_diccionario_U(cadena):
    diccionario_U = {}
    for u, u2 in product(diccionario_U_Full.keys(), diccionario_U_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(u), re.escape(u2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_U[u] = diccionario_U_Full[u]
            diccionario_U[u2] = diccionario_U_Full[u2]

    for u in diccionario_U_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(u))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_U[u] = diccionario_U_Full[u]
    print('U = ')
    print(diccionario_U)
    return diccionario_U


def get_diccionario_M(cadena):
    diccionario_M = {}
    for m, m2 in product(diccionario_M_Full.keys(), diccionario_M_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(m), re.escape(m2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_M[m] = diccionario_M_Full[m]
            diccionario_M[m2] = diccionario_M_Full[m2]

    for m in diccionario_M_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(m))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_M[m] = diccionario_M_Full[m]

    print('M = ')
    print(diccionario_M)
    return diccionario_M


def get_diccionario_L(cadena):
    diccionario_L = {}
    for l, l2 in product(diccionario_L_Full.keys(), diccionario_L_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(l), re.escape(l2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_L[l] = diccionario_L_Full[l]
            diccionario_L[l2] = diccionario_L_Full[l2]

    for l in diccionario_L_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(l))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_L[l] = diccionario_L_Full[l]

    print('L = ')
    print(diccionario_L)
    return diccionario_L


def get_diccionario_R(cadena):
    diccionario_R = {}
    for r, r2 in product(diccionario_R_Full.keys(), diccionario_R_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(r), re.escape(r2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_R[r] = diccionario_R_Full[r]
            diccionario_R[r2] = diccionario_R_Full[r2]

    for r in diccionario_R_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(r))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_R[r] = diccionario_R_Full[r]

    print('R = ')
    print(diccionario_R)
    return diccionario_R


def get_diccionario_F(cadena):
    diccionario_F = {}
    for f, f2 in product(diccionario_F_Full.keys(), diccionario_F_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(f), re.escape(f2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_F[f] = diccionario_F_Full[f]
            diccionario_F[f2] = diccionario_F_Full[f2]

    for f in diccionario_F_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(f))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_F[f] = diccionario_F_Full[f]

    print('F = ')
    print(diccionario_F)
    return diccionario_F


def get_diccionario_C(cadena):
    diccionario_C = {}
    for c, c2 in product(diccionario_C_Full.keys(), diccionario_C_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(c), re.escape(c2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_C[c] = diccionario_C_Full[c]
            diccionario_C[c2] = diccionario_C_Full[c2]

    for c in diccionario_C_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(c))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_C[c] = diccionario_C_Full[c]

    print('C = ')
    print(diccionario_C)
    return diccionario_C


def get_diccionario_T(cadena):
    diccionario_T = {}
    for t, t2 in product(diccionario_T_Full.keys(), diccionario_T_Full.keys()):
        patron = r'^(.*){}\s+(.*){}(.*)'.format(re.escape(t), re.escape(t2))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_T[t] = diccionario_T_Full[t]
            diccionario_T[t2] = diccionario_T_Full[t2]

    for t in diccionario_T_Full.keys():
        patron = r'^(.*){}(.*)'.format(re.escape(t))
        busqueda = re.search(patron, cadena)
        if busqueda:
            diccionario_T[t] = diccionario_T_Full[t]

    print('T = ')
    print(diccionario_T)
    return diccionario_T


def verificar_patron_escenario2(cadena, patron):
    busqueda = re.search(patron, cadena)
    if busqueda:
        return busqueda.groups()
    else:
        return None


def extraer_componentes_direccion_escenario2(cadena):
    diccionario_B = get_diccionario_B(cadena)
    diccionario_U = get_diccionario_U(cadena)
    diccionario_M = get_diccionario_M(cadena)
    diccionario_L = get_diccionario_L(cadena)
    diccionario_R = get_diccionario_R(cadena)
    diccionario_F = get_diccionario_F(cadena)
    diccionario_C = get_diccionario_C(cadena)
    diccionario_T = get_diccionario_T(cadena)
    componentes_direccion_escenario2 = {
        "Barrio": "",
        "Urbanizacion": "",
        "NombreUrbanizacion": "",
        "TipoPiso": "",
        "NumeroPiso": "",
        "Manzana": "",
        "TipoPredio": "",
        "Casa": "",
        "LoteParcela": "",
        "Sector": "",
        "Kilometro": "",
        "IdentificadorPredio": "",
        "UnhandledPattern": "",
        "UnhandledData": "",
        "InputPattern": "",
        "UserOverrideFlag": "",
        "LineaPatron": "",
        "DireccionEjemplo": ""
    }

    ####### Empieza 5 Diccionarios #######

    if diccionario_L is not None and diccionario_U is not None and diccionario_B is not None:
        for L, U, U2, B, L2 in product(diccionario_L.keys(), diccionario_U.keys(), diccionario_U.keys(),
                                       diccionario_B.keys(), diccionario_L.keys()):
            patron_34 = r'^({})\s+(\d+)\s+({})\s+(\d+)\s+({})\s+({})\s+(.*)'.format(re.escape(L), re.escape(U),
                                                                                    re.escape(U2), re.escape(B))
            componentes_34 = verificar_patron_escenario2(cadena, patron_34)
            if componentes_34 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_34[0]) + ' ' + \
                                                                 componentes_34[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_34[2]) + ' ' + \
                                                                   componentes_34[3] + ' ' + diccionario_U.get(
                    componentes_34[4]) + ' ' + diccionario_B.get(componentes_34[5]) + ' ' + componentes_34[6]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|U|^|U|B|?'
                componentes_direccion_escenario2["LineaPatron"] = '875'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION 29 CONDOMINIO BARRIO PELIGROSO'
                return componentes_direccion_escenario2

    if diccionario_F is not None and diccionario_M is not None and diccionario_B is not None:
        for F, M, B, M2, B2 in product(diccionario_F.keys(), diccionario_M.keys(), diccionario_B.keys(),
                                       diccionario_M.keys(), diccionario_B.keys()):
            patron_12 = r'^({})\s+(\d+)\s+({})\s+({})\s+({})\s+([A-Z]+)\s+({})$'.format(re.escape(F), re.escape(M),
                                                                                        re.escape(B), re.escape(M2),
                                                                                        re.escape(B2))
            componentes_12 = verificar_patron_escenario2(cadena, patron_12)
            if componentes_12 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_12[0]) + ' ' + \
                                                                 componentes_12[1]
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(
                    componentes_12[3]) + ' ' + diccionario_M.get(componentes_12[4]) + ' ' + componentes_12[
                                                                 5] + ' ' + diccionario_B.get(componentes_12[6])
                componentes_direccion_escenario2["UnhandledData"] = componentes_12[2]
                componentes_direccion_escenario2["InputPattern"] = 'F|^|M|B|M|+|B'
                componentes_direccion_escenario2["LineaPatron"] = '1391'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 8 EDIFICIO CIUDADELA MODULO NEGRO CD'
                return componentes_direccion_escenario2

    ####### Empieza 4 Diccionarios #######

    if diccionario_M is not None and diccionario_L is not None and diccionario_U is not None and diccionario_B is not None:
        for M, L, U, B in product(diccionario_M.keys(), diccionario_L.keys(), diccionario_U.keys(),
                                  diccionario_B.keys()):
            patron_22 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)\s+({})'.format(re.escape(M), re.escape(L),
                                                                                  re.escape(U), re.escape(B))
            componentes_22 = verificar_patron_escenario2(cadena, patron_22)
            if componentes_22 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_22[0]) + ' ' + \
                                                              componentes_22[1]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_22[2]) + ' ' + \
                                                                 componentes_22[3]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_22[4]) + ' ' + \
                                                                   componentes_22[5] + ' ' + diccionario_B.get(
                    componentes_22[6])
                componentes_direccion_escenario2["InputPattern"] = 'M|&|L|&|U|?|B'
                componentes_direccion_escenario2["LineaPatron"] = '525'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'VEREDA EL ROBLE ESTACION GASOLINA UNIDADRESIDENCIAL FORTALEZA CIUDADELA'
                return componentes_direccion_escenario2

        for L, U, U2, L2 in product(diccionario_L.keys(), diccionario_U.keys(), diccionario_U.keys(),
                                    diccionario_L.keys()):
            patron_35 = r'^({})\s+(\d+)\s+({})\s+(\d+)\s+({})\s+({})\s+(.*)\s+(\d+)'.format(re.escape(L), re.escape(U),
                                                                                            re.escape(U2),
                                                                                            re.escape(L2))
            componentes_35 = verificar_patron_escenario2(cadena, patron_35)
            if componentes_35 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_35[0]) + ' ' + \
                                                                 componentes_35[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_35[2]) + ' ' + \
                                                                   componentes_35[3] + ' ' + diccionario_U.get(
                    componentes_35[4]) + ' ' + diccionario_L.get(componentes_35[5]) + ' ' + componentes_35[6] + ' ' + \
                                                                   componentes_35[7]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|U|^|U|L|?|^'
                componentes_direccion_escenario2["LineaPatron"] = '901'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION 29 CONDOMINIO ENTRADA COLORINES 2'
                return componentes_direccion_escenario2

            patron_36 = r'^({})\s+(\d+)\s+({})\s+(\d+)\s+({})\s+({})\s+(.*)'.format(re.escape(L), re.escape(U),
                                                                                    re.escape(U2), re.escape(L2))
            componentes_36 = verificar_patron_escenario2(cadena, patron_36)
            if componentes_36 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_36[0]) + ' ' + \
                                                                 componentes_36[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_36[2]) + ' ' + \
                                                                   componentes_36[3] + ' ' + diccionario_U.get(
                    componentes_36[4]) + ' ' + diccionario_L.get(componentes_36[5]) + ' ' + componentes_36[6]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|U|^|U|L|?'
                componentes_direccion_escenario2["LineaPatron"] = '930'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION 29 CONDOMINIO ENTRADA COLORINES'
                return componentes_direccion_escenario2

    if diccionario_B is not None and diccionario_U is not None and diccionario_M is not None and diccionario_L is not None:
        for B, U, M, L in product(diccionario_B.keys(), diccionario_U.keys(), diccionario_M.keys(),
                                  diccionario_L.keys()):
            patron_190 = r'^({})\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+(\d+)\s+({})\s+(\d+)$'.format(
                re.escape(B), re.escape(U), re.escape(M), re.escape(L))
            componentes_190 = verificar_patron_escenario2(cadena, patron_190)
            if componentes_190 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_190[0]) + ' ' + \
                                                             componentes_190[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_190[2]) + ' ' + \
                                                                   componentes_190[3] + ' ' + componentes_190[4]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_190[5]) + ' ' + \
                                                              componentes_190[6]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_190[7]) + ' ' + \
                                                                 componentes_190[8]
                componentes_direccion_escenario2["InputPattern"] = 'B|+|U|+|+|M|^|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '008'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'BARRIO NORMANDIA CONJUNTO LOS LAGARTOS TORRE 2 APARTAMENTO 102'
                return componentes_direccion_escenario2

    if diccionario_M is not None and diccionario_L is not None and diccionario_C is not None:
        for M, M2, L, C in product(diccionario_M.keys(), diccionario_M.keys(), diccionario_L.keys(),
                                   diccionario_C.keys()):
            patron_2 = r'^({})\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+({})\s+(\d+)([A-Z]+)\s+({})\s+([A-Z]+)$'.format(
                re.escape(M), re.escape(M2), re.escape(L), re.escape(C))
            componentes_2 = verificar_patron_escenario2(cadena, patron_2)
            if componentes_2 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_2[0]) + ' ' + componentes_2[
                    1] + ' ' + diccionario_M.get(componentes_2[2]) + ' ' + componentes_2[3]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_2[4]) + ' ' + \
                                                                 componentes_2[5] + ' ' + componentes_2[6]
                componentes_direccion_escenario2["TipoPiso"] = diccionario_C.get(componentes_2[7]) + ' ' + \
                                                               componentes_2[8]
                componentes_direccion_escenario2["InputPattern"] = 'M|+|M|+|L|>|C|+'
                componentes_direccion_escenario2["LineaPatron"] = '592'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'EDIFICIO GIRASOLES TORRE AZUL APARTAMENTO 6A PISO UNO'
                return componentes_direccion_escenario2

    if diccionario_M is not None and diccionario_R is not None and diccionario_U is not None:
        for M, R, U, U2 in product(diccionario_M.keys(), diccionario_R.keys(), diccionario_U.keys(),
                                   diccionario_U.keys()):
            patron_15 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(R),
                                                                                         re.escape(U), re.escape(U2))
            componentes_15 = verificar_patron_escenario2(cadena, patron_15)
            if componentes_15 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_15[0]) + ' ' + \
                                                              componentes_15[1]
                componentes_direccion_escenario2["Casa"] = diccionario_R.get(componentes_15[2]) + ' ' + componentes_15[
                    3]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_15[4]) + ' ' + \
                                                                   componentes_15[5] + ' ' + diccionario_U.get(
                    componentes_15[6]) + ' ' + componentes_15[7]
                componentes_direccion_escenario2["InputPattern"] = 'M|&|R|&|U|*?|U|&'
                componentes_direccion_escenario2["LineaPatron"] = '262'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'MANZANA CUADRADA CASA VERDE CONDOMINIO LOS ALMENDROS BLOQUE PERDIDO'
                return componentes_direccion_escenario2

        for M, R, U, M2 in product(diccionario_M.keys(), diccionario_R.keys(), diccionario_U.keys(),
                                   diccionario_M.keys()):
            patron_14 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(R),
                                                                                         re.escape(U), re.escape(M2))
            componentes_14 = verificar_patron_escenario2(cadena, patron_14)
            if componentes_14 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_14[0]) + ' ' + \
                                                              componentes_14[1]
                componentes_direccion_escenario2["Casa"] = diccionario_R.get(componentes_14[2]) + ' ' + componentes_14[
                    3]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_14[4]) + ' ' + \
                                                                   componentes_14[5] + ' ' + diccionario_M.get(
                    componentes_14[6]) + ' ' + componentes_14[7]
                componentes_direccion_escenario2["InputPattern"] = 'M|&|R|&|U|&|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '235'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MZ SINFIN CASA AZUL URB ROJA MODULO AMARILLA'
                return componentes_direccion_escenario2

    if diccionario_M is not None and diccionario_R is not None and diccionario_L is not None:
        for M, R, L, M2 in product(diccionario_M.keys(), diccionario_R.keys(), diccionario_L.keys(),
                                   diccionario_M.keys()):
            patron_16 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(R),
                                                                                         re.escape(L), re.escape(M2))
            componentes_16 = verificar_patron_escenario2(cadena, patron_16)
            if componentes_16 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_16[0]) + ' ' + \
                                                              componentes_16[1]
                componentes_direccion_escenario2["Casa"] = diccionario_R.get(componentes_16[2]) + ' ' + componentes_16[
                    3]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_L.get(componentes_16[4]) + ' ' + \
                                                                   componentes_16[5] + ' ' + diccionario_M.get(
                    componentes_16[6]) + ' ' + componentes_16[7]
                componentes_direccion_escenario2["InputPattern"] = 'M|&|R|&|L|&|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '291'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'EDIFICIO QUINTA AVENIDA CASA 34 CONSULTORIO 302 KILOMETRO 100'
                return componentes_direccion_escenario2

    ####### Empieza 3 Diccionarios #######

    if diccionario_U is not None and diccionario_L is not None and diccionario_B is not None:
        for U, L, B in product(diccionario_U.keys(), diccionario_L.keys(), diccionario_B.keys()):
            patron_323 = r'^({})\s+({})\s+(.*)\s+(\d+)\s+({})\s+(.*)$'.format(re.escape(U), re.escape(L), re.escape(B))
            componentes_323 = verificar_patron_escenario2(cadena, patron_323)
            if componentes_323 is not None:
                componentes_direccion_escenario2["NombreUrbanizacion"] = re.sub(r'\s+', ' ',
                                                                                f"{diccionario_U.get(componentes_323[0])}  {diccionario_L.get(componentes_323[1])} {componentes_323[2]} {componentes_323[3]}")
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_323[4])}  {componentes_323[5]}")
                componentes_direccion_escenario2["InputPattern"] = 'U|L|?|^|B|?'
                componentes_direccion_escenario2["LineaPatron"] = '2131'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'CONJUNTO APARTAMENTO LOS LAGARTOS 53 BARRIO CASTILLA'
                return componentes_direccion_escenario2

        for U, U2, B in product(diccionario_U.keys(), diccionario_U.keys(), diccionario_B.keys()):
            patron_65 = r'^({})\s+(\d+)\s+({})\s+({})\s+(.*)'.format(re.escape(U), re.escape(U2), re.escape(B))
            componentes_65 = verificar_patron_escenario2(cadena, patron_65)
            if componentes_65 is not None:
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_65[0]) + ' ' + \
                                                                   componentes_65[1] + ' ' + diccionario_U.get(
                    componentes_65[2]) + ' ' + diccionario_B.get(componentes_65[3]) + ' ' + componentes_65[4]
                componentes_direccion_escenario2["InputPattern"] = '*U|^|U|B|?'
                componentes_direccion_escenario2["LineaPatron"] = '1572'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'URBANIZACION 2 CONDOMINIO BARRIO CORMONARES'
                return componentes_direccion_escenario2

        for L, U, B in product(diccionario_L.keys(), diccionario_U.keys(), diccionario_B.keys()):
            patron_39 = r'^({})\s+(\d+)\s+({})\s+({})\s+(.*)'.format(re.escape(L), re.escape(U), re.escape(B))
            componentes_39 = verificar_patron_escenario2(cadena, patron_39)
            if componentes_39 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_39[0]) + ' ' + \
                                                                 componentes_39[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(
                    componentes_39[2]) + ' ' + diccionario_B.get(componentes_39[3]) + ' ' + componentes_39[4]
                componentes_direccion_escenario2["InputPattern"] = 'L|^|U|B|*?'
                componentes_direccion_escenario2["LineaPatron"] = '994'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION BARRIO COLORINES'
                return componentes_direccion_escenario2

        for L, U, U2 in product(diccionario_L.keys(), diccionario_U.keys(), diccionario_U.keys()):
            patron_37 = r'^({})\s+(\d+)\s+({})\s+(\d+)\s+({})\s+(.*)'.format(re.escape(L), re.escape(U), re.escape(U2))
            componentes_37 = verificar_patron_escenario2(cadena, patron_37)
            if componentes_37 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_37[0]) + ' ' + \
                                                                 componentes_37[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_37[2]) + ' ' + \
                                                                   componentes_37[3] + ' ' + diccionario_U.get(
                    componentes_37[4]) + ' ' + componentes_37[5]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|U|^|U|?'
                componentes_direccion_escenario2["LineaPatron"] = '956'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION 29 CONDOMINIO COLORINES'
                return componentes_direccion_escenario2

        for L, U, L2 in product(diccionario_L.keys(), diccionario_U.keys(), diccionario_L.keys()):
            patron_41 = r'^({})\s+(\d+)\s+({})\s+({})\s+(\d+)'.format(re.escape(L), re.escape(U), re.escape(L2))
            componentes_41 = verificar_patron_escenario2(cadena, patron_41)
            if componentes_41 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_41[0]) + ' ' + \
                                                                 componentes_41[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(
                    componentes_41[2]) + ' ' + diccionario_L.get(componentes_41[3]) + ' ' + componentes_41[4]
                componentes_direccion_escenario2["InputPattern"] = 'L|^|U|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '1032'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION PORTERIA 10'
                return componentes_direccion_escenario2

            patron_42 = r'^({})\s+(\d+)\s+({})\s+({})\s+(.*)'.format(re.escape(L), re.escape(U), re.escape(L2))
            componentes_42 = verificar_patron_escenario2(cadena, patron_42)
            if componentes_42 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_42[0]) + ' ' + \
                                                                 componentes_42[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(
                    componentes_42[2]) + ' ' + diccionario_L.get(componentes_42[3]) + ' ' + componentes_42[4]
                componentes_direccion_escenario2["InputPattern"] = 'L|^|U|L|?'
                componentes_direccion_escenario2["LineaPatron"] = '1050'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION PORTERIA COLORADA'
                return componentes_direccion_escenario2

        for U, L, L2 in product(diccionario_U.keys(), diccionario_L.keys(), diccionario_L.keys()):
            patron_40 = r'^({})\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(U), re.escape(L), re.escape(L2))
            componentes_40 = verificar_patron_escenario2(cadena, patron_40)
            if componentes_40 is not None:
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(
                    componentes_40[0]) + ' ' + diccionario_L.get(componentes_40[1]) + ' ' + componentes_40[2]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_40[3]) + ' ' + \
                                                                 componentes_40[4]
                componentes_direccion_escenario2["InputPattern"] = 'U|L|?|L|&'
                componentes_direccion_escenario2["LineaPatron"] = '1013'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'URBANIZACION APARTAMENTO 102 PORTERIA COLORINES'
                return componentes_direccion_escenario2

    if diccionario_B is not None and diccionario_M is not None and diccionario_L is not None:
        for B, M, L in product(diccionario_B.keys(), diccionario_M.keys(), diccionario_L.keys()):
            patron_324 = r'^({})\s+([A-Z]+)\s+({})\s+(\d+)\s+({})\s+(\d+)'.format(re.escape(B), re.escape(M),
                                                                                  re.escape(L))
            componentes_324 = verificar_patron_escenario2(cadena, patron_324)
            if componentes_324 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_324[0]) + ' ' + \
                                                             componentes_324[1]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_324[2]) + ' ' + \
                                                              componentes_324[3]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_324[4]) + ' ' + \
                                                                 componentes_324[5]
                componentes_direccion_escenario2["InputPattern"] = 'B|+|M|^|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '0000'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO MANZANARES TORRE 2 APARTAMENTO 102'
                return componentes_direccion_escenario2

            patron_184 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+(\d+)$'.format(
                re.escape(B), re.escape(M), re.escape(L))
            componentes_184 = verificar_patron_escenario2(cadena, patron_184)
            if componentes_184 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_184[0]) + ' ' + \
                                                             componentes_184[1] + ' ' + componentes_184[2] + ' ' + \
                                                             componentes_184[3] + ' ' + componentes_184[4]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_184[5]) + ' ' + \
                                                              componentes_184[6] + ' ' + componentes_184[7]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_184[8]) + ' ' + \
                                                                 componentes_184[9]
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|+|+|M|+|+|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '001'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'BARRIO FRANCISCO DE PAULA SANTANDER EDIFICIO CAMILO TORRES LOCAL 2'
                return componentes_direccion_escenario2

            patron_185 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+(\d+)$'.format(
                re.escape(B), re.escape(M), re.escape(L))
            componentes_185 = verificar_patron_escenario2(cadena, patron_185)
            if componentes_185 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_185[0]) + ' ' + \
                                                             componentes_185[1] + ' ' + componentes_185[2] + ' ' + \
                                                             componentes_185[3]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_185[4]) + ' ' + \
                                                              componentes_185[5] + ' ' + componentes_185[6]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_185[7]) + ' ' + \
                                                                 componentes_185[8]
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|+|M|+|+|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '004'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'BARRIO FRANCISCO PAULA SANTANDER EDIFICIO CAMILO TORRES LOCAL 2'
                return componentes_direccion_escenario2

            patron_187 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+({})\s+(\d+)$'.format(
                re.escape(B), re.escape(M), re.escape(L))
            componentes_187 = verificar_patron_escenario2(cadena, patron_187)
            if componentes_187 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_187[0]) + ' ' + \
                                                             componentes_187[1] + ' ' + componentes_187[2] + ' ' + \
                                                             componentes_187[3]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_187[4]) + ' ' + \
                                                              componentes_187[5]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_187[6]) + ' ' + \
                                                                 componentes_187[7]
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|+|M|+|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '005'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'BARRIO FRANCISCO PAULA SANTANDER EDIFICIO CAMILO LOCAL 2'
                return componentes_direccion_escenario2

            patron_186 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+({})\s+(\d+)$'.format(
                re.escape(B), re.escape(M), re.escape(L))
            componentes_186 = verificar_patron_escenario2(cadena, patron_186)
            if componentes_186 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_186[0]) + ' ' + \
                                                             componentes_186[1] + ' ' + componentes_186[2] + ' ' + \
                                                             componentes_186[3] + ' ' + componentes_186[4]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_186[5]) + ' ' + \
                                                              componentes_186[6]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_186[7]) + ' ' + \
                                                                 componentes_186[8]
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|+|+|M|+|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '003'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'BARRIO FRANCISCO DE PAULA SANTANDER EDIFICIO CAMILO LOCAL 20'
                return componentes_direccion_escenario2

            patron_188 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+({})\s+(\d+)$'.format(re.escape(B),
                                                                                                 re.escape(M),
                                                                                                 re.escape(L))
            componentes_188 = verificar_patron_escenario2(cadena, patron_188)
            if componentes_188 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_188[0]) + ' ' + \
                                                             componentes_188[1] + ' ' + componentes_188[2]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_188[3]) + ' ' + \
                                                              componentes_188[4]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_188[5]) + ' ' + \
                                                                 componentes_188[6]
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|M|+|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '006'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'BARRIO FRANCISCO SANTANDER EDIFICIO TORRES LOCAL 20'
                return componentes_direccion_escenario2

            patron_402 = r'^({})\s+([A-Z]+)\s+({})\s+({})\s+([A-Z]+)\s+([A-Z]+)'.format(re.escape(B), re.escape(M),
                                                                                        re.escape(L))
            componentes_402 = verificar_patron_escenario2(cadena, patron_402)
            if componentes_402 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_402[0])}  {componentes_402[1]} ")
                componentes_direccion_escenario2["Manzana"] = re.sub(r'\s+', ' ',
                                                                     f"{diccionario_M.get(componentes_402[2])} ")
                componentes_direccion_escenario2["TipoPredio"] = re.sub(r'\s+', ' ',
                                                                        f"{diccionario_L.get(componentes_402[3])} {componentes_402[4]} {componentes_402[5]} ")
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|+|+|M|+|+|L|^'
                componentes_direccion_escenario2["LineaPatron"] = '4056'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO NORMANDIA EDIFICIO LOCAL FOTO ARIZA'
                return componentes_direccion_escenario2

        for L, M, L2 in product(diccionario_L.keys(), diccionario_M.keys(), diccionario_L.keys()):
            patron_31 = r'^({})\s+(\d+)\s+({})\s+(\d+)\s+({})\s+(.*)'.format(re.escape(L), re.escape(M), re.escape(L2))
            componentes_31 = verificar_patron_escenario2(cadena, patron_31)
            if componentes_31 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_31[0]) + ' ' + \
                                                                 componentes_31[1] + ' ' + diccionario_L.get(
                    componentes_31[4]) + ' ' + componentes_31[5]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_31[2]) + ' ' + \
                                                              componentes_31[3]
                componentes_direccion_escenario2["InputPattern"] = 'L|^|M|^|L|?'
                componentes_direccion_escenario2["LineaPatron"] = '798'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'APARTAMENTO 102 EDIFICIO 1 PORTERIA GIRASOLES NORTE'
                return componentes_direccion_escenario2

            patron_32 = r'^({})\s+(.*)\s+(\d+)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(L), re.escape(M),
                                                                                   re.escape(L2))
            componentes_32 = verificar_patron_escenario2(cadena, patron_32)
            if componentes_32 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_32[0]) + ' ' + \
                                                                 componentes_32[1] + ' ' + componentes_32[
                                                                     2] + ' ' + diccionario_L.get(
                    componentes_32[5]) + ' ' + componentes_32[6]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_32[3]) + ' ' + \
                                                              componentes_32[4]
                componentes_direccion_escenario2["InputPattern"] = 'L|?|^|M|*&|L|&'
                componentes_direccion_escenario2["LineaPatron"] = '821'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'APARTAMENTO EXTERIOR 102 EDIFICIO 161 PORTERIA VERDE'
                return componentes_direccion_escenario2

            patron_33 = r'^({})\s+(\d+)\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(L), re.escape(M),
                                                                                   re.escape(L2))
            componentes_33 = verificar_patron_escenario2(cadena, patron_33)
            if componentes_33 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_33[0]) + ' ' + \
                                                                 componentes_33[1] + ' ' + componentes_33[
                                                                     2] + ' ' + diccionario_L.get(
                    componentes_33[5]) + ' ' + componentes_33[6]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_33[3]) + ' ' + \
                                                              componentes_33[4]
                componentes_direccion_escenario2["InputPattern"] = 'L|^|?|M|*&|L|&'
                componentes_direccion_escenario2["LineaPatron"] = '848'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'APARTAMENTO 102 EXTERIOR EDIFICIO 161 PORTERIA VERDE'
                return componentes_direccion_escenario2

            patron_45 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(L), re.escape(M), re.escape(L2))
            componentes_45 = verificar_patron_escenario2(cadena, patron_45)
            if componentes_45 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_45[4]) + ' ' + \
                                                                 componentes_45[5] + ' ' + diccionario_L.get(
                    componentes_45[0]) + ' ' + componentes_45[1]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_45[2]) + ' ' + \
                                                              componentes_45[3]
                componentes_direccion_escenario2["InputPattern"] = 'L|*?|M|*&|L|&'
                componentes_direccion_escenario2["LineaPatron"] = '1101'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 EDIFICIO PRINCIPAL ESTACION 40'
                return componentes_direccion_escenario2

        for M, L, M2 in product(diccionario_M.keys(), diccionario_L.keys(), diccionario_M.keys()):
            patron_17 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(L), re.escape(M2))
            componentes_17 = verificar_patron_escenario2(cadena, patron_17)
            if componentes_17 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_17[0]) + ' ' + \
                                                              componentes_17[1]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_17[2]) + ' ' + \
                                                                 componentes_17[3] + ' ' + diccionario_M.get(
                    componentes_17[4]) + ' ' + componentes_17[5]
                componentes_direccion_escenario2["InputPattern"] = 'M|&|L|&|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '366'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'MANZANA RURAL APARTAMENTO LOS AGUACATES MANZANA AGUA LINDA'
                return componentes_direccion_escenario2

        for M, B, M2 in product(diccionario_M.keys(), diccionario_B.keys(), diccionario_M.keys()):
            patron_20 = r'^({})\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(B), re.escape(M2))
            componentes_20 = verificar_patron_escenario2(cadena, patron_20)
            if componentes_20 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(
                    componentes_20[0]) + ' ' + diccionario_B.get(componentes_20[1]) + ' ' + componentes_20[
                                                                  2] + ' ' + diccionario_M.get(
                    componentes_20[3]) + ' ' + componentes_20[4]
                componentes_direccion_escenario2["InputPattern"] = 'M|B|?|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '432'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'EDIFICIO BARRIO 10 MANZANA 20'
                return componentes_direccion_escenario2

    if diccionario_M is not None and diccionario_R is not None:
        for M, R, M2 in product(diccionario_M.keys(), diccionario_R.keys(), diccionario_M.keys()):
            patron_18 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(R), re.escape(M2))
            componentes_18 = verificar_patron_escenario2(cadena, patron_18)
            if componentes_18 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_18[0]) + ' ' + \
                                                              componentes_18[1]
                componentes_direccion_escenario2["TipoPredio"] = diccionario_R.get(componentes_18[2]) + ' ' + \
                                                                 componentes_18[3] + ' ' + diccionario_M.get(
                    componentes_18[4]) + ' ' + componentes_18[5]
                componentes_direccion_escenario2["InputPattern"] = 'M|&|R|&|M|?'
                componentes_direccion_escenario2["LineaPatron"] = '387'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CAMINO OSCURO CASA LOS CANSONES KILOMETRO 7'
                return componentes_direccion_escenario2

            patron_24 = r'^({})\s+(.*)\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(R),
                                                                                  re.escape(M2))
            componentes_24 = verificar_patron_escenario2(cadena, patron_24)
            if componentes_24 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_24[0]) + ' ' + \
                                                              componentes_24[1] + ' ' + componentes_24[
                                                                  2] + ' ' + diccionario_R.get(
                    componentes_24[3]) + ' ' + componentes_24[4] + ' ' + diccionario_M.get(componentes_24[5]) + ' ' + \
                                                              componentes_24[6]
                componentes_direccion_escenario2["InputPattern"] = '#M|&|&|R|&|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '648'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA REDOMA CASA ROSADA VEREDA CORMONARES'
                return componentes_direccion_escenario2

            patron_25 = r'^({})\s+(.*)\s+({})\s+(.*)\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(R),
                                                                                  re.escape(M2))
            componentes_25 = verificar_patron_escenario2(cadena, patron_25)
            if componentes_25 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_25[0]) + ' ' + \
                                                              componentes_25[1] + ' ' + diccionario_R.get(
                    componentes_25[2]) + ' ' + componentes_25[3] + ' ' + componentes_25[4] + ' ' + diccionario_M.get(
                    componentes_25[5]) + ' ' + componentes_25[6]
                componentes_direccion_escenario2["InputPattern"] = '#M|&|R|&|?|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '675'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'MANZANA REDOMA CASA TERMINAL NORTE VEREDA CORMONARES'
                return componentes_direccion_escenario2

            patron_26 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(R), re.escape(M2))
            componentes_26 = verificar_patron_escenario2(cadena, patron_26)
            if componentes_26 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_26[0]) + ' ' + \
                                                              componentes_26[1] + ' ' + diccionario_R.get(
                    componentes_26[2]) + ' ' + componentes_26[3] + ' ' + diccionario_M.get(componentes_26[4]) + ' ' + \
                                                              componentes_26[5]
                componentes_direccion_escenario2["InputPattern"] = '#M|&|R|&|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '675'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA REDOMA CASA TERMINAL VEREDA CORMONARES'
                return componentes_direccion_escenario2

    if diccionario_F is not None and diccionario_M is not None:
        for F, M, M2 in product(diccionario_F.keys(), diccionario_M.keys(), diccionario_M.keys()):
            patron_6 = r'^({})\s+(\d+)\s+({})\s+({})\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(F), re.escape(M),
                                                                                    re.escape(M2))
            componentes_6 = verificar_patron_escenario2(cadena, patron_6)
            if componentes_6 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_6[0]) + ' ' + \
                                                                 componentes_6[1]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(
                    componentes_6[2]) + ' ' + diccionario_M.get(componentes_6[3]) + ' ' + componentes_6[4] + ' ' + \
                                                              componentes_6[5]
                componentes_direccion_escenario2["InputPattern"] = 'F|^|M|M|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '1334'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 17 MANZANA EDIFICIO JARDIN PLAZA'
                return componentes_direccion_escenario2

    if diccionario_F is not None and diccionario_B is not None:
        for F, B, B2 in product(diccionario_F.keys(), diccionario_B.keys(), diccionario_B.keys()):
            patron_7 = r'^({})\s+(\d+)\s+({})\s+({})\s+([A-Z]+)$'.format(re.escape(F), re.escape(B), re.escape(B2))
            componentes_7 = verificar_patron_escenario2(cadena, patron_7)
            if componentes_7 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_7[0]) + ' ' + \
                                                                 componentes_7[1]
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(
                    componentes_7[2]) + ' ' + diccionario_B.get(componentes_7[3]) + ' ' + componentes_7[4]
                componentes_direccion_escenario2["InputPattern"] = 'F|^|B|B|+'
                componentes_direccion_escenario2["LineaPatron"] = '1334'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 19 BARRIO SUPERMANZANA A'
                return componentes_direccion_escenario2

    if diccionario_M is not None and diccionario_U is not None:
        for M, U, M2 in product(diccionario_M.keys(), diccionario_U.keys(), diccionario_M.keys()):
            patron_19 = r'^({})\s+(.*)\s+({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(U), re.escape(M2))
            componentes_19 = verificar_patron_escenario2(cadena, patron_19)
            if componentes_19 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_19[0]) + ' ' + \
                                                              componentes_19[1] + ' ' + diccionario_M.get(
                    componentes_19[4]) + ' ' + componentes_19[5]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_19[2]) + ' ' + \
                                                                   componentes_19[3]
                componentes_direccion_escenario2["InputPattern"] = 'M|&|U|&|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '410'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA 10 CONJUNTO LOS ARRAYANES TORRE 2'
                return componentes_direccion_escenario2

    ####### Empieza 2 Diccionarios #######

    if diccionario_U is not None and diccionario_M is not None:
        for U, M in product(diccionario_U.keys(), diccionario_M.keys()):
            patron_303 = r'^({})\s+({})\s+([A-Z]+)$'.format(re.escape(U), re.escape(M))
            componentes_303 = verificar_patron_escenario2(cadena, patron_303)
            if componentes_303 is not None:
                componentes_direccion_escenario2["Urbanizacion"] = re.sub(r'\s+', ' ',
                                                                          f"{diccionario_U.get(componentes_303[0])} {diccionario_M.get(componentes_303[1])} {componentes_303[2]}")
                componentes_direccion_escenario2["InputPattern"] = '*U|M="CAMINO"|?'
                componentes_direccion_escenario2["LineaPatron"] = '2312'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CONJUNTO CAMINO CERROS'
                return componentes_direccion_escenario2

        for M, U in product(diccionario_M.keys(), diccionario_U.keys()):
            patron_23 = r'^({})\s+(\d+)\s+({})\s+(.*)\s+(\d+)$'.format(re.escape(M), re.escape(U))
            componentes_23 = verificar_patron_escenario2(cadena, patron_23)
            if componentes_23 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_23[0]) + ' ' + \
                                                              componentes_23[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_23[2]) + ' ' + \
                                                                   componentes_23[3] + ' ' + componentes_23[4]
                componentes_direccion_escenario2["InputPattern"] = '#M|^|U|?|^'
                componentes_direccion_escenario2["LineaPatron"] = '592'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CAMINO 45 AEROPUERTO INTERNACIONAL EL DORADO 27'
                return componentes_direccion_escenario2

    if diccionario_U is not None and diccionario_R is not None:
        for U, R in product(diccionario_U.keys(), diccionario_R.keys()):
            patron_302 = r'^({})\s+({})\s+([A-Z]+)$'.format(re.escape(U), re.escape(R))
            componentes_302 = verificar_patron_escenario2(cadena, patron_302)
            if componentes_302 is not None:
                componentes_direccion_escenario2["NombreUrbanizacion"] = re.sub(r'\s+', ' ',
                                                                                f"{diccionario_U.get(componentes_302[0])} {diccionario_R.get(componentes_302[1])} {componentes_302[2]}")
                componentes_direccion_escenario2["InputPattern"] = '*U|R="CASA"|?'
                componentes_direccion_escenario2["LineaPatron"] = '2325'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CONJUNTO CASA AZUL'
                return componentes_direccion_escenario2

    if diccionario_B is not None and diccionario_U is not None:
        for B, U in product(diccionario_B.keys(), diccionario_U.keys()):
            patron_309 = r'^({})\s+({})$'.format(re.escape(B), re.escape(U))
            componentes_309 = verificar_patron_escenario2(cadena, patron_309)
            if componentes_309 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_309[0])}  {diccionario_U.get(componentes_309[1])}")
                componentes_direccion_escenario2["InputPattern"] = 'B|U'
                componentes_direccion_escenario2["LineaPatron"] = '2252 '
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO SECTOR'
                return componentes_direccion_escenario2

    if diccionario_B is not None and diccionario_L is not None:
        for B, L in product(diccionario_B.keys(), diccionario_L.keys()):
            patron_307 = r'^({})\s+(\d+)\s+({})$'.format(re.escape(B), re.escape(L))
            componentes_307 = verificar_patron_escenario2(cadena, patron_307)
            if componentes_307 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_307[0])}  {componentes_307[1]} {diccionario_L.get(componentes_307[2])}")
                componentes_direccion_escenario2["InputPattern"] = 'B|^|L'
                componentes_direccion_escenario2["LineaPatron"] = '2273'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO 53 APTO'
                return componentes_direccion_escenario2

        for L, B in product(diccionario_L.keys(), diccionario_B.keys()):
            patron_5 = r'^({})\s+({})$'.format(re.escape(L), re.escape(B))
            componentes_5 = verificar_patron_escenario2(cadena, patron_5)
            if componentes_5 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(
                    componentes_5[0]) + ' ' + diccionario_B.get(componentes_5[1])
                componentes_direccion_escenario2["InputPattern"] = 'L|B'
                componentes_direccion_escenario2["LineaPatron"] = '1241'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO CIUDADELA'
                return componentes_direccion_escenario2

    if diccionario_B is not None and diccionario_M is not None:
        for B, M in product(diccionario_B.keys(), diccionario_M.keys()):
            patron_189 = r'^({})\s+([A-Z]+)\s+({})\s+([A-Z]+)$'.format(re.escape(B), re.escape(M))
            componentes_189 = verificar_patron_escenario2(cadena, patron_189)
            if componentes_189 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_189[0]) + ' ' + \
                                                             componentes_189[1]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_189[2]) + ' ' + \
                                                              componentes_189[3]
                componentes_direccion_escenario2["InputPattern"] = 'B|+|M|+'
                componentes_direccion_escenario2["LineaPatron"] = '007'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO SANTANDER EDIFICIO TORRES'
                return componentes_direccion_escenario2

    if diccionario_L is not None and diccionario_U is not None:
        for L, U in product(diccionario_L.keys(), diccionario_U.keys()):
            patron_43 = r'^({})\s+(\d+)\s+({})\s+(.*)'.format(re.escape(L), re.escape(U))
            componentes_43 = verificar_patron_escenario2(cadena, patron_43)
            if componentes_43 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_43[0]) + ' ' + \
                                                                 componentes_43[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_43[2]) + ' ' + \
                                                                   componentes_43[3]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|U|?'
                componentes_direccion_escenario2["LineaPatron"] = '1069'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION COLORADA'
                return componentes_direccion_escenario2

            patron_44 = r'^({})\s+(\d+)\s+({})\s+([A-Z]+)(\d+)'.format(re.escape(L), re.escape(U))
            componentes_44 = verificar_patron_escenario2(cadena, patron_44)
            if componentes_44 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_44[0]) + ' ' + \
                                                                 componentes_44[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_44[2]) + ' ' + \
                                                                   componentes_44[3]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|U|<'
                componentes_direccion_escenario2["LineaPatron"] = '1085'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION A6'
                return componentes_direccion_escenario2

            patron_38 = r'^({})\s+(\d+)\s+({})\s+(\d+)\s+(.*)'.format(re.escape(L), re.escape(U))
            componentes_38 = verificar_patron_escenario2(cadena, patron_38)
            if componentes_38 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_38[0]) + ' ' + \
                                                                 componentes_38[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_38[2]) + ' ' + \
                                                                   componentes_38[3] + ' ' + componentes_38[4]
                componentes_direccion_escenario2["InputPattern"] = 'L|^|U|^|*?'
                componentes_direccion_escenario2["LineaPatron"] = '979'
                componentes_direccion_escenario2[
                    "DireccionEjemplo"] = 'APARTAMENTO 102 URBANIZACION 29 COLORINES MORADOS'
                return componentes_direccion_escenario2

    if diccionario_L is not None and diccionario_U is not None:
        for L, M in product(diccionario_L.keys(), diccionario_M.keys()):
            patron_181 = r'^({})\s+(\d+)\s+({})\s+(\d+)$'.format(re.escape(L), re.escape(M))
            componentes_181 = verificar_patron_escenario2(cadena, patron_181)
            if componentes_181 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_181[0]) + ' ' + \
                                                                 componentes_181[1]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_181[2]) + ' ' + \
                                                              componentes_181[3]
                componentes_direccion_escenario2["InputPattern"] = 'L|^|M|^'
                componentes_direccion_escenario2["LineaPatron"] = '0'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 TORR 1'
                return componentes_direccion_escenario2

    if diccionario_M is not None and diccionario_L is not None:
        for M, L in product(diccionario_M.keys(), diccionario_L.keys()):
            patron_70 = r'^({})\s+(\d+)\s+([A-Z]+)\s+(\d+)$'.format(re.escape(M), re.escape(L))
            componentes_70 = verificar_patron_escenario2(cadena, patron_70)
            if componentes_70 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_70[0]) + ' ' + \
                                                              componentes_70[1]
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_L.get(componentes_70[2]) + ' ' + \
                                                                   componentes_70[3]
                componentes_direccion_escenario2["InputPattern"] = 'M|^|L|^|'
                componentes_direccion_escenario2["LineaPatron"] = 'Sin Linea'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'TORRE 2 APARTAMENTO 102'
                return componentes_direccion_escenario2

        for M, M2 in product(diccionario_M.keys(), diccionario_M.keys()):
            patron_21 = r'^({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(M), re.escape(M2))
            componentes_21 = verificar_patron_escenario2(cadena, patron_21)
            if componentes_21 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_21[0]) + ' ' + \
                                                              componentes_21[1] + ' ' + diccionario_M.get(
                    componentes_21[2]) + ' ' + componentes_21[3]
                componentes_direccion_escenario2["InputPattern"] = '*M|&|M|&'
                componentes_direccion_escenario2["LineaPatron"] = '509'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'EDIFICIO LOS CEREZOS MANZANA 45 NORTE'
                return componentes_direccion_escenario2

    if diccionario_F is not None and diccionario_B is not None:
        for F, B in product(diccionario_F.keys(), diccionario_B.keys()):
            patron_10 = r'^({})\s+(\d+)\s+({})$'.format(re.escape(F), re.escape(B))
            componentes_10 = verificar_patron_escenario2(cadena, patron_10)
            if componentes_10 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_10[0]) + ' ' + \
                                                                 componentes_10[1] + ' ' + diccionario_B.get(
                    componentes_10[2])
                componentes_direccion_escenario2["InputPattern"] = 'F|^|B'
                componentes_direccion_escenario2["LineaPatron"] = '1439'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 201 CIUDADELA'
                return componentes_direccion_escenario2

            patron_8 = r'^({})\s+(\d+)\s+({})\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(F), re.escape(B))
            componentes_8 = verificar_patron_escenario2(cadena, patron_8)
            if componentes_8 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_8[0]) + ' ' + \
                                                                 componentes_8[1]
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_8[2]) + ' ' + componentes_8[
                    3] + ' ' + componentes_8[4]
                componentes_direccion_escenario2["InputPattern"] = 'F|^|B|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '1406'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'PLANTA 2 SUPERMANZANA PLAZA NORTE'
                return componentes_direccion_escenario2

            patron_9 = r'^({})\s+(\d+)\s+({})\s+([A-Z]+)$'.format(re.escape(F), re.escape(B))
            componentes_9 = verificar_patron_escenario2(cadena, patron_9)
            if componentes_9 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_9[0]) + ' ' + \
                                                                 componentes_9[1]
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_9[2]) + ' ' + componentes_9[
                    3]
                componentes_direccion_escenario2["InputPattern"] = 'F|^|B|+'
                componentes_direccion_escenario2["LineaPatron"] = '1424'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'TZ 10 BARRIO TOBERIN'
                return componentes_direccion_escenario2

    if diccionario_F is not None and diccionario_M is not None:
        for F, M in product(diccionario_F.keys(), diccionario_M.keys()):
            patron_56 = r'^({})\s+(\d+)\s+({})\s+(\d{{3,9}})\s+(\d{{3,9}})'.format(re.escape(F), re.escape(M))
            componentes_56 = verificar_patron_escenario2(cadena, patron_56)
            if componentes_56 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_56[0]) + ' ' + \
                                                                 componentes_56[1]
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_56[2]), componentes_56[
                                                                                                        3] + ' ' + \
                                                                                                    componentes_56[4]
                componentes_direccion_escenario2["InputPattern"] = 'F|^|M|+[{}LEN >=3]|+[{}LEN >=3]'
                componentes_direccion_escenario2["LineaPatron"] = '1355'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 102 EDIFICIO 104 403'
                return componentes_direccion_escenario2

    if diccionario_L is not None and diccionario_C is not None:
        for L, C in product(diccionario_L.keys(), diccionario_C.keys()):
            patron_30 = r'^({})\s+(\d+)\s+({})\s+(\d+)$'.format(re.escape(L), re.escape(C))
            componentes_30 = verificar_patron_escenario2(cadena, patron_30)
            if componentes_30 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_30[0]) + ' ' + \
                                                                 componentes_30[1]
                componentes_direccion_escenario2["TipoPiso"] = diccionario_C.get(componentes_30[2]) + ' ' + \
                                                               componentes_30[3]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|C|^'
                componentes_direccion_escenario2["LineaPatron"] = '781'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CONSULTORIO 101 PISO 1'
                return componentes_direccion_escenario2

        for L, L2 in product(diccionario_L.keys(), diccionario_L.keys()):
            patron_46 = r'^({})\s+(\d+)\s+({})\s+(\d+)$'.format(re.escape(L), re.escape(L2))
            componentes_46 = verificar_patron_escenario2(cadena, patron_46)
            if componentes_46 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_46[0]) + ' ' + \
                                                                 componentes_46[1] + ' ' + diccionario_L.get(
                    componentes_46[2]) + ' ' + componentes_46[3]
                componentes_direccion_escenario2["InputPattern"] = '*L|^|L|?'
                componentes_direccion_escenario2["LineaPatron"] = '1147'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 ESTACION 40'
                return componentes_direccion_escenario2

            patron_47 = r'^({})\s+(.*)\s+({})\s+(.*)'.format(re.escape(L), re.escape(L2))
            componentes_47 = verificar_patron_escenario2(cadena, patron_47)
            if componentes_47 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_47[0]) + ' ' + \
                                                                 componentes_47[1] + ' ' + diccionario_L.get(
                    componentes_47[2]) + ' ' + componentes_47[3]
                componentes_direccion_escenario2["InputPattern"] = '#L|&|L|&'
                componentes_direccion_escenario2["LineaPatron"] = '1164'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 ALTO ESTACION 40'
                return componentes_direccion_escenario2

    if diccionario_M is not None and diccionario_R is not None:
        for M, R in product(diccionario_M.keys(), diccionario_R.keys()):
            patron_182 = r'^({})\s+(\d+)\s+({})\s+(\d+)$'.format(re.escape(M), re.escape(R))
            componentes_182 = verificar_patron_escenario2(cadena, patron_182)
            if componentes_182 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_182[0]) + ' ' + \
                                                              componentes_182[1]
                componentes_direccion_escenario2["Casa"] = diccionario_R.get(componentes_182[2]) + ' ' + \
                                                           componentes_182[3]
                componentes_direccion_escenario2["InputPattern"] = 'M|^|R|^|'
                componentes_direccion_escenario2["LineaPatron"] = '000'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'INT 3 CASA 27'
                return componentes_direccion_escenario2

    ####### Empieza 1 Diccionario #######

    if diccionario_M is not None:
        for M in diccionario_M.keys():
            patron_1 = r'^({})\s+(\d{{1,3}})$'.format(re.escape(M))
            componentes_1 = verificar_patron_escenario2(cadena, patron_1)
            if componentes_1 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_1[0]) + ' ' + componentes_1[
                    1]
                componentes_direccion_escenario2["InputPattern"] = 'M|^'
                componentes_direccion_escenario2["LineaPatron"] = '5189'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA 27'
                return componentes_direccion_escenario2

            patron_3 = r'^({})\s+([A-Z]+)\s+(\d+)$'.format(re.escape(M))
            componentes_3 = verificar_patron_escenario2(cadena, patron_3)
            if componentes_3 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_3[0]) + ' ' + componentes_3[
                    1] + ' ' + componentes_3[2]
                componentes_direccion_escenario2["InputPattern"] = 'M|+|^'
                componentes_direccion_escenario2["LineaPatron"] = '498'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA GUTIERREZ 27'
                return componentes_direccion_escenario2

            patron_11 = r'^({})\s+(\d+)\s+([A-Z]+)\s+(\d+)$'.format(re.escape(M))
            componentes_11 = verificar_patron_escenario2(cadena, patron_11)
            if componentes_11 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_11[0]) + ' ' + \
                                                              componentes_11[1]
                componentes_direccion_escenario2["UnhandledData"] = componentes_11[2] + ' ' + componentes_11[3]
                componentes_direccion_escenario2["InputPattern"] = 'M|^|+|^|'
                componentes_direccion_escenario2["LineaPatron"] = '226'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MZ 27 ARBOL 2'
                return componentes_direccion_escenario2

            patron_27 = r'^({})\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(M))
            componentes_27 = verificar_patron_escenario2(cadena, patron_27)
            if componentes_27 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_27[0]) + ' ' + \
                                                              componentes_27[1] + ' ' + componentes_27[2]
                componentes_direccion_escenario2["InputPattern"] = '#M|&|?'
                componentes_direccion_escenario2["LineaPatron"] = '723'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA JARDIN ARMARIO'
                return componentes_direccion_escenario2

            patron_61 = r'^({})\s+(\d+)\s+(.*)'.format(re.escape(M))
            componentes_61 = verificar_patron_escenario2(cadena, patron_61)
            if componentes_61 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_61[0]) + ' ' + \
                                                              componentes_61[1] + ' ' + componentes_61[2]
                componentes_direccion_escenario2["InputPattern"] = '#M|^|**'
                componentes_direccion_escenario2["LineaPatron"] = '1519'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA 10 VERDE'
                return componentes_direccion_escenario2

            patron_63 = r'^({})\s+([A-Z]+)\s+(.*)'.format(re.escape(M))
            componentes_63 = verificar_patron_escenario2(cadena, patron_63)
            if componentes_63 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_63[0]) + ' ' + \
                                                              componentes_63[1] + ' ' + componentes_63[2]
                componentes_direccion_escenario2["InputPattern"] = '#M|+|**'
                componentes_direccion_escenario2["LineaPatron"] = '1537'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA AMARILLO VERDE'
                return componentes_direccion_escenario2

            patron_64 = r'^({})\s+(\d+[A-Z]+)\s+(.*)'.format(re.escape(M))
            componentes_64 = verificar_patron_escenario2(cadena, patron_64)
            if componentes_64 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_64[0]) + ' ' + \
                                                              componentes_64[1] + ' ' + componentes_64[2]
                componentes_direccion_escenario2["InputPattern"] = '#M|>|**'
                componentes_direccion_escenario2["LineaPatron"] = '1546'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA 2A VERDE'
                return componentes_direccion_escenario2

            patron_62 = r'^({})\s+(\d{{1}})\s+([A-Z]+)$'.format(re.escape(M))
            componentes_62 = verificar_patron_escenario2(cadena, patron_62)
            if componentes_62 is not None:
                componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_62[0]) + ' ' + \
                                                              componentes_62[1] + ' ' + componentes_62[2]
                componentes_direccion_escenario2["InputPattern"] = '#M|+[{}LEN =1]|**'
                componentes_direccion_escenario2["LineaPatron"] = '1528'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA 1 VERDE'
                return componentes_direccion_escenario2

    if diccionario_R is not None:
        for R in diccionario_R.keys():
            patron_28 = r'^({})\s+(.*)\s+(.*)'.format(re.escape(R))
            componentes_28 = verificar_patron_escenario2(cadena, patron_28)
            if componentes_28 is not None:
                componentes_direccion_escenario2["Casa"] = diccionario_R.get(componentes_28[0]) + ' ' + componentes_28[
                    1] + ' ' + componentes_28[2]
                componentes_direccion_escenario2["InputPattern"] = '#R|&|?'
                componentes_direccion_escenario2["LineaPatron"] = '736'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CASA ESQUINA PRIMAVERA'
                return componentes_direccion_escenario2

            patron_29 = r'^({})\s+(.*)'.format(re.escape(R))
            componentes_29 = verificar_patron_escenario2(cadena, patron_29)
            if componentes_29 is not None:
                componentes_direccion_escenario2["Casa"] = diccionario_R.get(componentes_29[0]) + ' ' + componentes_29[
                    1]
                componentes_direccion_escenario2["InputPattern"] = '#R|*&'
                componentes_direccion_escenario2["LineaPatron"] = '762'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CASA JARDINES'
                return componentes_direccion_escenario2

    if diccionario_U is not None:
        for U in diccionario_U.keys():
            patron_13 = r'^({})\s+(\d+)\s+([A-Z]+)$'.format(re.escape(U))
            componentes_13 = verificar_patron_escenario2(cadena, patron_13)
            if componentes_13 is not None:
                componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_13[0]) + ' ' + \
                                                                   componentes_13[1] + ' ' + componentes_13[2]
                componentes_direccion_escenario2["InputPattern"] = 'U|^|+'
                componentes_direccion_escenario2["LineaPatron"] = '1669'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'URBANIZACION 27 ARBOLEDAS'
                return componentes_direccion_escenario2

            patron_301 = r'^({})\s+([A-Z]+)$'.format(re.escape(U))
            componentes_301 = verificar_patron_escenario2(cadena, patron_301)
            if componentes_301 is not None:
                componentes_direccion_escenario2["NombreUrbanizacion"] = re.sub(r'\s+', ' ',
                                                                                f"{diccionario_U.get(componentes_301[0])} {componentes_301[1]}")
                componentes_direccion_escenario2["InputPattern"] = 'U|+'
                componentes_direccion_escenario2["LineaPatron"] = '2337'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CONJUNTO KIOSCO'
                return componentes_direccion_escenario2

            patron_325 = r'^({})\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(U))
            componentes_325 = verificar_patron_escenario2(cadena, patron_325)
            if componentes_325 is not None:
                componentes_direccion_escenario2["NombreUrbanizacion"] = re.sub(r'\s+', ' ',
                                                                                f"{diccionario_U.get(componentes_325[0])} {componentes_325[1]} {componentes_325[2]}")
                componentes_direccion_escenario2["InputPattern"] = 'U|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '2338'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CONJUNTO ENTRE RIOS'
                return componentes_direccion_escenario2

            patron_301 = r'^({})\s+([A-Z]+)$'.format(re.escape(U))
            componentes_301 = verificar_patron_escenario2(cadena, patron_301)
            if componentes_301 is not None:
                componentes_direccion_escenario2["NombreUrbanizacion"] = re.sub(r'\s+', ' ',
                                                                                f"{diccionario_U.get(componentes_301[0])} {componentes_301[1]}")
                componentes_direccion_escenario2["InputPattern"] = 'U|+'
                componentes_direccion_escenario2["LineaPatron"] = '2339'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CONJUNTO KIOSCO'
                return componentes_direccion_escenario2

            patron_325 = r'^({})\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(U))
            componentes_325 = verificar_patron_escenario2(cadena, patron_325)
            if componentes_325 is not None:
                componentes_direccion_escenario2["NombreUrbanizacion"] = re.sub(r'\s+', ' ',
                                                                                f"{diccionario_U.get(componentes_325[0])} {componentes_325[1]} {componentes_325[2]}")
                componentes_direccion_escenario2["InputPattern"] = 'U|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '2340'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CONJUNTO ENTRE RIOS'
                return componentes_direccion_escenario2

            patron_326 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(U))
            componentes_326 = verificar_patron_escenario2(cadena, patron_326)
            if componentes_326 is not None:
                componentes_direccion_escenario2["NombreUrbanizacion"] = re.sub(r'\s+', ' ',
                                                                                f"{diccionario_U.get(componentes_326[0])} {componentes_326[1]} {componentes_326[2]}")
                componentes_direccion_escenario2["InputPattern"] = 'U|+|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '2341'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CONJUNTO ENTRE RIOS GRANDES'
                return componentes_direccion_escenario2

    if diccionario_C is not None:
        for C in diccionario_C.keys():
            patron_53 = r'^({})\s+(\d{{1}})\s+(.*)'.format(re.escape(C))
            componentes_53 = verificar_patron_escenario2(cadena, patron_53)
            if componentes_53 is not None:
                componentes_direccion_escenario2["TipoPiso"] = diccionario_C.get(componentes_53[0]) + ' ' + \
                                                               componentes_53[1] + ' ' + componentes_53[2]
                componentes_direccion_escenario2["InputPattern"] = '#C|+[{}LEN =1]|**'
                componentes_direccion_escenario2["LineaPatron"] = '1299'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'PISO 6 ULTIMO'
                return componentes_direccion_escenario2

            patron_54 = r'^({})\s+([A-Z]+)\s+(.*)$'.format(re.escape(C))
            componentes_54 = verificar_patron_escenario2(cadena, patron_54)
            if componentes_54 is not None:
                componentes_direccion_escenario2["TipoPiso"] = diccionario_C.get(componentes_54[0]) + ' ' + \
                                                               componentes_54[1] + ' ' + componentes_54[2]
                componentes_direccion_escenario2["InputPattern"] = '#C|+|**'
                componentes_direccion_escenario2["LineaPatron"] = '1308'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'PISO UNO AEROPUERTO'
                return componentes_direccion_escenario2

            patron_55 = r'^({})\s+(\d+[A-Z]+)\s+(.*)'.format(re.escape(C))
            componentes_55 = verificar_patron_escenario2(cadena, patron_55)
            if componentes_55 is not None:
                componentes_direccion_escenario2["TipoPiso"] = diccionario_C.get(componentes_55[0]) + ' ' + \
                                                               componentes_55[1] + ' ' + componentes_55[2]
                componentes_direccion_escenario2["InputPattern"] = '#C|>|**'
                componentes_direccion_escenario2["LineaPatron"] = '1317'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'PISO 6A ALTO'
                return componentes_direccion_escenario2

            patron_52 = r'^({})\s+(\d+)\s+(.*)'.format(re.escape(C))
            componentes_52 = verificar_patron_escenario2(cadena, patron_52)
            if componentes_52 is not None:
                componentes_direccion_escenario2["TipoPiso"] = diccionario_C.get(componentes_52[0]) + ' ' + \
                                                               componentes_52[1] + ' ' + componentes_52[2]
                componentes_direccion_escenario2["InputPattern"] = '#C|^|**'
                componentes_direccion_escenario2["LineaPatron"] = '1290'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'PISO 60 ULTIMO'
                return componentes_direccion_escenario2

    if diccionario_L is not None:
        for L in diccionario_L.keys():
            patron_48 = r'^({})\s+([A-Z]+)\s+(\d+)'.format(re.escape(L))
            componentes_48 = verificar_patron_escenario2(cadena, patron_48)
            if componentes_48 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_48[0]) + ' ' + \
                                                                 componentes_48[1] + ' ' + componentes_48[2]
                componentes_direccion_escenario2["InputPattern"] = '#L|?|^'
                componentes_direccion_escenario2["LineaPatron"] = '1164'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO ALTO 102'
                return componentes_direccion_escenario2

            patron_49 = r'^({})\s+(\d+)\s+([A-Z]+)$'.format(re.escape(L))
            componentes_49 = verificar_patron_escenario2(cadena, patron_49)
            if componentes_49 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_49[0]) + ' ' + \
                                                                 componentes_49[1] + ' ' + componentes_49[2]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|?'
                componentes_direccion_escenario2["LineaPatron"] = '1210'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102 ALTO'
                return componentes_direccion_escenario2

            patron_51 = r'^({})\s+(\d+[A-Z]+)\s+(.*)'.format(re.escape(L))
            componentes_51 = verificar_patron_escenario2(cadena, patron_51)
            if componentes_51 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_51[0]) + ' ' + \
                                                                 componentes_51[1] + ' ' + componentes_51[2]
                componentes_direccion_escenario2["InputPattern"] = '#L|>|**'
                componentes_direccion_escenario2["LineaPatron"] = '1232'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 6A ALTO'
                return componentes_direccion_escenario2

            patron_50 = r'^({})\s+(\d+)$'.format(re.escape(L))
            componentes_50 = verificar_patron_escenario2(cadena, patron_50)
            if componentes_50 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_50[0]) + ' ' + \
                                                                 componentes_50[1]
                componentes_direccion_escenario2["InputPattern"] = '#L|^|**'
                componentes_direccion_escenario2["LineaPatron"] = '1223'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 102'
                return componentes_direccion_escenario2

    if diccionario_F is not None:
        for F in diccionario_F.keys():
            patron_58 = r'^({})\s+(\d{{1}})\s+(.*)'.format(re.escape(F))
            componentes_58 = verificar_patron_escenario2(cadena, patron_58)
            if componentes_58 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_58[0]) + ' ' + \
                                                                 componentes_58[1] + ' ' + componentes_58[2]
                componentes_direccion_escenario2["InputPattern"] = '#F|+[{}LEN =1]|**'
                componentes_direccion_escenario2["LineaPatron"] = '1472'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 1 AMARILLO'
                return componentes_direccion_escenario2

            patron_57 = r'^({})\s+(\d+)\s+(.*)'.format(re.escape(F))
            componentes_57 = verificar_patron_escenario2(cadena, patron_57)
            if componentes_57 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_57[0]) + ' ' + \
                                                                 componentes_57[1] + ' ' + componentes_57[2]
                componentes_direccion_escenario2["InputPattern"] = '#F|^|**'
                componentes_direccion_escenario2["LineaPatron"] = '1463'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 102 AMARILLO'
                return componentes_direccion_escenario2

            patron_59 = r'^({})\s+([A-Z]+)\s+(.*)'.format(re.escape(F))
            componentes_59 = verificar_patron_escenario2(cadena, patron_59)
            if componentes_59 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_59[0]) + ' ' + \
                                                                 componentes_59[1] + ' ' + componentes_59[2]
                componentes_direccion_escenario2["InputPattern"] = '#F|+|**'
                componentes_direccion_escenario2["LineaPatron"] = '1481'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA AMARILLO VERDE'
                return componentes_direccion_escenario2

            patron_60 = r'^({})\s+(\d+[A-Z]+)\s+(.*)'.format(re.escape(F))
            componentes_60 = verificar_patron_escenario2(cadena, patron_60)
            if componentes_60 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_60[0]) + ' ' + \
                                                                 componentes_60[1] + ' ' + componentes_60[2]
                componentes_direccion_escenario2["InputPattern"] = '#F|>|**'
                componentes_direccion_escenario2["LineaPatron"] = '1490'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 3B VERDE'
                return componentes_direccion_escenario2

            patron_180 = r'^({})\s+(\d+)$'.format(re.escape(F))
            componentes_180 = verificar_patron_escenario2(cadena, patron_180)
            if componentes_180 is not None:
                componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_180[0]) + ' ' + \
                                                                 componentes_180[1]
                componentes_direccion_escenario2["InputPattern"] = 'F|^'
                componentes_direccion_escenario2["LineaPatron"] = '0'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 202'
                return componentes_direccion_escenario2

    if diccionario_B is not None:
        for B in diccionario_B.keys():
            patron_304 = r'^({})\s+(\d+)([A-Z]+)$'.format(re.escape(B))
            componentes_304 = verificar_patron_escenario2(cadena, patron_304)
            if componentes_304 is not None:
                componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_304[0]) + " " + \
                                                             componentes_304[1] + " " + componentes_304[2]
                componentes_direccion_escenario2["InputPattern"] = 'B|*>'
                componentes_direccion_escenario2["LineaPatron"] = '2303'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO 56NORMANDIA'
                return componentes_direccion_escenario2

            patron_320 = r'^({})\s+(\d+)\s+([A-Z]+)$'.format(re.escape(B))
            componentes_320 = verificar_patron_escenario2(cadena, patron_320)
            if componentes_320 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_320[0])}  {componentes_320[1]} {componentes_320[2]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|*>'
                componentes_direccion_escenario2["LineaPatron"] = '2304'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO 2 NORMANDIA'
                return componentes_direccion_escenario2

            patron_321 = r'^({})\s+(\d+)\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(B))
            componentes_321 = verificar_patron_escenario2(cadena, patron_321)
            if componentes_321 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_321[0])}  {componentes_321[1]} {componentes_321[2]} {componentes_321[3]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|^|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '2305'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO 20 DE JULIO'
                return componentes_direccion_escenario2

            patron_322 = r'^({})\s+(\d+)([A-Z]+)\s+([A-Z]+)$'.format(re.escape(B))
            componentes_322 = verificar_patron_escenario2(cadena, patron_322)
            if componentes_322 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_322[0])}  {componentes_322[1]} {componentes_322[2]} {componentes_322[3]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|>|+'
                componentes_direccion_escenario2["LineaPatron"] = '2306'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO 20DE JULIO'
                return componentes_direccion_escenario2

            patron_305 = r'^({})\s+([A-Z]+)(\d+)$'.format(re.escape(B))
            componentes_305 = verificar_patron_escenario2(cadena, patron_305)
            if componentes_305 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_305[0])}  {componentes_305[1]} {componentes_305[2]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|<'
                componentes_direccion_escenario2["LineaPatron"] = '2294'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO NORMANDIA2'
                return componentes_direccion_escenario2

            patron_318 = r'^({})\s+([A-Z]+)\s+(\d+)$'.format(re.escape(B))
            componentes_318 = verificar_patron_escenario2(cadena, patron_318)
            if componentes_318 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_318[0])}  {componentes_318[1]} {componentes_318[2]}  ")
                componentes_direccion_escenario2["InputPattern"] = 'B|+|^'
                componentes_direccion_escenario2["LineaPatron"] = '2154'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO NORMANDIA 2'
                return componentes_direccion_escenario2

            patron_319 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+(\d+)$'.format(re.escape(B))
            componentes_319 = verificar_patron_escenario2(cadena, patron_319)
            if componentes_319 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_319[0])}  {componentes_319[1]} {componentes_319[2]} {componentes_319[3]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|^'
                componentes_direccion_escenario2["LineaPatron"] = '2154'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO VILLA LUZ 2'
                return componentes_direccion_escenario2

            patron_306 = r'^({})\s+(\d+)$'.format(re.escape(B))
            componentes_306 = verificar_patron_escenario2(cadena, patron_306)
            if componentes_306 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_306[0])}  {componentes_306[1]} ")
                componentes_direccion_escenario2["InputPattern"] = 'B|^'
                componentes_direccion_escenario2["LineaPatron"] = '2285'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO 53'
                return componentes_direccion_escenario2

            patron_308 = r'^({})\s+(\d+)\s+(\d+)$'.format(re.escape(B))
            componentes_308 = verificar_patron_escenario2(cadena, patron_308)
            if componentes_308 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_308[0])}  {componentes_308[1]} {componentes_308[2]} ")
                componentes_direccion_escenario2["InputPattern"] = 'B|^|^'
                componentes_direccion_escenario2["LineaPatron"] = '2261'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'CIUDADELA 53 78'
                return componentes_direccion_escenario2

            patron_310 = r'^({})\s+([A-Z]+)$'.format(re.escape(B))
            componentes_310 = verificar_patron_escenario2(cadena, patron_310)
            if componentes_310 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_310[0])}  {componentes_310[1]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|+'
                componentes_direccion_escenario2["LineaPatron"] = '2252 '
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO NORMANDIA'
                return componentes_direccion_escenario2

            patron_313 = r'^({})\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(B))
            componentes_313 = verificar_patron_escenario2(cadena, patron_313)
            if componentes_313 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_313[0])}  {componentes_313[1]} {componentes_313[2]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '2213'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO EL GAITAN'
                return componentes_direccion_escenario2

            patron_315 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(B))
            componentes_315 = verificar_patron_escenario2(cadena, patron_315)
            if componentes_315 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_315[0])}  {componentes_315[1]} {componentes_315[2]} {componentes_315[3]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '2187'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO CLAROS DEL BOSQUE'
                return componentes_direccion_escenario2

            patron_316 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(B))
            componentes_316 = verificar_patron_escenario2(cadena, patron_316)
            if componentes_316 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_316[0])}  {componentes_316[1]} {componentes_316[2]} {componentes_316[3]} {componentes_316[4]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|+|+'
                componentes_direccion_escenario2["LineaPatron"] = '2177'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO VEINTE DE JULIO BGOTA'
                return componentes_direccion_escenario2

            patron_317 = r'^({})\s+([A-Z]+)\s+([A-Z]+)\s+([A-Z]+)\s+(\d+)$'.format(re.escape(B))
            componentes_317 = verificar_patron_escenario2(cadena, patron_317)
            if componentes_317 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_317[0])}  {componentes_317[1]} {componentes_317[2]} {componentes_317[3]} {componentes_317[4]} ")
                componentes_direccion_escenario2["InputPattern"] = 'B|+|+|+|^'
                componentes_direccion_escenario2["LineaPatron"] = '2167'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO VEINTE DE JULIO 1'
                return componentes_direccion_escenario2

            patron_311 = r'^(\d+)\s+({})\s+([A-Z]+)(\d+)$'.format(re.escape(B))
            componentes_311 = verificar_patron_escenario2(cadena, patron_311)
            if componentes_311 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{componentes_311[0]} {diccionario_B.get(componentes_311[1])} {componentes_311[2]}")
                componentes_direccion_escenario2["InputPattern"] = '^|B|<'
                componentes_direccion_escenario2["LineaPatron"] = '2234 '
                componentes_direccion_escenario2["DireccionEjemplo"] = '53 BARRIO NORMANDIA2'
                return componentes_direccion_escenario2

            patron_312 = r'^({})\s+([A-Z]+)(\d+)\s+(\d+)$'.format(re.escape(B))
            componentes_312 = verificar_patron_escenario2(cadena, patron_312)
            if componentes_312 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_312[0])}  {componentes_312[1]} {componentes_312[2]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|<|^'
                componentes_direccion_escenario2["LineaPatron"] = '2222 '
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO NORMANDIA2 3'
                return componentes_direccion_escenario2

            patron_314 = r'^({})\s+([A-Z]+)\s+(\d+)$'.format(re.escape(B))
            componentes_314 = verificar_patron_escenario2(cadena, patron_314)
            if componentes_314 is not None:
                componentes_direccion_escenario2["Barrio"] = re.sub(r'\s+', ' ',
                                                                    f"{diccionario_B.get(componentes_314[0])}  {componentes_314[1]} {componentes_314[2]}")
                componentes_direccion_escenario2["InputPattern"] = 'B|?|^'
                componentes_direccion_escenario2["LineaPatron"] = '2200'
                componentes_direccion_escenario2["DireccionEjemplo"] = 'BARRIO ENTRE RIOS 2'
                return componentes_direccion_escenario2

    componentes_direccion_escenario2["UnhandledData"] = cadena

    return componentes_direccion_escenario2
