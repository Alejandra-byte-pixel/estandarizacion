import streamlit as st
import estandarizador_direcciones
from multiprocessing import Pool
import csv  

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
        background-color: #FFFFFF; /* Fondo */
        color: white; /* Letras */
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



st.sidebar.image("casa.jpg",caption='Direcciones', width=80, use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
nombre_archivo = st.sidebar.file_uploader(" 🧩 ", type=["txt"], key="file-upload", help='Limite 200MB')
#st.sidebar.markdown("<h1 style='text-align: center; color: black;'>Aquí cargue el archivo</h1>", unsafe_allow_html=True)
#nombre_archivo = st.sidebar.file_uploader(" 🧩 Cargue archivo TXT",type=["txt"], key="file-upload", help='Limite 200MB')
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

Dataframe1 = {"ADDRESS": [],
              "ADDR_LINE_ONE": [],
              "ADDR_LINE_TWO": [],
              "ADDR_LINE_THREE": []
}

if nombre_archivo is not None:
    contenido = nombre_archivo.read().decode("utf-8")  # Leer el contenido del archivo
    name = nombre_archivo.name.split('.')[0]

    datos = "ADDRESS;ADDR_LINE_ONE;ADDR_LINE_TWO;ADDR_LINE_THREE" + '\r\n'
    lector_csv = csv.reader(contenido.splitlines())
    
    for fila in lector_csv:
        linea = fila[0]  # Obtener el primer elemento de la fila como la línea a procesar
        resultado = estandarizador_direcciones.estandarizar(linea)  # Obtener el resultado como una lista
        Dataframe1["ADDRESS"].append(linea)
        Dataframe1["ADDR_LINE_ONE"].append(resultado[0])
        Dataframe1["ADDR_LINE_TWO"].append(resultado[1])
        Dataframe1["ADDR_LINE_THREE"].append(resultado[2])
        resultado_str = linea + ";" + ";".join(str(item) for item in resultado)  # Convertir cada elemento en una cadena de texto
        datos += resultado_str + '\r\n'

    print(dir(estandarizador_direcciones))

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(Dataframe1)

    # Mostrar el resultado en una tabla
    st.write("Resultado:")
    st.dataframe(df)

    # Crear botón para descargar archivo csv
    st.download_button('🖨️ Descarga del .CSV', datos, file_name=name + '.csv')

else:
    st.markdown("<p style='color: black;'>Por favor, selecciona un archivo para cargar.</p>", unsafe_allow_html=True)
