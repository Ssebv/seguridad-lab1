import os

from desafios.desafio1 import EjecutarDesafio1
from desafios.desafio2 import EjecutarDesafio2
from desafios.testCifrado import Ejecutartest   

def main():
    while True:
        print("Menú:")
        print("1. Ejecutar Desafío 1")
        print("2. Ejecutar Desafío 2")
        print("3. Ejecutar Test")
        print("0. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            os.system("clear")
            print("Ejecutando Desafío 1...")
            EjecutarDesafio1()


        elif opcion == "2":
            os.system("clear")
            print("Ejecutando Desafío 2...")
            EjecutarDesafio2()
        
        elif opcion == "3":
            os.system("clear")
            print("Ejecutando Desafío 3...")
            Ejecutartest()

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()