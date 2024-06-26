
#*************
# Sena, Mosquera CBA
# Version 2.0
# 09/05/2024
# Ficha: 2877795
#Funcion: Programa de conjuntos y listas con aprendices

#*************


import msvcrt
#Importamos el colorama
from colorama import Back, Fore, Style, Cursor, init
#Aca iniciamos el colorama
init()
#Impostamos la libreria os para acceder al sistema
import os


#Funcion para digitar solo numeros
def solo_numeros(prompt):
    while True:
        entrada=input(prompt)
        if entrada.isdigit():
            return entrada
        else:
            print ("Solo se pueden digitar numeros")
            


#Funcion para poder digitar numeros y tenga un minimo de 6 y maximo de 10
def solo_numeros_seis(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit() and 6 <= len(entrada) <= 10:
            return entrada
        else:
            print('\n'"La entrada debe contener solo numeros y un minimo entre 6 y 10 caracteres.")


#Funcion para digitar solo numeros con un limite de 7
def solo_numeros_siete(prompt):
    while True:
        entrada = input(prompt)
        if entrada.isdigit() and len(entrada) == 7:
            return entrada
        else:
            print('\n'"La entrada debe ser solo numeros y debe contener exactamente 7 caracteres")

#Funcion para digitar solo letras
def solo_letras(prompt):
    while True:
        entrada=input(prompt)
        if entrada.replace(" ","").isalpha():
            return entrada
        else:
            print ('\n'"Solo se pueden digitar letras")

#Definimos la funcion de el menu principal
def mostrar_menu():
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX + "*******   BIENVENIDO   ********")  #Le da la bienvenida al usuario al programa
    print(" ") #Estos print son para dejar un espacio
    print(" ") #Estos print son para dejar un espacio
    print("**********************************")
    print(" ")
    #Le pedimos al usuario que opcion quiere digitar
    print(Fore.LIGHTCYAN_EX ,Back.BLACK +  '1. Iniciar lista')
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTCYAN_EX ,Back.BLACK +'2. Ingreso Aprendiz')
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTCYAN_EX ,Back.BLACK +'3. Lista aprendices')
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTCYAN_EX ,Back.BLACK +'4. Lista por fichas')
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTCYAN_EX ,Back.BLACK +'5. Resultado Aprendices por ficha')
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTCYAN_EX ,Back.BLACK +'6. Borrar aprendizes')
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTCYAN_EX ,Back.BLACK +'7. Actualizar información')
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTCYAN_EX ,Back.BLACK +'0. Salir')
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTYELLOW_EX + "**********************************")
    print(" ")  #Estos print son para dejar un espacio


# Creamos una lista vacía para almacenar los diccionarios
lista_aprendices = []


#Funcion para limpiar la lista de aprendices ya ingresada
def limpiar_lista():
    #Esta funcion la usamos para limpiar el contenido que tenga la lista
    lista_aprendices.clear()
    


#Creamos esta funcion para ingresar y crear nuevo aprendiz
def ingresar_aprendiz():
    os.system('cls') #Limpiamos la pantalla
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTYELLOW_EX  + "*******   BIENVENIDO AL REGISTRO DE APRENDICES   ********"+ Style.RESET_ALL) #Nos da la bienvenida al registro de aprendices
    print(" ")  #Estos print son para dejar un espacio
    Nombre = solo_letras( Fore.CYAN + '\n'"Ingrese su nombre y apellido: " + Style.RESET_ALL)
    print(" ")  #Estos print son para dejar un espacio
    Documento = solo_numeros_seis (Fore.CYAN + '\n'"Ingrese su Documento: "+ Style.RESET_ALL)
    print(" ")  #Estos print son para dejar un espacio
    Ficha = solo_numeros_siete (Fore.CYAN + '\n'"Ingrese el numero de ficha de su programa: "+ Style.RESET_ALL)
    print(" ")  #Estos print son para dejar un espacio
    while True:
        #Le pedimos al ususario que digite una evaluacion entre A o D
        Evaluacion = solo_letras (Fore.CYAN + '\n'"Ingrese su evaluación (A o D): "+ Style.RESET_ALL).upper()
        if Evaluacion in ['A', 'D']:
            break
        else:
            #Si el usuario digito una letra que no es valida le saldra este mensaje
            print(Fore.CYAN + '\n'"Ingrese una opción válida (A o D).")
    var = Fore.GREEN if Evaluacion.upper() == 'A' else Fore.LIGHTRED_EX
    # Creamos un diccionario con los datos del aprendiz
    aprendiz = {'Nombre': Nombre, 'Documento': Documento, 'Ficha': Ficha, 'Evaluacion': Evaluacion}

    # Agregamos el diccionario a la lista
    lista_aprendices.append(aprendiz)


#Creamos una funcion para mostrar en pantalla la lista de aprendices que hallamos ingresado
def listar_aprendices():
    os.system('cls') #Limpiamos pantalla
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTYELLOW_EX + "*******   BIENVENIDO A LA LISTA DE APRENDICES  ********" + Style.RESET_ALL)   #Nos da la  bienvenida a la lista de aprendices
    print(" ")  #Estos print son para dejar un espacio
    #Creamos este bucle para hacer el conteo de aprendices y mostrarlos en pantalla
    for aprendiz in lista_aprendices:
        print( Fore.LIGHTWHITE_EX+ f"Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}, Evaluación: {aprendiz['Evaluacion']}" + Style.RESET_ALL)
        print ("  ") #Estos print son para dejar un espacio


#Creamos una funcion para mostrar en pantalla la lista de aprendices que hallamos ingresado por ficha   
def lista_ficha():
    os.system('cls')
    print(" ")  # Estos print son para dejar un espacio
    print(Fore.LIGHTYELLOW_EX + "*******   TODAS LAS FICHAS   ********" + Style.RESET_ALL)   # Nos da la bienvenida a la lista de todas las fichas
    print(" ")  # Estos print son para dejar un espacio
    #Creamos una lista para cada ficha
    fichas_unicas = list(set([aprendiz['Ficha'] for aprendiz in lista_aprendices]))
    for ficha in fichas_unicas:
        print(Fore.BLUE + f"Ficha: {ficha}"+ Style.RESET_ALL)
        for aprendiz in lista_aprendices:
            if aprendiz['Ficha'] == ficha:
                print(f"  Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Evaluación: {aprendiz['Evaluacion']}")
        print(" ")  # Estos print son para dejar un espacio


#Creamos una funcion para buscar por evaluacion(A/D)
def buscar_por_evaluacion():
    os.system('cls')  # Limpiamos la pantalla
    print(" ")  # Dejamos un espacio
    print(Fore.LIGHTYELLOW_EX + "*******   EVALUACIONES DE APRENDICES   ********" + Style.RESET_ALL)  # Título en amarillo
    print(" ")  # Dejamos un espacio

    # Mostramos las evaluaciones A y D
    aprendices_A = [aprendiz for aprendiz in lista_aprendices if aprendiz['Evaluacion'] == 'A']
    aprendices_D = [aprendiz for aprendiz in lista_aprendices if aprendiz['Evaluacion'] == 'D']

    # Mostramos los aprendices con evaluación A en verde
    if aprendices_A:
        print(Fore.GREEN + "Aprendices con evaluación A:" + Style.RESET_ALL)
        for aprendiz in aprendices_A:
            print(f"Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}")

    # Mostramos los aprendices con evaluación D en rojo
    if aprendices_D:
        print(Fore.RED + "Aprendices con evaluación D:" + Style.RESET_ALL)
        for aprendiz in aprendices_D:
            print(f"Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}")

    print(" ")  # Dejamos un espacio


#Creamos una funcion para borrar aprendices
def borrar_aprendiz():
    os.system('cls') #Limpiamos la pantalla
    print(" ")  #Estos print son para dejar un espacio
    print(Fore.LIGHTYELLOW_EX + "*******   BIENVENIDO A LA ELIMINACIÓN DE APRENDICES POR DOCUMENTO   ********" + Style.RESET_ALL) #Nos da la bienvenida a la eliminacion de aprendices por  
    #Creamos este bucle para hacer el conteo de aprendices y mostrarlos en pantalla
    for aprendiz in lista_aprendices:
        print( Fore.LIGHTWHITE_EX+ f"Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}, Evaluación: {aprendiz['Evaluacion']}" + Style.RESET_ALL)
        print ("  ") #Estos print son para dejar un espacio
    print(" ")  #Estos print son para dejar un espacio
    #Le pedimos al usuario  que digite el numero del aprendiz el cual vaya a borrar toda su informacion 
    documento_buscar = solo_numeros_seis('\n' "Ingrese el número de documento del aprendiz a eliminar: " '\n')
    #Esta lista es para almacenar los aprendices que se encuentra en la busqueda
    encontrados = []
    #Este For nos permite hacer la busqueda en la lista donde esta 
    # almacenada la informacion
    for i, aprendiz in enumerate(lista_aprendices):
        #Si en el diccionario esta el dato que ingreso el usuario
        if aprendiz['Documento'] == documento_buscar:
            #Si lo encontro, que lo añada a la lista encontrados
            encontrados.append(i)
    if encontrados:
        print(f"Aprendices encontrados con el documento {documento_buscar}:" '\n')
        for i in encontrados:
            aprendiz = lista_aprendices[i]
            #Si encontro algun resultado, nos muestra los datos de el aprendiz 
            print(Fore.CYAN + f"Nombre:{Style.RESET_ALL} {aprendiz['Nombre']} ,{Fore.CYAN} Documento:{Style.RESET_ALL} {aprendiz['Documento']}, {Fore.CYAN} Ficha:{Style.RESET_ALL} {aprendiz['Ficha']}" '\n')
        #Le preguntamos al usuario si esta seguro que quiere eliminar el apreindiz
        confirmar = input( '\n' f"¿Está seguro de eliminar {len(encontrados)} aprendiz(es)? (s/n): "'\n').lower()
        if confirmar == 's':
            #Si oprime S lo elimina de (lista_aprendices)
            for i in sorted(encontrados, reverse=True):
                del lista_aprendices[i]
            print(Fore.LIGHTRED_EX + "Aprendices eliminados exitosamente."'\n' + Style.RESET_ALL)  #Le decimos al usuario que la operacion fue completada
        else:
            #Esto es por si oprime N
            print(Fore.LIGHTRED_EX + "Operación cancelada."'\n' + Style.RESET_ALL)
    #Si no encuentra ningun aprendiz por el documento digitado
    else:
        print(Fore.LIGHTRED_EX + f"No se encontraron aprendices con el documento {documento_buscar}" + Style.RESET_ALL) 


#Creamos una funcion que nos permita actualizar la informacion de algun aprendiz
def actualizar_aprendiz():
    # Limpia la pantalla de la consola
    os.system('cls')
    print(" ")  #Estos print son para dejar un espacio
    # Imprime un encabezado formateado en color amarillo claro
    print('\n' + Fore.LIGHTYELLOW_EX +  "BIENVENIDO A LA ACTUALIZACIÓN DE APRENDICES POR DOCUMENTO"  + Style.RESET_ALL)
    print(" ")  #Estos print son para dejar un espacio

    for aprendiz in lista_aprendices:
        print('\n' + Fore.LIGHTWHITE_EX+ f"Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}, Evaluación: {aprendiz['Evaluacion']}" + Style.RESET_ALL)
    print(' ')
    # Solicita al usuario ingresar el número de documento del aprendiz a actualizar
    documento_buscar = solo_numeros_seis("Ingrese el número de documento del aprendiz a actualizar: \n")

    # Busca los índices de los aprendices que coinciden con el documento ingresado
    encontrados = [i for i, aprendiz in enumerate(lista_aprendices) if aprendiz['Documento'] == documento_buscar]

    if encontrados:
        
        # Si se encontraron aprendices con el documento ingresado
        
        print('\n' f"Aprendices encontrados con el documento {documento_buscar}:\n")
        # Imprime los datos de los aprendices encontrados
        for i in encontrados:
            aprendiz = lista_aprendices[i]
            print('\n'f"Índice: {i}, Nombre: {aprendiz['Nombre']}, Documento: {aprendiz['Documento']}, Ficha: {aprendiz['Ficha']}, Evaluación: {aprendiz['Evaluacion']}\n")
        try:
            # Solicita al usuario ingresar el índice del aprendiz a actualizar
            indice_actualizar = int(input('\n'"Ingrese el índice del aprendiz a actualizar (0, 1, 2, ...): \n"))
            if indice_actualizar in encontrados:
                
                # Si el índice ingresado es válido
                aprendiz_actualizar = lista_aprendices[indice_actualizar]
                print(f"Datos actuales: Nombre: {aprendiz_actualizar['Nombre']}, Documento: {aprendiz_actualizar['Documento']}, Ficha: {aprendiz_actualizar['Ficha']}, Evaluación: {aprendiz_actualizar['Evaluacion']}\n")
                # Solicita al usuario ingresar el nuevo nombre (si lo desea)
                nuevo_nombre = input('\n'"Ingrese el nuevo nombre (dejar en blanco para no cambiar): \n") or aprendiz_actualizar['Nombre']
                # Solicita al usuario ingresar el nuevo número de ficha (si lo desea)
                nueva_ficha = input('\n'"Ingrese el nuevo número de ficha (dejar en blanco para no cambiar): \n") or aprendiz_actualizar['Ficha']
                # Solicita al usuario ingresar la nueva evaluación (A o D)
                while True:
                    nueva_evaluacion = input('\n'"Ingrese la nueva evaluación (A o D, dejar en blanco para no cambiar): \n").upper() or aprendiz_actualizar['Evaluacion']
                    if nueva_evaluacion in ['A', 'D']:
                        break
                    else:
                        print("Ingrese una opción válida (A o D).")
                # Actualiza los datos del aprendiz
                aprendiz_actualizar['Nombre'] = nuevo_nombre
                aprendiz_actualizar['Ficha'] = nueva_ficha
                aprendiz_actualizar['Evaluacion'] = nueva_evaluacion
                print("Datos actualizados correctamente.")
            else:
                print("Índice inválido.")
        #Esto nos sirve para capturar el error y que no se nos salga del programa 
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        # Si no se encontraron aprendices con el documento ingresado
        print(f"No se encontraron aprendices con el documento {documento_buscar}")