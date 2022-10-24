import tkinter as tk
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
import sys
import os
try:
	import qmclient as qm
except:
	print("No exite el Modulo 'qmclient'")
	sys.exit()

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
	if username.get() == "" or password.get() == "":
		usernameEntry.focus()
		print("El campo del Usuario y/o el campo de la Contraseña estan en blanco")
		return

	# Conectarse a la Base de Datos
	qm.ConnectionType(4)
	if not qm.Connect("127.0.0.1", -1, "qmuser", "xiomara", "contabilidad"):
		print("Falló la conexión - ", qm.Error())
		sys.exit()

	# Apertura del Archivo <USUARIOS>
	try:
		fUser = qm.Open("USUARIOS")	
		print(fUser)
	except:
		if fUser == 0:
			print(f"No se puede abrir el archivo <USUARIOS>")
			sys.exit()
	else:
		print("Estoy Feliz")
	finally:
		print("Se logró abrir el archivo <USUARIOS>")

	# Lectura del Archivo <USUARIOS>
	UserId = username.get()
	#print("username entered :", username.get())
	try:
		print(fUser)
		UserRec, Err = qm.Read(fUser, UserId)
		print(UserRec)
	except:
		print("El Usuario " + UserId + " no se pudo leer")
	finally:
		print("El Usuario está correcto")
		UserPass = qm.Extract(UserRec, 1, 0, 0)
		print(UserPass)
		if UserPass == password.get():
			print("Ok")
		print("password entered :", password.get())
	return

#window
root = Tk()  
root.geometry('470x250')  
root.title('Sistema de Seguridad - Iniciar Sesión')
root.resizable(0, 0)

#set window color
root.configure(bg='#54E9E9')

#Load an image in the script
img = Image.open("Nautilus.png")

#Resize the Image using resize method
resized_image = img.resize((100,100), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
imglabel = Label(root, image = new_image).grid(row = 0, column = 0)

# Etiqueta 
tituloLabel = Label(root, font = ("Time", 40, "bold"), bg='#54E9E9', text="Sistema ARDI").grid(row=0, column=1, columnspan=2)

#username label and text entry box
usernameLabel = Label(root, font = ("Time", 15, "bold"), bg='#54E9E9', text="      Usuario:").grid(row=1, column=1)
username = StringVar()
usernameEntry = Entry(root, background="#ccff66", font = ("Time", 15, "normal"), textvariable=username, validate="focusout", validatecommand=test)
usernameEntry.delete(0, 'end')
usernameEntry.focus()
usernameEntry.grid(row=1, column=2, padx=10, pady=10)

#password label and password entry box
passwordLabel = Label(root, font = ("Time", 15, "bold"), bg='#54E9E9', text="Contraseña:").grid(row=2, column=1)
password = StringVar()
passwordEntry = Entry(root, font = ("Time", 15, "normal"), state = DISABLED, textvariable=password, show='*')  
passwordEntry.grid(row=2, column=2, padx=10, pady=10)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(root, text="Login", font = ("Time", 15, "bold"), width = 5, bg='#A4360D', fg = "#FDFEFE", activebackground='#0052cc', activeforeground='#aaffaa', command=validateLogin).grid(row=4, column=0)  

#clear button
clearButton = Button(root, text="Clear", font = ("Time", 15, "bold"), width = 5, bg='#252850', fg = "#FDFEFE", activebackground='#0052cc', activeforeground='#aaffaa', command=limpiar).grid(row=4, column=1)

#logout button
logoutButton = Button(root, text="Salir", font = ("Time", 15, "bold"), width = 5, bg='#008f39', fg = "#FDFEFE", activebackground='#0052cc', activeforeground='#aaffaa', command=root.quit).grid(row=4, column=2, sticky = W)


root.mainloop()