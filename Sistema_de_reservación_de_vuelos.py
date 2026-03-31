marcas = []
modelos = []
aerolineas = []
aviones = []
vuelos = []
reservas = []

def cargar_marcas():
    global marcas

    try:
        archivo = open("Archivos_Txt\aviones.txt", "r")

        for linea in archivo:
            marcas.append(linea.strip())  # .strip() elimina el \n

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío

def guardar_marcas():
    archivo = open("Archivos_Txt/aviones.txt", "w")

    for marca in marcas:
        archivo.write(marca[0] + "\n")
        
    archivo.close()

def cargar_modelos():
    global modelos

    try:
        archivo = open("Archivos_Txt\modeloAviones.txt", "r")

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
        archivo = open("Archivos_Txt\aerolineas.txt", "r")

        for linea in archivo:

            aerolineas.append(linea.strip().split(";"))

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío

def cargar_aviones():
    global aviones

    try:
        archivo = open("Archivos_Txt\avionesAerolineas.txt", "r")

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
        archivo = open("Archivos_Txt\vuelos.txt", "r")

        for linea in archivo:

            partes = linea.strip().split(";")

            partes[9] = int(partes[9])
            partes[10] = int(partes[10])
            partes[11] = int(partes[11])

            vuelos.append(partes)

        archivo.close()

    except:
        pass  # si el archivo no existe, arranca vacío    