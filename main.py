from multiprocessing.sharedctypes import Value
import streamlit as st
import os
from front import main as Telefonos
from Escenario_2_Optimizado import main as Direcciones

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
        background-color: rgb(255, 250, 250); /* Color de fondo original */
        color: #FFFFFF; /* Color de letras original (blanco) */
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

#seleccion de Programa
# Configuración de la página
st.set_page_config(layout="wide")

# Diccionario de opciones
dashboards = {
    "Telefonos": front,
    "Direcciones": Escenario_2_Optimizado,
}

# Barra lateral para seleccionar el dashboard
choice_from_url = query_params = st.experimental_get_query_params().get("example", ["Telefonos"])[0]
index = list(dashboards.keys()).index(choice_from_url)

choice = st.sidebar.radio("Seleccionar Programa", list(dashboards.keys()), index=index)

# Obtener la función del dashboard seleccionado
dashboard_func = dashboards[choice]

# Ejecutar la función del dashboard seleccionado
dashboard_func()

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())

    with st.expander('Code for this example:'):
        st.markdown(f"""``` python
{c}```""")
