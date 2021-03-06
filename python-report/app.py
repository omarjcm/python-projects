import openpyxl
from funciones import *

# Creación del archivo en excel
nombre_archivo = 'data/reporte_see.xlsx'

wb = load_workbook( nombre_archivo )
#sheet = wb['Sheet']
sheet = wb['Reporte 1']
#sheet.title = 'Reporte 1'
agregar_imagen( sheet )

ws = wb.active
ws.oddHeader.left.color = "CC3366"
cabecera = ['Country', 'Year', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

agregar_titulo( ws )
agregar_filtro( ws, sheet, cabecera )

# Lectura de los datos
agregar_datos( ws, sheet, cabecera )

# Guardar el archivo
wb.save( nombre_archivo )