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

