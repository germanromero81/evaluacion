import os.path

UBICACION_DIAS = 'dias.csv'

def carga_legajo():
    nombre_archivo = input("Escriba el nombre del archivo: ")
    modo_escritura = "w"
    
    if os.path.isfile(nombre_archivo + ".csv"):
        respuesta = input("El archivo ya existe, desdea modificarlo? si/no")
        
        if respuesta == "si":
            modo_escritura = "a"         
    
    archivo  = open(nombre_archivo + ".csv", modo_escritura) 
    
    cargar_empleados = True

    while cargar_empleados == True:
        print("Datos del empleado: ")
        legajo = input("Escriba el número de legajo: ")
        apellido = input("Escriba el apellido: ")
        nombre = input("Escriba el nombre: ")
        total_de_vacaciones = input ("Total de vacaciones: ")
        archivo.write(legajo + "," + apellido + "," + nombre + "," + total_de_vacaciones)
        seguir_cargando = input("Desea cargar otro empleado? si/no ")
        
        if seguir_cargando == "no":
            cargar_empleados = False


    archivo.close()
    menu_principal()

def dias_disponibles():
    legajo = input("Ingrese un número de legajo: ")
    archivo_dias = open(UBICACION_DIAS, "r")
    lineas = list(archivo_dias)
    contador = 0
    total_dias_usados = 0 

    for linea in lineas:
        if contador > 0:
            columnas = linea.split(",")
            legajo_linea = columnas[0]
            if legajo_linea == legajo:
                total_dias_usados += 1
        contador += 1
    archivo_dias.close()

    nombre_archivo_legajo = input("Escriba el nombre del archivo del legajo: ")
    
    if os.path.isfile(nombre_archivo_legajo + ".csv"):
        archivo_legajo = open(nombre_archivo_legajo + ".csv", "r")
        lineas2 = list(archivo_legajo)
        
        for linea2 in lineas2:
            columnas2 = linea2.split(",")
            if columnas2[0] == legajo:
                total_dias_legajo = columnas2[3]
                dias_usados = int(total_dias_legajo) - int(total_dias_usados)
                print("Le quedan disponibles " + str(dias_usados) + " días")
        
        archivo_legajo.close()
    else:
        print("No existe el archivo")
    
    menu_principal()


def menu_principal():
    print("menu principal ")
    print("1", "carga de legajo")
    print("2", "ver dias disponibles")

    opcion = int(input("eliga una opcion: "))
    
    
    if opcion==1:
        carga_legajo()
    if opcion ==2:
        dias_disponibles()



menu_principal()






 