import base_datos as bd

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar par de números")
    print("2. Insertar par en posición")
    print("3. Eliminar último par")
    print("4. Eliminar par por posición")
    print("5. Eliminar par por valor")
    print("6. Buscar par")
    print("7. Mostrar lista completa")
    print("8. Crear tupla con números pares")
    print("9. Crear tupla con números impares")
    print("10. Submenú: Editar tuplas")
    print("0. Salir")

def mostrar_submenu():
    print("\n--- SUBMENÚ TUPLAS ---")
    print("1. Modificar valor en tupla de pares")
    print("2. Modificar valor en tupla de impares")
    print("3. Eliminar valor de tupla de pares")
    print("4. Eliminar valor de tupla de impares")
    print("5. Mostrar tuplas")
    print("0. Volver")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            n1 = int(input("Ingrese número 1: "))
            n2 = int(input("Ingrese número 2: "))
            bd.agregar_par(n1, n2)
        elif opcion == '2':
            pos = int(input("Posición donde insertar: "))
            n1 = int(input("Ingrese número 1: "))
            n2 = int(input("Ingrese número 2: "))
            bd.insertar_par(pos, n1, n2)
        elif opcion == '3':
            bd.eliminar_ultimo()
        elif opcion == '4':
            pos = int(input("Posición a eliminar: "))
            bd.eliminar_por_posicion(pos)
        elif opcion == '5':
            n1 = int(input("Ingrese número 1: "))
            n2 = int(input("Ingrese número 2: "))
            bd.eliminar_par_valor([n1, n2])
        elif opcion == '6':
            n1 = int(input("Ingrese número 1: "))
            n2 = int(input("Ingrese número 2: "))
            idx = bd.buscar_par([n1, n2])
            if idx != -1:
                print(f"Par encontrado en posición: {idx}")
            else:
                print("Par no encontrado.")
        elif opcion == '7':
            print("Contenido actual:", bd.lista_numeros)
        elif opcion == '8':
            numeros = list(map(int, input("Ingrese números separados por espacio: ").split()))
            bd.crear_tupla_pares(numeros)
        elif opcion == '9':
            numeros = list(map(int, input("Ingrese números separados por espacio: ").split()))
            bd.crear_tupla_impares(numeros)
        elif opcion == '10':
            while True:
                mostrar_submenu()
                sub = input("Opción del submenú: ")
                if sub == '1':
                    pos = int(input("Posición a modificar en tupla de pares: "))
                    val = int(input("Nuevo valor: "))
                    bd.modificar_valor_tupla('par', pos, val)
                elif sub == '2':
                    pos = int(input("Posición a modificar en tupla de impares: "))
                    val = int(input("Nuevo valor: "))
                    bd.modificar_valor_tupla('impar', pos, val)
                elif sub == '3':
                    val = int(input("Valor a eliminar de tupla de pares: "))
                    bd.eliminar_valor_tupla('par', val)
                elif sub == '4':
                    val = int(input("Valor a eliminar de tupla de impares: "))
                    bd.eliminar_valor_tupla('impar', val)
                elif sub == '5':
                    print("Tupla pares:", bd.tuplas_pares)
                    print("Tupla impares:", bd.tuplas_impares)
                elif sub == '0':
                    break
                else:
                    print("Opción inválida.")
        elif opcion == '0':
            print("¡Programa finalizado!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
