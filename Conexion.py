##################################
# Importar los database conector #
##################################
import mysql.connector
from mysql.connector import errorcode, MySQLConnection
import qmclient as qm
import sys

########################
# Crear conexión MYSQL #
########################
try:
  db_connection = MySQLConnection(
    host="localhost",
    user="root",
    password="jOrSLDINk7yKbIAM",
    port = "3306",
    database="vicsoasesores",
  )
  print("Se conecto correctamente a la Base de Datos")

  #############################
  # getting the cursor object #
  #############################
  cursor = db_connection.cursor()

  #########################
  # Inicializar Variables #
  #########################
  VM = chr(253)

  #####################
  # Crear Conexion QM #
  #####################
  if not qm.Connect("127.0.0.1", -1, "VICSOASESORES", "Anastasis_123", "ESPANA"):
     print("Failed to connect - ", qm.Error())
     sys.exit()

############
# Countries #
#############
  #########################################################
  # Mostrar todos los registros de un archivo <countries> #
  #########################################################
  sql = "SELECT * FROM countries"
  cursor.execute(sql)
  myresult = cursor.fetchall()

  #########################
  # Open file <COUNTRIES> #
  #########################
  fCountries = qm.Open("COUNTRIES")
  if fCountries == 0:
    print("No se puede abrir el archivo <COUNTRIES>")
    sys.exit()

  ####################################################
  # Lectura de los Registros del archivo <countries> #
  ####################################################
  for x in myresult:
    Codigo = str(x[0])
    iso2 = x[1]
    Mayusc = x[2]
    Minus = x[3]
    iso3 = x[4]
    if iso3 is None:
      iso3 = "NULL"
    isonum = str(x[5])
    if isonum is None:
      isonum = "NULL"
    phone = str(x[6])

    #############################################
    # Armar el Registro del archivo <Countries> #
    #############################################
    CountriesRec, Err = qm.Read(fCountries, Codigo)
    CountriesRec = qm.Replace(CountriesRec, 1, 0, 0, iso2)
    CountriesRec = qm.Replace(CountriesRec, 2, 0, 0, Mayusc)
    CountriesRec = qm.Replace(CountriesRec, 3, 0, 0, Minus)
    CountriesRec = qm.Replace(CountriesRec, 4, 0, 0, iso3)
    CountriesRec = qm.Replace(CountriesRec, 5, 0, 0, isonum)
    CountriesRec = qm.Replace(CountriesRec, 6, 0, 0, phone)

    ##################################
    # Grabar el Registro <Countries> #
    ##################################
    qm.Write(fCountries, Codigo, CountriesRec)
  qm.Close(fCountries)
  print("Se cerró el archivo <COUNTRIES>")

#############
# Languages #
#############
  #########################################################
  # Mostrar todos los registros de un archivo <languages> #
  #########################################################
  sql = "SELECT * FROM languages"

  cursor.execute(sql)
  myresult = cursor.fetchall()

  #########################
  # Open file <LANGUAGES> #
  #########################
  fLanguages = qm.Open("LANGUAGES")
  if fLanguages == 0:
    print("No se puede abrir el archivo <LANGUAGES>")
    sys.exit()

  ####################################################
  # Lectura de los Registros del archivo <Languages> #
  ####################################################
  for x in myresult:
    Codigo = str(x[0])
    code = x[1]
    cadena1 = str(x[2])[0:10]
    cadena2 = str(x[2])[11:19]
    cadena3 = cadena2 + ' ' + cadena1
    created_at = cadena3
    cadena4 = str(x[3])[0:10]
    cadena5 = str(x[3])[11:19]
    cadena6 = cadena5 + ' ' + cadena4
    update_at = cadena6

    #############################################
    # Armar el Registro del archivo <Countries> #
    #############################################
    LanguagesRec, Err = qm.Read(fLanguages, Codigo)
    LanguagesRec = qm.Replace(LanguagesRec, 1, 0, 0, code)
    LanguagesRec = qm.Replace(LanguagesRec, 2, 0, 0, created_at)
    LanguagesRec = qm.Replace(LanguagesRec, 3, 0, 0, update_at)

    ##################################
    # Grabar el Registro <Countries> #
    ##################################
    qm.Write(fLanguages, Codigo, LanguagesRec)
  qm.Close(fLanguages)
  print("Se cerró el archivo <LANGUAGES>")

  qm.Disconnect()
except mysql.connector.Error as error:
  if error.errno == errorcode.ER_BAD_DB_ERROR:
    print("La Base de Datos no existe")
  elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("El Nombre del Usuario o el Password está equivocado")
  else:
    print(error)
else:
  db_connection.close()