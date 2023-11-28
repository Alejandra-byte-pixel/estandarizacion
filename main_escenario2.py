import streamlit as st
import estandarizador_escenario2
from multiprocessing import Pool
import time
inicio = time.time()

# Establecer el color de fondo para la parte derecha
st.markdown(
    """
    <style>
    .main {
        background-color: #FFFFFF;
        padding: 0;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def get_diccionario(diccionario: dict):
    dictionary_depurado: dict = {}
    if diccionario is not None:
        for i in diccionario.keys():
            if diccionario[i] != "":
                dictionary_depurado[i] = diccionario[i]
        return dictionary_depurado
    else:
        return dictionary_depurado

def procesar_direccion(direccion):
    componentes = estandarizador_escenario2.estandarizar_direccion(direccion)
    return direccion, get_diccionario(componentes)

def procesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        lista_direcciones = f.read().splitlines()

    with Pool(processes=6) as pool:
        resultados = pool.map(procesar_direccion, lista_direcciones)

    with open(archivo_salida, 'w') as f:
        for direccion, diccionario in resultados:
            f.write(f"{direccion}\n{diccionario}\n-------------------------------------------\n")

if __name__ == '__main__':
    ruta_archivo_entrada = 'C:/Users/aleja/PycharmProjects/Escenario_2_Optimizado/Direcciones_escenario_2.txt'
    ruta_archivo_salida = 'C:/Users/aleja/PycharmProjects/Escenario_2_Optimizado/Direcciones_estabdarizadas_escenario_2.txt'

    procesar_archivo(ruta_archivo_entrada, ruta_archivo_salida)

fin = time.time()
print(fin-inicio)
