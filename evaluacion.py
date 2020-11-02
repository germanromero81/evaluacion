import os.path

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
    print("hola 2")


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






 