"""
Version: 1.0.0
Date: 1/7/2023

* VICSO-Asesores Empresariales, C.A.
* Copyright (C) VICSO-Asesores Empresariales, C.A.  1990-2023
"""
###########
# Imports #
###########
import tkinter as tk
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
import subprocess
import sys
import os
import qmclient as qm

###################################
# Efecto Hoover y Leave del Ratón #
###################################
def on_enter1(e):
    e.widget['background'] = '#FF8C00'

def on_leave1(e):
    e.widget['background'] = '#8B0000'
    
def on_enter2(e):
    e.widget['background'] = '#FF8C00'

def on_leave2(e):
    e.widget['background'] = '#483D8B'

def on_enter3(e):
    e.widget['background'] = '#FF8C00'

def on_leave3(e):
    e.widget['background'] = '#006400'

def test():
    if usernameEntry.get() != "":
        usernameEntry.config(state = DISABLED, bg = "#ffffff")
        passwordEntry.delete(0, 'end')
        passwordEntry.focus()
        passwordEntry.config(state = NORMAL, bg="#ccff66")
        return True
    else:
        print("¡error!")
        usernameEntry.config(state = NORMAL, bg = "#ccff66")
        usernameEntry.delete(0, 'end')
        usernameEntry.focus()
        return False

def limpiar():
    usernameEntry.config(state = NORMAL, bg = "#ccff66")
    usernameEntry.delete(0, 'end')
    usernameEntry.focus()
    passwordEntry.config(state = NORMAL, bg="#ffffff")
    passwordEntry.delete(0, 'end')

def validateLogin(username, password):
    #####################
    # Crear Conexion QM #
    #####################
    if not qm.Connect("127.0.0.1", -1, "VICSOASESORES", "Anastasis_123", "ESPANA"):
        print("Failed to connect - ", qm.Error())
        qm.Disconnect()
        sys.exit()

    #########################
    # Open file <USERS> #
    #########################
    fUsers = qm.Open("USERS")
    if fUsers == 0:
        print("No se puede abrir el archivo <USERS>")
        qm.Disconnect()
        sys.exit()

    Codigo = usernameEntry.get()
    password = passwordEntry.get()

    UsersRec, Err = qm.Read(fUsers, Codigo)
    
    if UsersRec == 0:
        print("Falló la comprobación de Credenciales")
        limpiar()
        qm.Disconnect()
    else:
        clave = qm.Extract(UsersRec, 1, 0, 0)

    if password == clave:
        root.destroy()
        qm.Disconnect()
        os.system('python menu.py')
    else:
        print("Falló la comprobación de Credenciales")
        limpiar()
        qm.Disconnect()

######################
# initialize tkinter #
######################
root = Tk()  
root.title('Sistema de Seguridad - Iniciar Sesión')
root.resizable(False, False)

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

####################
# set window color #
####################
root.configure(bg='#54E9E9')

##################################
# Cargar el Icono del formulario #
##################################
root.iconbitmap('imagenes/Nautilus.ico')

###############################
# Load an image in the script #
###############################
img = Image.open(r"imagenes/Nautilus.png")

########################################
# Resize the Image using resize method #
########################################
resized_image = img.resize((100,100), Image.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
imglabel = Label(root, image = new_image).grid(row = 0, column = 0)

#################
# Heading Label #
################# 
headingLabel = Label(root, font = ("Time", 40, "bold"), bg='#54E9E9', text="Sistema ARDI")
headingLabel.grid(row=0, column=1, columnspan=2)

#####################################
# username label and text entry box #
#####################################
usernameLabel = Label(root, font = ("Time", 15, "bold"), bg='#54E9E9', text="Usuario:").grid(row=1, column=1, sticky=E)
username = StringVar()
usernameEntry = Entry(root, border = 0, background="#ccff66", font = ("Time", 15, "normal"), textvariable=username, validate="focusout", validatecommand=test)
usernameEntry.delete(0, 'end')
usernameEntry.focus()
usernameEntry.grid(row=1, column=2, padx=10, pady=10)

#########################################
# password label and password entry box #
#########################################
passwordLabel = Label(root, font = ("Time", 15, "bold"), bg='#54E9E9', text="Contraseña:").grid(row=2, column=1, sticky=E)
password = StringVar()
passwordEntry = Entry(root, border = 0,  font = ("Time", 15, "normal"), state = DISABLED, textvariable=password, show='*')  
passwordEntry.grid(row=2, column=2, padx=10, pady=10)

validateLogin = partial(validateLogin, username, password)

################
# login button #
################
loginButton = Button(root, text="Login", border = 0, font = ("Time", 15, "bold"), width = 5, bg='#8B0000', fg = "#FDFEFE", activebackground='#0052cc', activeforeground='#aaffaa', cursor = "hand2", command=validateLogin)
loginButton.grid(row=4, column=0)  

loginButton.bind("<Enter>", on_enter1)
loginButton.bind("<Leave>", on_leave1)

################
# clear button #
################
clearButton = Button(root, text="Clear", border = 0, font = ("Time", 15, "bold"), width = 5, bg='#483D8B', fg = "#FDFEFE", activebackground='#0052cc', activeforeground='#aaffaa', cursor = "hand2", command=limpiar)
clearButton.grid(row=4, column=1)

clearButton.bind("<Enter>", on_enter2)
clearButton.bind("<Leave>", on_leave2)

#################
# logout button #
#################
img_btn = Image.open("imagenes/exitg.gif")
img_btn = img_btn.resize((20, 20), Image.LANCZOS) # Redimension (Alto, Ancho)
img_btn = ImageTk.PhotoImage(img_btn)

logoutButton = Button(root, text="Salir", image = img_btn, compound = LEFT, border = 0, font = ("Time", 15, "bold"), height = 35, width = 65, bg='#006400', fg = "#FDFEFE", activebackground='#0052cc', activeforeground='#aaffaa', cursor = "hand2", command=root.quit)
logoutButton.grid(row=4, column=2, sticky = W)

logoutButton.bind("<Enter>", on_enter3)
logoutButton.bind("<Leave>", on_leave3)

root.mainloop()