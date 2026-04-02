# ---------- Variables globales ----------

marcas = []
modelos = []
aerolineas = []
aviones = []
vuelos = []
reservas = []
credenciales = []


# ---------- Esta parte se encarga de cargar todos los archivos ----------


def cargar_todo():

    cargar_marcas()
    cargar_modelos()
    cargar_aerolineas()
    cargar_aviones()
    cargar_vuelos()
    cargar_credenciales()


def cargar_marcas():
    global marcas

    try:
        archivo = open("Archivos_Txt/aviones.txt", "r")

        for linea in archivo:
            marcas.append([linea.strip()])  # .strip() elimina el \n

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío


def cargar_modelos():
    global modelos

    try:
        archivo = open("Archivos_Txt/modeloAviones.txt", "r")

        for linea in archivo:

            partes = linea.strip().split(";")

            partes[2] = int(partes[2])
            partes[3] = int(partes[3])
            partes[4] = int(partes[4])

            modelos.append(partes)

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío


def cargar_aerolineas():
    global aerolineas

    try:
        archivo = open("Archivos_Txt/aerolineas.txt", "r")

        for linea in archivo:

            aerolineas.append(linea.strip().split(";"))

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío


def cargar_aviones():
    global aviones

    try:
        archivo = open("Archivos_Txt/avionesAerolineas.txt", "r")

        for linea in archivo:

            partes = linea.strip().split(";")

            partes[3] = int(partes[3])

            aviones.append(partes)

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío


def cargar_vuelos():
    global vuelos

    try:
        archivo = open("Archivos_Txt/vuelos.txt", "r")

        for linea in archivo:

            partes = linea.strip().split(";")

            partes[9] = int(partes[9])
            partes[10] = int(partes[10])
            partes[11] = int(partes[11])

            vuelos.append(partes)

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío


# ---------- Esta parte se encarga de guardar todos los cambios de los archivos ----------


def guardar_todo():

    lista_a_texto(marcas, "Archivos_Txt/aviones.txt")
    lista_a_texto(modelos, "Archivos_Txt/modeloAviones.txt")
    lista_a_texto(aerolineas, "Archivos_Txt/aerolineas.txt")
    lista_a_texto(aviones, "Archivos_Txt/avionesAerolineas.txt")
    lista_a_texto(vuelos, "Archivos_Txt/vuelos.txt")


def largo_lista(lista):
    contador = 0

    for elemento in lista:
        contador += 1

    return contador - 1


def lista_a_texto(listas, archivo_direccion):

    archivo = open(archivo_direccion, "w")

    for lista in listas:
        longitud_lista = largo_lista(lista)
        contador = 0

        for pos in lista:

            if contador != longitud_lista:
                contador += 1
                archivo.write(str(pos) + ";")

            else:
                archivo.write(str(pos))

        archivo.write("\n")

    archivo.close()


# ---------- Esta parte se encarga de cargar y verificar a los administradores del programa ----------


def cargar_credenciales():
    global credenciales

    try:
        archivo = open("Archivos_Txt/acceso.txt", "r")

        for linea in archivo:
            credenciales.append(linea.strip().split(";"))  # .strip() elimina el \n

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío


def verificar_acceso(usuario, clave):
    global credenciales

    for credencial in credenciales:

        if usuario == credencial[0] and clave == credencial[1]:
            return True

    return False


# ---------- Esta parte se encarga de mostrar, agregar, eliminar y modificar marcas ----------


def mostrar_marcas():
    marcas_listas = ""

    for marca in marcas:
        marcas_listas += marca[0] + "\n"

    return marcas_listas.strip()


def incluir_marca(nombre):
    global marcas

    for marca in marcas:

        if nombre == marca[0]:
            return False

    marcas.append([str(nombre)])

    return True


def eliminar_marca(nombre):
    global marcas

    for modelo in modelos:

        if nombre == modelo[1]:
            return False

    res = []

    for marca in marcas:

        if marca[0] != nombre:
            res.append([marca[0]])

    if res != marcas:
        marcas = res
        return True

    return False


def modificar_marca(nombre_viejo, nombre_nuevo):
    global marcas

    for marca in marcas:

        if nombre_nuevo == marca[0]:
            return False

    for marca in marcas:

        if marca[0] == nombre_viejo:
            marca[0] = nombre_nuevo
            return True

    return False


# ---------- Esta parte se encarga de mostrar, agregar, eliminar y modificar modelos ----------


def mostrar_modelos():
    return modelos


def incluir_modelo(descripcion, marca, ejecutiva, turista, economica):
    global modelos

    for modelo in modelos:

        if modelo[0] == descripcion:
            return False

    modelos.append([descripcion, marca, int(ejecutiva), int(turista), int(economica)])

    return True


def eliminar_modelo(descripcion):
    global modelos

    for avion in aviones:

        if descripcion == avion[2]:
            return False

    res = []

    for modelo in modelos:

        if modelo[0] != descripcion:
            res.append([modelo])

    if res != modelos:
        modelos = res
        return True

    return False


def modificar_modelo(
    descripcion,
    nueva_descripcion,
    nueva_marca,
    nueva_ejecutiva,
    nueva_turista,
    nueva_economica,
):
    global modelos

    for modelo in modelos:

        if modelo[0] == nueva_descripcion:
            return False

    for modelo in modelos:

        if modelo[0] == descripcion:
            modelo[0] = nueva_descripcion
            modelo[1] = nueva_marca
            modelo[2] = int(nueva_ejecutiva)
            modelo[3] = int(nueva_turista)
            modelo[4] = int(nueva_economica)

            return True

    return False
