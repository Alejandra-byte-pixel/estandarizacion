# Opción 1: Utilizando el módulo csv
import csv

nombre_archivo = "telefonos.csv"  

with open(nombre_archivo, "r") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        columna = fila[0]
        print(columna)

# Opción 2: Abriendo y leyendo el archivo directamente
nombre_archivo = "telefonos.csv" 
with open(nombre_archivo, "r") as archivo:
    for linea in archivo:
        columna = linea.strip()
        print(columna)
