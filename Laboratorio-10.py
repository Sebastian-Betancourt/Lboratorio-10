# Definición de funciones

def capturar_datos():
    print("Capturando datos del usuario y huella...")
    nombre = input("Ingrese su nombre (sin números): ")
    while any(char.isdigit() for char in nombre):
        print("Error: El nombre no puede contener números.")
        nombre = input("Ingrese su nombre (sin números): ")
    
    edad = input("Ingrese su edad: ")
    while not edad.isdigit() or int(edad) < 0:
        print("Error: La edad debe ser un número entero positivo.")
        edad = input("Ingrese su edad: ")
    
    huella = input("Ingrese su huella digital: ")
    return nombre, edad, huella

def generar_clave_acceso():
    print("Generando clave de acceso...")
    clave = "1234"  # Clave de acceso por defecto para este ejemplo
    return clave

def mostrar_datos(nombre, edad, huella, clave):
    print("\nDatos registrados:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Huella digital: {huella}")
    print(f"Clave de acceso: {clave}")

def validar_numero_personas():
    while True:
        try:
            num_personas = int(input("¿Cuántas personas se van a registrar (entre 1 y 20)?: "))
            if 1 <= num_personas <= 20:
                return num_personas
            else:
                print("Error: Debe ingresar un número entre 1 y 20.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Lista para almacenar los registros de personas
registros = []

# Programa principal

print("Bienvenido al sistema de registro de huella digital Huawei P60")

while True:
    print("\nMenú de opciones:")
    print("1. Registrar personas")
    print("2. Generar clave de acceso")
    print("3. Mostrar datos registrados")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Cuantas personas se van a registrar:")
        num_personas = validar_numero_personas()
        for i in range(1, num_personas + 1):
            print(f"\nRegistrando datos de la persona {i}:")
            nombre, edad, huella = capturar_datos()
            registros.append((nombre, edad, huella, generar_clave_acceso())) 

    elif opcion == "2":
        if not registros:
            print("No hay registros para generar claves de acceso.")
      
    