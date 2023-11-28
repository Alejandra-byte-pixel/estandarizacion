import streamlit as st
import estandarizador
import csv
import pandas as pd

# Establecer el color de fondo para la parte derecha
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

# Contenedor principal
#separador_campos = ';'

# Crear dos columnas para las imágenes
#col1, col2 = st.columns(2)

# Imagen 1
#image1 = col1.image("LogoSETI.jpeg", caption='SETI', width=100)
# Espacio entre las imágenes
#col1.write("")

# Imagen 2
#image2 = col2.image("LogoAIO.jpeg", caption='AIO', width=100)

#Una sola imagen 
#st.image("LogoSetiAio.jpg", caption='Logo', width=50)

#Titulo Solo 
#st.markdown("<h1 style='color: red;'>Aplicación Estandarización de teléfonos nacionales</h1>", unsafe_allow_html=True)

# Contenedor principal
#col1, col2 = st.columns([1, 3])  # Definir el ancho de las columnas (en este caso, 1 y 3)

# Estilo para la imagen y el título
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
col1.image("LogoSetiAio.jpg", caption='Logo', width=100, use_column_width=True)

# Título
col2.markdown("<h1 class='titulo'>Estandarización de teléfonos nacionales</h1>", unsafe_allow_html=True)

# Barra lateral (sidebar)
#st.sidebar.markdown("<div style='background-color: #FFFFFF; color: with; padding: 20px;'>", unsafe_allow_html=True)
# Barra lateral (sidebar)
# Cargar la imagen en el sidebar y alinearla a la derecha
st.sidebar.image("telefono.jpg",caption='Telefonos', width=80, use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
nombre_archivo = st.sidebar.file_uploader(" 🧩 ", type=["txt"], key="file-upload", help='Limite 200MB')
#st.sidebar.markdown("<h1 style='text-align: center; color: black;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
#nombre_archivo = st.sidebar.file_uploader(" 🧩 Cargue archivo TXT",type=["txt"], key="file-upload", help='Limite 200MB')
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

Dataframe1 = {"cadenas": [],
    "tipo":[],
    "indicativos pais": [],
    "indicativos area": [],
    "telefonos": [],
    "estandarizacion final": []
}


if nombre_archivo is not None:
    contenido = nombre_archivo.read().decode("utf-8")  # Leer el contenido del archivo
    name = nombre_archivo.name.split('.')[0]

    datos = "CADENA;TIPO;INDICATIVO PAIS;INDICATIVO AREA;TELEFONO;ESTANDARIZACION FINAL" + '\r\n'
    lector_csv = csv.reader(contenido.splitlines())
    
    for fila in lector_csv:
        linea = fila[0]  # Obtener el primer elemento de la fila como la línea a procesar
        resultado = estandarizador.estandarizar(linea)  # Obtener el resultado como una lista
        Dataframe1["cadenas"].append(linea)
        Dataframe1["tipo"].append(resultado[0])
        Dataframe1["indicativos pais"].append(resultado[1])
        Dataframe1["indicativos area"].append(resultado[2])
        Dataframe1["telefonos"].append(resultado[3])
        Dataframe1["estandarizacion final"].append(resultado[4])

        
        resultado_str = linea + ";" + ";".join(str(item) for item in resultado)  # Convertir cada elemento en una cadena de texto
        datos += resultado_str + '\r\n'

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(Dataframe1)

    # Mostrar el resultado en una tabla
    st.write("Resultado:")
    st.dataframe(df)

    #Crear botón para descargar archivo csv
    st.download_button('🖨️ Descarga del .CSV', datos,file_name=name + '.csv')

else:
    st.markdown("<p style='color: black;'>Por favor, selecciona un archivo para cargar.</p>", unsafe_allow_html=True)
