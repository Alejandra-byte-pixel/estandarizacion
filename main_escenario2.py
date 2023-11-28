import streamlit as st

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
col2.markdown("<h1 class='titulo'>Estandarización de direcciones nacionales</h1>", unsafe_allow_html=True)


