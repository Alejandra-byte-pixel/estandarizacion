from multiprocessing.sharedctypes import Value
import streamlit as st
import os

st.set_page_config(layout="wide")
root = os.path.join(os.path.dirname(__file__))

dashboards = {
    "Telefonos": os.path.join(root, "front.py"),
    "Direcciones": os.path.join(root, "main_escenario2.py")
}

choice_from_url = st.experimental_get_query_params().get("example", ["Telefonos"])[0]
index = list(dashboards.keys()).index(choice_from_url) if choice_from_url in dashboards else 0

choice = st.sidebar.radio("Seleccionar Programa", list(dashboards.keys()), index=index)

path = dashboards[choice]

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())
    with st.expander('Code for this example:'):
        st.markdown(f"""``` python
{c}```""")

