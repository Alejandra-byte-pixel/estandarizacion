from multiprocessing.sharedctypes import Value
import streamlit as st
import os

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


st.set_page_config(layout="wide")
root = os.path.join(os.path.dirname(__file__))

dashboards = {
    "Telefonos": os.path.join(root, "front.py"),
    "Direcciones": os.path.join(root, "Escenario_2_Optimizado.py"),
}

choice_from_url = query_params = st.experimental_get_query_params().get("example", ["Main Example"])[0]
index = list(dashboards.keys()).index(choice_from_url)

choice = st.sidebar.radio("Examples", list(dashboards.keys()), index=index)

path = dashboards[choice]

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())

    with st.expander('Code for this example:'):
        st.markdown(f"""``` python
{c}```""")
