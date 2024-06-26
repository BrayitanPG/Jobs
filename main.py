
#*************
# Sena, Mosquera CBA
# Version 2.0
# 09/05/2024
# Ficha: 2877795
#Funcion: Programa de conjuntos y listas con aprendices

#*************



#Importamos las librerias que necesitemos
import msvcrt
from colorama import Back, Fore, init
#Aca iniciamos el colorama
init()
#Importamos la libreria para trabajar con el sistema 
import os

#Importamos todas las funciones que estan en la carpeta "modules", en el archivo "funciones"
from Modules.funciones import mostrar_menu
from Modules.funciones import limpiar_lista
from Modules.funciones import ingresar_aprendiz
from Modules.funciones import listar_aprendices
from Modules.funciones import buscar_por_evaluacion
from Modules.funciones import lista_ficha
from Modules.funciones import borrar_aprendiz
from Modules.funciones import actualizar_aprendiz


#Creamos una funcion que sea la principal
def main():
    #Creamos un bucle while el cual nos permitira preguntarle mas adelante al usuario si quiere volver a empezar o no 
    while True:
        #Mostramos la primera funcion que es la del menu
        mostrar_menu()
        #Le preguntamos al usuario a que funcion quiere ir, del 0 hasta el 7 
        opcion = input(Fore.LIGHTWHITE_EX +  Back.BLACK + "Ingrese a donde quiere ir: ")
        #Si elije la opcion 1, limpiara el contenido de la lista
        if opcion == '1':
            limpiar_lista()
        #Si presiona 2, Lo llevara a el ingreso del aprendiz
        elif opcion == '2':
            ingresar_aprendiz()
            print(" ")  #Estos print son para dejar un espacio
            print(Fore.WHITE + ".... Guardado....")
            print(" ")  #Estos print son para dejar un espacio
            #Que presione enter para continuar
            continuar = input("Presione Enter para  volver al menú: ")
            os.system('cls')  #Limpiamos la pantalla
        #Si presiona 3, lo va a llevar a la lista de aprendices
        elif opcion == '3':
            listar_aprendices()
            print(" ")  #Estos print son para dejar un espacio 
            #Que presione enter para continuar
            continuar = input("Presione Enter para volver al menú: ")
            os.system('cls')  #Limpiamos la pantalla
        #Si presiona 4, lo va a llevar a la busqueda por ficha
        elif opcion =='4':
            lista_ficha()
            print(" ")  #Estos print son para dejar un espacio          
            #Que presione enter para continuar
            continuar = input("Presione Enter para volver al menú: ")
            os.system('cls')  #Limpiamos la pantalla
        #Si presiona 5, lo va a levar a la busqueda por evaluacion(A/D)
        elif opcion == '5':
            buscar_por_evaluacion()
            print(" ")  #Estos print son para dejar un espacio
            #Que presione enter para continuar
            continuar=input("Presione Enter para volver al muenú: ")
            os.system('cls')  #Limpiamos la pantalla
        #Si presiona 6, lo llevara a la funcion de borrar aprendiz
        elif opcion =='6':
            borrar_aprendiz()
            print(" ")  #Estos print son para dejar un espacio
            #Que presione enter para continuar
            continuar = input("Presione Enter para volver al menú: ")
            os.system('cls')  #Limpiamos la pantalla
        #Si presiona 7, lo llevara a la funcion de actualizar aprendiz
        elif opcion == '7':
            actualizar_aprendiz()
            print(" ")  #Estos print son para dejar un espacio
            #Que presione enter para continuar
            continuar = input("Presione Enter para volver al menú: ")
            os.system('cls')  #Limpiamos la pantalla
        #Si presiona 0, lo llevara a la funcion de salir y se saldra del programa
        elif opcion == '0':
            print(" ")  #Estos print son para dejar un espacio
            print("*******    VUELVA PRONTO!!!    ********")  
            break #Esta funcion es para que el programa se pueda salir
        #Si oprime alguna ocpion no valida le saldra este mensaje
        else:
            print("Opción inválida, intente de nuevo.")


#Hace que se ejecute la funcion principal
if __name__ == '__main__':
    main()