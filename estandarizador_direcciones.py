import streamlit as st
import csv
import pandas as pd
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


def procesar_direccion(cadena):
    palabras = cadena.split()
    campo1 = " ".join(palabras)
    campo2 = " ".join(palabras[:-2])
    campo3 = palabras[-2]
    campo4 = "si"
    return [campo1, campo2, campo3, campo4]

st.sidebar.image("casa.jpg",caption='Direcciones', width=80, use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
nombre_archivo = st.sidebar.file_uploader(" 🧩 ", type=["txt"], key="file-upload", help='Limite 200MB')
#st.sidebar.markdown("<h1 style='text-align: center; color: black;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
#nombre_archivo = st.sidebar.file_uploader(" 🧩 Cargue archivo TXT",type=["txt"], key="file-upload", help='Limite 200MB')
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

def procesar_archivo(archivo_entrada):
    with open(nombre_archivo, 'r') as f:
        lineas = f.readlines()

    resultados = [procesar_direccion(linea.strip()) for linea in lineas]

    return resultados

if __name__ == '__main__':
    st.title("Procesador de Direcciones")

      if archivo_entrada is not None:
        # Procesar el archivo y obtener los resultados
        resultados = procesar_archivo(archivo_entrada)
        
        # Crear un CSV en memoria
        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(["Campo1", "Campo2", "Campo3", "Campo4"])
        csv_writer.writerows(resultados)

        # Botón de descarga
        st.download_button(
            label="Descargar CSV",
            data=csv_data.getvalue(),
            file_name="resultados.csv",
            key="csv_button"
        )

