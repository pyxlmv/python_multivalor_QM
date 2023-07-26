"""
Version: 1.0.0
Date: 6/4/2023

* VICSO-Asesores Empresariales, C.A.
* Copyright (C) VICSO-Asesores Empresariales, C.A.  1990-2023
"""
glversion = "1.0.0"

###########
# Imports #
###########
import sys
import importlib
from importlib import util

# Try to import tkinter
try:
    import tkinter as tk
except:
    print()
    print("Error:No se puede continuar con este ejemplo")
    print("El paquete 'tkinter' no fue encontrado")
    print("Consulte la Guía del usuario de d3 Python para obtener más detalles")
    print()
    quit()

# Se crea la ventana del programa
root = tk.Tk()
root.title('Sistema Administrativo - VICSO')
root.resizable(0, 0)

#  Actualizamos todo el contenido de la ventana (la ventana pude crecer si se le agrega
#  mas widgets).Esto actualiza el ancho y alto de la ventana en caso de crecer.

##################################
# Inicio de Centrado de Pantalla #
##################################
##############################################
# Obtenemos el largo y  ancho de la pantalla #
##############################################
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()

############################################
#  Guardamos el largo y alto de la ventana #
############################################
wventana = 470
hventana = 250

###########################################################################
# Aplicamos la siguiente formula para calcular donde debería posicionarse #
###########################################################################
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

################################################
# Se lo aplicamos a la geometría de la ventana #
################################################
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
#################################
# Final de Centrado de Pantalla #
#################################

#set window color
root.configure(bg='#54E9E9')

# Se crea el menú de la ventana
menu = tk.Menu()

# Se crean las opciones principales
menu_archivos = tk.Menu(menu, tearoff=0)
menu_mga = tk.Menu(menu, tearoff=0)
menu_inf = tk.Menu(menu, tearoff=0)
menu_cxc = tk.Menu(menu, tearoff=0)
menu_cxp = tk.Menu(menu, tearoff=0)
menu_inv = tk.Menu(menu, tearoff=0)
menu_fac = tk.Menu(menu, tearoff=0)
menu_nom = tk.Menu(menu, tearoff=0)
menu_afi = tk.Menu(menu, tearoff=0)
menu_est = tk.Menu(menu, tearoff=0)
menu_ayuda = tk.Menu(menu, tearoff=0)

# Agregar las opciones principales al menú
menu.add_cascade(label="CON", menu=menu_archivos)
menu.add_cascade(label="MGA", menu=menu_mga)
menu.add_cascade(label="INF", menu=menu_inf)
menu.add_cascade(label="CXC", menu=menu_cxc)
menu.add_cascade(label="CXP", menu=menu_cxp)
menu.add_cascade(label="INV", menu=menu_inv)
menu.add_cascade(label="FAC", menu=menu_fac)
menu.add_cascade(label="NOM", menu=menu_nom)
menu.add_cascade(label="AFI", menu=menu_afi)
menu.add_cascade(label="EST", menu=menu_est)
menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Se crean las subopciones para "Archivo"
menu_archivos.add_command(label="MGA")
menu_archivos.add_command(label="INF")
menu_archivos.add_command(label="CXC")
menu_archivos.add_command(label="CXP")
menu_archivos.add_command(label="INV")
menu_archivos.add_command(label="FAC")
menu_archivos.add_command(label="NOM")
menu_archivos.add_command(label="AFI")
menu_archivos.add_command(label="EST")
menu_archivos.add_separator()
menu_archivos.add_command(label="Salir", command=root.quit)

#######
# MGA #
#######
# Se crean las subopciones para "MGA > Mantenimiento"
menu_mga_mtto = tk.Menu(menu_mga, tearoff=0)
menu_mga_mtto.add_command(label="Mantenimiento de Cuentas")
menu_mga_mtto.add_command(label="Creación de Indices")
menu_mga_mtto.add_command(label="Diarios de Mantenimiento")
# Se crea la cascada de "Mantenimiento" al menú "MGA > Mantenimiento"
menu_mga.add_cascade(label="Mantenimiento del Sistema", menu=menu_mga_mtto)

# Se crean las subopciones para "MGA > Posteo"
menu_mga_post = tk.Menu(menu_mga, tearoff=0)
menu_mga_post.add_command(label="Posteo de los Comprobantes")
menu_mga_post.add_command(label="Carga de Asientos Automaticos")
menu_mga_post.add_command(label="Diarios General de Operaciones")
# Se crea la cascada de "Posteo" al menú "MGA > Posteo"
menu_mga.add_cascade(label="Procesos de Posteo", menu=menu_mga_post)

# Se crean las subopciones para "MGA > Balances"
menu_mga_impr = tk.Menu(menu_mga, tearoff=0)
menu_mga_impr.add_command(label="Balance de Comprobación")
menu_mga_impr.add_command(label="Mayor General Analítico")
menu_mga_impr.add_command(label="Informe de Presupuesto")
# Se crea la cascada de "Balances" al menú "MGA > Balances"
menu_mga.add_cascade(label="Impresión de Balances", menu=menu_mga_impr)

# Se crean las subopciones para "MGA > Procesos"
menu_mga_proc = tk.Menu(menu_mga, tearoff=0)
menu_mga_proc.add_command(label="Cierres Contables")
menu_mga_proc.add_command(label="Consultas de Cuentas")
menu_mga_proc.add_command(label="Mantenimiento de Presupuestos")
menu_mga_proc.add_command(label="Impresión de Datos Históricos")
# Se crea la cascada de "Procesos" al menú "MGA > Procesos"
menu_mga.add_cascade(label="Procesos Especiales", menu=menu_mga_proc)

#######
# INF #
#######
# Se crean las subopciones para "INF > Mantenimiento"
menu_inf_mtto = tk.Menu(menu_inf, tearoff=0)
menu_inf_mtto.add_command(label="Mantenimiento de Informes")
# Se crea la cascada de "Mantenimiento" al menú "INF > Mantenimiento"
menu_inf.add_cascade(label="Mantenimiento de Informes", menu=menu_inf_mtto)

# Se crean las subopciones para "INF > Impresión"
menu_inf_impr = tk.Menu(menu_inf, tearoff=0)
menu_inf_impr.add_command(label="Impresión de Listados")
menu_inf_impr.add_command(label="Impresión de Informes")
# Se crea la cascada de "Impresión" al menú "INF > Impresión"
menu_inf.add_cascade(label="Impresión de Informes", menu=menu_inf_impr)

#######
# CXC #
#######
# Se crean las subopciones para "CXC > Mantenimiento"
menu_cxc_mtto = tk.Menu(menu_cxc, tearoff=0)
menu_cxc_mtto.add_command(label="Mantenimiento de Códigos de Financiamiento")
menu_cxc_mtto.add_command(label="Mantenimiento de Bancos")
menu_cxc_mtto.add_command(label="Mantenimiento de Clientes")
menu_cxc_mtto.add_command(label="Diarios de Mantenimiento")
# Se crea la cascada de "Mantenimiento" al menú "CXC > Mantenimiento"
menu_cxc.add_cascade(label="Mantenimiento del Sistema", menu=menu_cxc_mtto)

# Se crean las subopciones para "CXC > Posteo"
menu_cxc_post = tk.Menu(menu_cxc, tearoff=0)
menu_cxc_post.add_command(label="Posteo de los Movimientos")
menu_cxc_post.add_command(label="Diario del Movimiento")
menu_cxc_post.add_command(label="Informe de Variaciones")
# Se crea la cascada de "Posteo" al menú "CXC > Posteo"
menu_cxc.add_cascade(label="Procesos de Posteo", menu=menu_cxc_post)

# Se crean las subopciones para "CXC > Balances"
menu_cxc_impr = tk.Menu(menu_cxc, tearoff=0)
menu_cxc_impr.add_command(label="Balance / Análisis de Antiguedad")
menu_cxc_impr.add_command(label="Estados de Cuenta")
menu_cxc_impr.add_command(label="Documentos al Cobro")
menu_cxc_impr.add_command(label="Documentos en los Bancos")
# Se crea la cascada de "Balances" al menú "CXC > Balances"
menu_cxc.add_cascade(label="Impresión de Balances", menu=menu_cxc_impr)

# Se crean las subopciones para "CXC > Procesos"
menu_cxc_proc = tk.Menu(menu_cxc, tearoff=0)
menu_cxc_proc.add_command(label="Cierres Contables")
menu_cxc_proc.add_command(label="Auditoría de Base de Datos")
# Se crea la cascada de "Procesos" al menú "CXC > Procesos"
menu_cxc.add_cascade(label="Procesos Especiales", menu=menu_cxc_proc)

# Se crean las subopciones para "CXC > Consultas"
menu_cxc_cons = tk.Menu(menu_cxc, tearoff=0)
menu_cxc_cons.add_command(label="Consulta Saldo Cliente")
menu_cxc_cons.add_command(label="Consulta História Cliente")
# Se crea la cascada de "Balances" al menú "CXC > Balances"
menu_cxc.add_cascade(label="Consultas", menu=menu_cxc_cons)

#######
# CXP #
#######
# Se crean las subopciones para "CXP > Mantenimiento"
menu_cxp_mtto = tk.Menu(menu_cxp, tearoff=0)
menu_cxp_mtto.add_command(label="Mantenimiento de Proveedores")
menu_cxp_mtto.add_command(label="Consulta de Proveedores")
menu_cxp_mtto.add_command(label="Diarios de Mantenimiento")
# Se crea la cascada de "Mantenimiento" al menú "CXP > Mantenimiento"
menu_cxp.add_cascade(label="Mantenimiento del Sistema", menu=menu_cxp_mtto)

# Se crean las subopciones para "CXP > Posteo"
menu_cxp_post = tk.Menu(menu_cxp, tearoff=0)
menu_cxp_post.add_command(label="Posteo de los Movimientos")
menu_cxp_post.add_command(label="Coneversión de Facturas a Giros")
menu_cxp_post.add_command(label="Emisión Automática de Cheques")
menu_cxp_post.add_command(label="Diario del Movimiento")
# Se crea la cascada de "Posteo" al menú "CXP > Posteo"
menu_cxp.add_cascade(label="Procesos de Posteo", menu=menu_cxp_post)

# Se crean las subopciones para "CXP > Balances"
menu_cxp_impr = tk.Menu(menu_cxp, tearoff=0)
menu_cxp_impr.add_command(label="Balance de Comprobación")
menu_cxp_impr.add_command(label="Documentos Pendientes de Pago")
# Se crea la cascada de "Balances" al menú "CXP > Balances"
menu_cxp.add_cascade(label="Impresión de Balances", menu=menu_cxp_impr)

# Se crean las subopciones para "cxp > Procesos"
menu_cxp_proc = tk.Menu(menu_cxp, tearoff=0)
menu_cxp_proc.add_command(label="Cierres Contables")
menu_cxp_proc.add_command(label="Transferencia de Saldos")
menu_cxp_proc.add_command(label="Auditoría de Base de Datos")
# Se crea la cascada de "Procesos" al menú "CXP > Procesos"
menu_cxp.add_cascade(label="Procesos Especiales", menu=menu_cxc_proc)

#######
# INV #
#######
# Se crean las subopciones para "INV > Mantenimiento"
menu_inv_mtto = tk.Menu(menu_inv, tearoff=0)
menu_inv_mtto.add_command(label="Mantenimiento de Almacenes")
menu_inv_mtto.add_command(label="Mantenimiento de Productos")
menu_inv_mtto.add_command(label="Cambios en la lista de Precios")
menu_inv_mtto.add_command(label="Diarios de Mantenimiento")
# Se crea la cascada de "Mantenimiento" al menú "INV > Mantenimiento"
menu_inv.add_cascade(label="Mantenimiento del Sistema", menu=menu_inv_mtto)

# Se crean las subopciones para "INV > Posteo"
menu_inv_post = tk.Menu(menu_inv, tearoff=0)
menu_inv_post.add_command(label="Posteo de las Operaciones")
menu_inv_post.add_command(label="Diarios General de Operaciones")
# Se crea la cascada de "Posteo" al menú "INV > Posteo"
menu_inv.add_cascade(label="Procesos de Posteo", menu=menu_inv_post)

# Se crean las subopciones para "INV > Balances"
menu_inv_impr = tk.Menu(menu_inv, tearoff=0)
menu_inv_impr.add_command(label="Informe de Existencias")
menu_inv_impr.add_command(label="Balance del Inventario")
# Se crea la cascada de "Balances" al menú "INV > Balances"
menu_inv.add_cascade(label="Impresión de Balances", menu=menu_inv_impr)

# Se crean las subopciones para "INV > Procesos"
menu_inv_proc = tk.Menu(menu_inv, tearoff=0)
menu_inv_proc.add_command(label="Cierres Contables")
menu_inv_proc.add_command(label="Consultas de Productos")
menu_inv_proc.add_command(label="Composición de Productos")
menu_inv_proc.add_command(label="Cambio del Costo Estandar")
menu_inv_proc.add_command(label="Informe para la Toma Fisica")
menu_inv_proc.add_command(label="Lista de Precios")
menu_inv_proc.add_command(label="Lista de Seriales")
# Se crea la cascada de "Procesos" al menú "INV > Procesos"
menu_inv.add_cascade(label="Procesos Especiales", menu=menu_inv_proc)

#######
# FAC #
#######
# Se crean las subopciones para "FAC > Posteo"
menu_fac_post = tk.Menu(menu_fac, tearoff=0)
menu_fac_post.add_command(label="Carga de los Pedidos")
menu_fac_post.add_command(label="Emisión Ordenes de Despacho")
menu_fac_post.add_command(label="Cambio de Pedidos a Facturas")
menu_fac_post.add_command(label="Carga de las Facturas")
menu_fac_post.add_command(label="Carga de las Notas de Débito")
menu_fac_post.add_command(label="Carga de las Notas de Crédito")
# Se crea la cascada de "Posteo" al menú "FAC > Posteo"
menu_fac.add_cascade(label="Procesos de Posteo", menu=menu_fac_post)

# Se crean las subopciones para "FAC > Documentos"
menu_fac_impr = tk.Menu(menu_fac, tearoff=0)
menu_fac_impr.add_command(label="Impresión de Registros de Ventas")
menu_fac_impr.add_command(label="Impresión Diario de Inventario")
menu_fac_impr.add_command(label="Impresión de los Documentos")
menu_fac_impr.add_command(label="Relación de Giros Emitidos")
menu_fac_impr.add_command(label="Impresión de los Giros")
# Se crea la cascada de "Balances" al menú "FAC > Documentos"
menu_fac.add_cascade(label="Impresión de Documentos", menu=menu_fac_impr)

# Se crean las subopciones para "FAC > Depuración"
menu_fac_proc = tk.Menu(menu_fac, tearoff=0)
menu_fac_proc.add_command(label="Depuración Diaria de Pedidos") 
# Se crea la cascada de "Procesos" al menú "FAC > Procesos"
menu_fac.add_cascade(label="Procesos Especiales", menu=menu_fac_proc)

#######
# NOM #
#######
# Se crean las subopciones para "NOM > Mantenimiento"
menu_nom_mtto = tk.Menu(menu_nom, tearoff=0)
menu_nom_mtto.add_command(label="Mantenimiento de Conceptos")
menu_nom_mtto.add_command(label="Mantenimiento de Departamentos")
menu_nom_mtto.add_command(label="Mantenimiento de Empleados")
menu_nom_mtto.add_command(label="Diarios de Mantenimiento")
# Se crea la cascada de "Mantenimiento" al menú "NOM > Mantenimiento"
menu_nom.add_cascade(label="Mantenimiento del Sistema", menu=menu_nom_mtto)

# Se crean las subopciones para "NOM > Posteo"
menu_nom_post = tk.Menu(menu_nom, tearoff=0)
menu_nom_post.add_command(label="Posteo a Empleados/Conceptos")
menu_nom_post.add_command(label="Posteos Excepciones Nómina")
menu_nom_post.add_command(label="Diarios de Movimientos")
# Se crea la cascada de "Posteo" al menú "NOM > Posteo"
menu_nom.add_cascade(label="Movimiento Normal de Nómina", menu=menu_nom_post)

# Se crean las subopciones para "NOM > Cálculo"
menu_nom_calc = tk.Menu(menu_nom, tearoff=0)
menu_nom_calc.add_command(label="Cálculo Automático de Nómina")
menu_nom_calc.add_command(label="Impresión de Recibos de Pago")
menu_nom_calc.add_command(label="Impresión de Diario de Nómina")
menu_nom_calc.add_command(label="Impresión Diario de Nómina")
menu_nom_calc.add_command(label="Informe de Conceptos de Nómina")
menu_nom_calc.add_command(label="Distribución Departamental")
menu_nom_calc.add_command(label="Relación de Pagos de Nómina")
menu_nom_calc.add_command(label="Informe Situación de Ahorro")
menu_nom_calc.add_command(label="Cierre del Proceso de Nómina")
# Se crea la cascada de "Cálculo" al menú "NOM > Cálculo"
menu_nom.add_cascade(label="Proceso de Cálculo de Nómina", menu=menu_nom_calc)

# Se crean las subopciones para "NOM > Procesos"
menu_nom_proc = tk.Menu(menu_nom, tearoff=0)
menu_nom_proc.add_command(label="Informe del Seguro Social")
menu_nom_proc.add_command(label="Informe del Ministerio del Trabajo")
menu_nom_proc.add_command(label="Informe para el I.S.L.R.")
menu_nom_proc.add_command(label="Informe Mensual de Conceptos")
menu_nom_proc.add_command(label="Cierre Mensual (Intereses)")
# Se crea la cascada de "Procesos" al menú "NOM > Procesos"
menu_nom.add_cascade(label="Procesos Especiales", menu=menu_nom_proc)

#######
# AFI #
#######
# Se crean las subopciones para "AFI > Mantenimiento"
menu_afi_mtto = tk.Menu(menu_afi, tearoff=0)
menu_afi_mtto.add_command(label="Mantenimiento de Activos")
menu_afi_mtto.add_command(label="Consulta de Activos")
menu_afi_mtto.add_command(label="Diario de Mantenimiento")
menu_afi_mtto.add_command(label="Depuración de Auditoría")
# Se crea la cascada de "Mantenimiento" al menú "AFI > Mantenimiento"
menu_afi.add_cascade(label="Mantenimiento del Sistema", menu=menu_afi_mtto)

# Se crean las subopciones para "AFI > Posteo"
menu_afi_post = tk.Menu(menu_afi, tearoff=0)
menu_afi_post.add_command(label="Posteo de Activos")
menu_afi_post.add_command(label="Diarios de Movimiento")
# Se crea la cascada de "Posteo" al menú "AFI > Posteo"
menu_afi.add_cascade(label="Procesos de Posteo", menu=menu_afi_post)

# Se crean las subopciones para "AFI > Balances"
menu_afi_impr = tk.Menu(menu_afi, tearoff=0)
menu_afi_impr.add_command(label="Balance de Comprobación")
menu_afi_impr.add_command(label="Informe A-30")
# Se crea la cascada de "Balances" al menú "AFI > Balances"
menu_afi.add_cascade(label="Impresión de Balances", menu=menu_afi_impr)

# Se crean las subopciones para "AFI > Procesos"
menu_afi_proc = tk.Menu(menu_afi, tearoff=0)
menu_afi_proc.add_command(label="Cierres Mensual")
# Se crea la cascada de "Procesos" al menú "AFI > Procesos"
menu_afi.add_cascade(label="Procesos Especiales", menu=menu_afi_proc)

#######
# EST #
#######
# Se crean las subopciones para "EST > Mantenimiento"
menu_est_mtto = tk.Menu(menu_est, tearoff=0)
menu_est_mtto.add_command(label="Mantenimiento Zona de Ventas")
menu_est_mtto.add_command(label="Mantenimiento de Vendedores")
menu_est_mtto.add_command(label="Mantenimiento Casa de Representación")
menu_est_mtto.add_command(label="Mantenimiento Tipo de Clientes")
menu_est_mtto.add_command(label="Mantenimiento Tipo de Productos")
menu_est_mtto.add_command(label="Carga de Estimados de Ventas")
menu_est_mtto.add_command(label="Carga Rango de Comisiones")
menu_est_mtto.add_command(label="Diarios de Mantenimiento")
# Se crea la cascada de "Mantenimiento" al menú "MGA > Mantenimiento"
menu_est.add_cascade(label="Mantenimiento del Sistema", menu=menu_est_mtto)

# Se crean las subopciones para "EST > Balances"
menu_est_impr = tk.Menu(menu_est, tearoff=0)
menu_est_impr.add_command(label="Ventas por Zona de Ventas")
menu_est_impr.add_command(label="Ventas por Vendedores")
menu_est_impr.add_command(label="Ventas por Vendedor/Producto")
menu_est_impr.add_command(label="Ventas por Productos")
menu_est_impr.add_command(label="Ventas por Por Tipo Cliente/Producto")
menu_est_impr.add_command(label="Comisiones de Ventas")
# Se crea la cascada de "Balances" al menú "EST > Balances"
menu_est.add_cascade(label="Impresión de Balances", menu=menu_est_impr)

# Se crean las subopciones para "MGA > Procesos"
menu_est_proc = tk.Menu(menu_est, tearoff=0)
menu_est_proc.add_command(label="Cierres Contables")
menu_est_proc.add_command(label="Informes de Estimados de Venta")
# Se crea la cascada de "Procesos" al menú "MGA > Procesos"
menu_est.add_cascade(label="Procesos Especiales", menu=menu_est_proc)

# Se muestra la barra de menú en la ventana principal
root.config(menu=menu)

# Bucle de ejecución del programa
root.mainloop()