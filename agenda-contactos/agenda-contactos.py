def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")


def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto")
    telefono = input("Por favor introduzca el teléfono completo del contacto")
    email = input("Por favor introduzca el email completo del contacto")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"Se ha agregado el contacto {nombre} exitosamente")


def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")


def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre de contacto que quiere buscar")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")


def listar_contacto(agenda):
    if agenda:
        print("\nLista de contactos")
        print("\n")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"Email: {info['email']}")
            print("-" * 20)
    else:
        print("La agenda está vacía")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opcion: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contacto(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos ¡Hasta pronto!")
            break
        else:
            print("Por favor seleccione una opción valida (del 1 al 5)")


agenda_contactos()
