import pandas as pd

import preprocesamiento
import filtros

import poblacion

cuentas_por_cobrar = []
cuentas_por_pagar = []
ingresos = []
egresos = []

facturas = pd.read_csv('reportCXCAgosto_done.csv')
cuentas_por_cobrar += preprocesamiento.clean_cuentas(facturas)
facturas = pd.read_csv('reportCXCSeptiembre_done.csv')
cuentas_por_cobrar += preprocesamiento.clean_cuentas(facturas)
facturas = pd.read_csv('reportCXCOctubre_done.csv')
cuentas_por_cobrar += preprocesamiento.clean_cuentas(facturas)

facturas = pd.read_csv('reportCXPAgosto_done.csv')
cuentas_por_pagar += preprocesamiento.clean_cuentas(facturas)
facturas = pd.read_csv('reportCXPSeptiembre_done.csv')
cuentas_por_pagar += preprocesamiento.clean_cuentas(facturas)
facturas = pd.read_csv('reportCXPOctubre_done.csv')
cuentas_por_pagar += preprocesamiento.clean_cuentas(facturas)

movimientos = pd.read_csv('movsAgoSep_done.csv')
ig, eg = preprocesamiento.clean_movimientos(movimientos)
ingresos += ig
egresos += eg
movimientos = pd.read_csv('movsOct_done.csv')
ig, eg = preprocesamiento.clean_movimientos(movimientos)
ingresos += ig
egresos += eg

cuentas_por_cobrar[0].showFactura()
print(len(ingresos))
movimientos_filtrados = filtros.filtrar_movimientos_factura_por_cobrar(cuentas_por_cobrar[0], ingresos)
print(len(movimientos_filtrados))

poblacion_soluciones = poblacion.Poblacion(100, cuentas_por_cobrar[0], movimientos_filtrados)
poblacion_soluciones.inicializar_poblacion()
poblacion_soluciones.mejor_solution()