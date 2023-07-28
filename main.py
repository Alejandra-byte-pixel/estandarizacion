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
        padding: 20px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Establecer el estilo para el bloque de cita
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
        background-color: rgb(183, 179, 179 ); /* Color de fondo original */
        color: #FFFFFF; /* Color de letras original (blanco) */
    }
    [aria-selected="true"] {
        color: black; /* Letras negras */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenedor principal
separador_campos = ';'

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

# Imágenes y el título
col1, col2 = st.columns([2, 4])

# Imagen
col1.image("LogoSetiAio.jpg", caption='Logo', width=50)

# Título
col2.markdown("<h1 style='color: red;'>Aplicación Estandarización de teléfonos nacionales</h1>", unsafe_allow_html=True)


st.sidebar.markdown(
    """
    <style>
    .main {
        background-color: #FFFFFF;
        padding: 20px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Barra lateral (sidebar)
#st.sidebar.markdown("<div style='background-color: #FFFFFF; color: with; padding: 20px;'>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: center; color: grey;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
nombre_archivo = st.sidebar.file_uploader("Cargue archivo TXT", type=["txt"], key="file-upload", help='Limite 200MB')
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

Dataframe1 = {"cadenas": [],
    "tipo":[],
    "indicativos_pais": [],
    "indicativos_area": [],
    "telefonos": [],
    "estandarizacion_final": []
}


if nombre_archivo is not None:
    contenido = nombre_archivo.read().decode("utf-8")  # Leer el contenido del archivo
    name = nombre_archivo.name.split('.')[0]

    datos = "CADENA;TIPO;INDICATIVO_PAIS;INDICATIVO_AREA;TELEFONO;ESTANDARIZACION_FINAL" + '\r\n'
    lector_csv = csv.reader(contenido.splitlines())
    
    for fila in lector_csv:
        linea = fila[0]  # Obtener el primer elemento de la fila como la línea a procesar
        resultado = estandarizador.estandarizar(linea)  # Obtener el resultado como una lista
        Dataframe1["cadenas"].append(linea)
        Dataframe1["tipo"].append(resultado[0])
        Dataframe1["indicativos_pais"].append(resultado[1])
        Dataframe1["indicativos_area"].append(resultado[2])
        Dataframe1["telefonos"].append(resultado[3])
        Dataframe1["estandarizacion_final"].append(resultado[4])

        
        resultado_str = linea + ";" + ";".join(str(item) for item in resultado)  # Convertir cada elemento en una cadena de texto
        datos += resultado_str + '\r\n'

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(Dataframe1)

    # Mostrar el resultado en una tabla
    st.write("Resultado:")
    st.dataframe(df)

    #Crear botón para descargar archivo csv
    st.download_button('Download CSV', datos,file_name=name + '.csv')

else:
    st.markdown("<p style='color: black;'>Por favor, selecciona un archivo para cargar.</p>", unsafe_allow_html=True)
    
