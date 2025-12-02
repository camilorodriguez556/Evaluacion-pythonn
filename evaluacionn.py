usuarios = {
    "10901": {"nombre": "Catalina Forero", "contrasena": "Qwe1rt#a", "saldo": 10000, "movimientos": []},
    "11123": {"nombre": "Miguel Triana", "contrasena": "A123bxsn", "saldo": 20000, "movimientos": []}
}

print("Bienvenido al sistema")
print("Tienes máximo 3 intentos para iniciar sesión.")

cedula_ingresada = ""
for i in range(3):
    cedula = input("Ingrese su número de cédula: ")

    if cedula in usuarios:
        print(f"Bienvenido {usuarios[cedula]['nombre']}")
        cedula_ingresada = cedula
        break
    else:
        print(f" Documento no encontrado. Intentos restantes: {2 - i}")

if cedula_ingresada == "":
    print("Número de intentos alcanzado. Saliendo del programa.")
    exit()
for i in range(3):
    clave = input("Ingrese su contraseña: ")
    if clave == usuarios[cedula_ingresada]["contrasena"]:
        print("Inicio de sesión exitoso.\n")
        break
    else:
        print(f" Contraseña incorrecta. Intentos restantes: {2 - i}")
else:
    print("Has superado el número de intentos. Programa finalizado.")
    exit()
while True:
    print("MENÚ PRINCIPAL ")
    print("1. Consultar saldo")
    print("2. Consignar dinero")
    print("3. Retirar dinero")
    print("4. Ver movimientos")
    print("5. Salir")
    opc = input("Seleccione una opción: ")
    if opc == "1":
        saldo = usuarios[cedula_ingresada]["saldo"]
        print(f" Su saldo actual es: {saldo}")
    elif opc == "2":
        valor = int(input("Ingrese el valor a consignar: "))
        usuarios[cedula_ingresada]["saldo"] += valor   
        usuarios[cedula_ingresada]["movimientos"].append(f"Consigno {valor}")
        print(f" Consignación exitosa. Nuevo saldo: {usuarios[cedula_ingresada]['saldo']}")
    elif opc == "3":
        valor = int(input("Ingrese el valor a retirar: "))
        if valor <= usuarios[cedula_ingresada]["saldo"]:
            usuarios[cedula_ingresada]["saldo"] -= valor
            usuarios[cedula_ingresada]["movimientos"].append(f"Retiro {valor}")
            print(f" Retiro exitoso. Nuevo saldo: {usuarios[cedula_ingresada]['saldo']}")
        else:
            print(" Fondos insuficientes.")
    elif opc == "4":
        print(" MOVIMIENTOS:")
        
        movs = usuarios[cedula_ingresada]["movimientos"]
        if len(movs) == 0:
            print("No hay movimientos registrados.")
        else:
            for m in movs:
                print("-", m)
    elif opc == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intente nuevamente.")
