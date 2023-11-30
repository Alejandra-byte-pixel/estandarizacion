import streamlit as st
import estandarizador_escenario2
from multiprocessing import Pool

# fondo para la parte derecha
st.markdown(
    """
    <style>
    .main {
        background-color: #FFFFFF;
        padding: 0;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Establecer Fondo para la barra izq
st.markdown(
    """
    <style>
    blockquote {
        background-color: #FFFFFF; /* Fondo blanco */
        color: black; /* Letras negras */
    }
    blockquote p {
        font-size: 30px;
        color: black; /* Letras negras */
    }
    [data-testid="stSidebar"] {
        background-color: rgb(0, 0, 0); /* Color de fondo original */
        color: #000000; /* Color de letras original (blanco) */
    }
    [aria-selected="true"] {
        color: black; /* Letras negras */
    }
    </style>
    """,
    unsafe_allow_html=True
)


estilo_imagen = """
    <style>
    .imagen {
        display: inline-block;
        vertical-align: middle;
    }
    .titulo {
        color: red;
        display: inline-block;
        vertical-align: middle;
        margin-left: 10px;
        margin-top: 0;
    }
    </style>
    """
st.markdown(estilo_imagen, unsafe_allow_html=True)

# Contenedor principal
col1, col2 = st.columns([1, 3])  # Definir el ancho de las columnas (en este caso, 1 y 3)

# Imagen
col1.image("LogoSetiAio.jpg", caption='AIO', width=100, use_column_width=True)

# Título
col2.markdown("<h1 class='titulo'>Estandarización de direcciones nacionales</h1>", unsafe_allow_html=True)


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

    with Pool(processes=8) as pool:
        resultados = pool.map(procesar_direccion, lista_direcciones)

    with open(archivo_salida, 'w') as f:
        for direccion, diccionario in resultados:
            f.write(f"{direccion}\n{diccionario}\n-------------------------------------------\n")


st.sidebar.image("casa.jpg",caption='Direcciones', width=80, use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
nombre_archivo = st.sidebar.file_uploader(" 🧩 ", type=["txt"], key="file-upload", help='Limite 200MB')
#st.sidebar.markdown("<h1 style='text-align: center; color: black;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
#nombre_archivo = st.sidebar.file_uploader(" 🧩 Cargue archivo TXT",type=["txt"], key="file-upload", help='Limite 200MB')
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)



