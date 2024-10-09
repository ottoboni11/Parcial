'''
Primer parcial programacion

En la clínica "La Fuerza" se requiere desarrollar un sistema de gestión de pacientes. El sistema
debe gestionar la información de los pacientes atendidos en el día. Para cada paciente, se
almacenará:
• Número de historia clínica (un número entero).
• Nombre del paciente (una cadena de texto).
• Edad del paciente (un número entero).
• Diagnóstico (una cadena de texto).
• Cantidad de días de internación (un número entero).
'''

def cargar_pacientes(pacientes):
    '''
    La funcion recibe como parametro la variable pacientes para almacenar la lista de pacientes.

    Historia clinica tiene una validacion para corroborar que el N° vaya desde 1000 a 9999
    Nombre valida que no sea un string vacio.

    '''

    n = int(input("Ingrese la cantidad de pacientes a cargar."))

    for i in range(n):

        n_historia_clinica = int(input("Ingrese el numero de historia clinica: "))
        while n_historia_clinica > 9999 or n_historia_clinica < 1000: #Validacion de historia clinica.
            n_historia_clinica = int(input("Ingrese el numero de historia clinica: "))

        nombre = input("Ingrese el nombre del paciente: ")

        edad = int(input("Ingrese la edad del paciente: "))
        
        diagnostico = input("Ingrese el diagnostico del paciente: ")

        dias_internado = int(input("Ingrese la cantidad de dias internado del paciente: "))

        print("\n Ingrese el paciente que sigue: \n")

        pacientes.append([n_historia_clinica, nombre, edad, diagnostico, dias_internado])
    
    return pacientes

def mostrar_pacientes(pacientes):
    '''
    Muestra los pacientes primero revisando si la lista posee algun paciente((Revisa si es TRUE o FALSE))
    Luego mediante un for printea cada paciente con el formato aclarado.
    En caso de no haber ningun paciente, dara el aviso.
    '''

    if pacientes:
        print("\nPacientes internados: ")
        for paciente in pacientes:
            print(f"N° Historia clinica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnostico: {paciente[3]}, Dias internado: {paciente[4]}")
    else:
        print("No hay ningun paciente ingresado aun.")

def buscar_pacientes(pacientes, n_historia):
    '''
    Mediante un for recorre la lista de pacientes corroborando que el numero de historia clinica sea igual al ingresado mediante un input.
    Se corrobora indicando el indice que en este caso es 0 donde se encuentran los N° de historia clinica.
    En caso de no haber coincidencias, retorna NONE y asi nos dara el aviso de que no hay coincidencias.
    '''
    for paciente in pacientes:
        if paciente[0] == n_historia:
            return paciente
    return None

def ordenar_pacientes(pacientes):
    '''
    Algoritmo de ordenamiento bubble sorting con desempaquetamiento.
    Al principio funcionaba pero nose que cambié en el codigo y ahora me sobreescribe la lista cada vez que lo uso, me gustaria saber cual fue el error :(

    '''

    for i in range(len(pacientes)):
        for j in range(0, len(pacientes) - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j] 
                #Esto se podria reemplazar con auxiliares de la siguiente manera.
                # aux = pacientes[j]
                # pacientes[j] = pacientes[j + 1]
                # pacientes[j + 1] = aux

    print("\n Pacientes ordenados por N° de Historia clinica de manera ascendente.")

def mostrar_mas_dias_internado(pacientes):
    mas_dias = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > mas_dias[4]:
            mas_dias = paciente
    print(f"El paciente con mas dias de internacion es: {mas_dias}")

def mostrar_menos_dias_internado(pacientes):
    menos_dias = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < menos_dias[4]:
            menos_dias = paciente
    print(f"El paciente con mas dias de internacion es: {menos_dias}")

def mostrar_pacientes_5_dias(pacientes):
    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            contador += 1
    return contador


def promediar_dias_internacion(pacientes):
    total_dias = 0

    for paciente in pacientes:
        total_dias += paciente[4]

    cantidad_pacientes = len(pacientes)

    if cantidad_pacientes > 0:
        promedio = total_dias / cantidad_pacientes
    else:
        promedio = 0

    return promedio


def menu():
    salir = ""
    pacientes = []

    while salir != "Salir":
        print("\nSistema de gestión de clinica.")
        print("1. Cargar pacientes")
        print("2. Mostrar todos los pacientes")
        print("3. Buscar pacientes por numero de historia clinica")
        print("4. Ordenar pacientes por numero de historia clinica")
        print("5. Mostrar pacientes con mas dias de internacion")
        print("6. Mostrar pacientes con menos dias de intenacion")
        print("7. Cantidad de pacientes con mas de 5 dias de internacion")
        print("8. Promedio de los dias de internacion de todos los pacientes")
        print("9. Salir")
        opcion = input("Elija una opcion: ")

        if opcion == "1":
            pacientes = cargar_pacientes(pacientes)

        elif opcion == "2":
            mostrar_pacientes(pacientes)

        elif opcion == "3":
            numero_h_c = int(input("Ingrese el numero de historia clinica del paciente a buscar"))
            paciente = buscar_pacientes(pacientes, numero_h_c)
            if paciente:
                print(f"\n Paciente encontrado: {paciente}")
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "4":
            pacientes = ordenar_pacientes(pacientes)

        elif opcion == "5":
            mostrar_mas_dias_internado(pacientes)

        elif opcion == "6":
            mostrar_menos_dias_internado(pacientes)

        elif opcion == "7":
            cantidad_pacientes = mostrar_pacientes_5_dias(pacientes)
            print(f"Cantidad de pacientes con mas de 5 dias de internacion: {cantidad_pacientes}")

        elif opcion == "8":
            promedio = promediar_dias_internacion(pacientes)
            print(f"El promedio de dias de internacion de todos los pacientes es de: {promedio}")

        elif opcion == "9":
            print("Cerrando programa...")
            salir = "Salir"
        else:
            print("Ingresó una opcion invalida. Pruebe una vez mas.")

menu()