# File path: travel_booking_system.py

# clientes = {}
# usuario_actual = None  # Variable global para rastrear el estado de inicio de sesión

# def main_menu():
#     while True:
#         print("\n--- Menú Principal ---")
#         print("1. Gestionar Usuarios")
#         print("2. Paquetes")
#         print("3. Reserva de Vuelos")
#         print("4. Reserva de Hoteles")
#         print("5. Salir")

#         opcion = input("Seleccione una opción: ")

#         if opcion == '1':
#             menu_principal_usuarios()
#         elif opcion in ['2', '3', '4']:
#             if usuario_actual:
#                 if opcion == '2':
#                     menu_paquetes()
#                 elif opcion == '3':
#                     reservar_vuelos()
#                 elif opcion == '4':
#                     reserva_hoteles()
#             else:
#                 print("\nDebe iniciar sesión para acceder a estas funciones.")
#         elif opcion == '5':
#             print("Saliendo del sistema. ¡Hasta luego!")
#             break
#         else:
#             print("Opción no válida. Intente nuevamente.")

# def menu_principal_usuarios():
#     global usuario_actual
#     while True:
#         print("\n--- Gestión de Clientes ---")
#         print("1. Registrar Cliente")
#         print("2. Iniciar Sesión")
#         print("3. Cerrar Sesión")
#         print("4. Modificar Cliente")
#         print("5. Eliminar Cliente")
#         print("6. Volver al Menú Principal")

#         opcion = input("Seleccione una opción: ")

#         if opcion == '1':
#             registrar_cliente()
#         elif opcion == '2':
#             iniciar_sesion()
#         elif opcion == '3':
#             if usuario_actual:
#                 print(f"Cerrando sesión del usuario {usuario_actual['nombre']} {usuario_actual['apellido']}.")
#                 usuario_actual = None
#             else:
#                 print("No hay ningún usuario conectado.")
#         elif opcion == '4':
#             if usuario_actual:
#                 modificar_cliente()
#             else:
#                 print("\nDebe iniciar sesión para modificar un cliente.")
#         elif opcion == '5':
#             eliminar_cliente()
#         elif opcion == '6':
#             break
#         else:
#             print("Opción no válida. Intente nuevamente.")

# def registrar_cliente():
#     nombre = input("Ingrese su nombre: ")
#     apellido = input("Ingrese su apellido: ")
#     correo = input("Ingrese su correo: ")
#     telefono = input("Ingrese su número de teléfono: ")

#     if not nombre or not apellido or not correo or not telefono:
#         print("\nError: Todos los campos son obligatorios. Intente nuevamente.")
#         return

#     if correo in clientes:
#         print("\nError: Ya existe un cliente registrado con este correo.")
#         return

#     clientes[correo] = {
#         'nombre': nombre,
#         'apellido': apellido,
#         'telefono': telefono
#     }
#     print("\nCliente registrado con éxito!")

# def iniciar_sesion():
#     global usuario_actual
#     correo = input("Ingrese su correo para iniciar sesión: ")
#     telefono = input("Ingrese su número de teléfono como contraseña: ")

#     if correo in clientes and clientes[correo]['telefono'] == telefono:
#         usuario_actual = clientes[correo]
#         print(f"\nInicio de sesión exitoso. Bienvenido/a {usuario_actual['nombre']} {usuario_actual['apellido']}!")
#     else:
#         print("\nError: Correo o número de teléfono incorrectos.")

# def modificar_cliente():
#     global usuario_actual
#     correo = input("Ingrese el correo del cliente que desea modificar: ")

#     if correo not in clientes:
#         print("\nError: Cliente no encontrado.")
#         return

#     print("\n¿Qué dato desea modificar?")
#     print("1. Nombre")
#     print("2. Apellido")
#     print("3. Correo")
#     print("4. Teléfono")

#     opcion = input("Seleccione una opción: ")

#     if opcion == '1':
#         nuevo_nombre = input("Ingrese el nuevo nombre: ")
#         if nuevo_nombre:
#             clientes[correo]['nombre'] = nuevo_nombre
#             print("\nNombre actualizado con éxito!")
#     elif opcion == '2':
#         nuevo_apellido = input("Ingrese el nuevo apellido: ")
#         if nuevo_apellido:
#             clientes[correo]['apellido'] = nuevo_apellido
#             print("\nApellido actualizado con éxito!")
#     elif opcion == '3':
#         nuevo_correo = input("Ingrese el nuevo correo: ")
#         if nuevo_correo and nuevo_correo not in clientes:
#             clientes[nuevo_correo] = clientes.pop(correo)
#             print("\nCorreo actualizado con éxito!")
#             if usuario_actual and usuario_actual['telefono'] == clientes[nuevo_correo]['telefono']:
#                 usuario_actual = clientes[nuevo_correo]
#         else:
#             print("\nError: El correo ingresado ya existe o no es válido.")
#     elif opcion == '4':
#         nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
#         if nuevo_telefono:
#             clientes[correo]['telefono'] = nuevo_telefono
#             print("\nTeléfono actualizado con éxito!")
#     else:
#         print("\nOpción no válida. Intente nuevamente.")

# def eliminar_cliente():
#     global usuario_actual
#     correo = input("Ingrese el correo del cliente que desea eliminar: ")

#     if correo in clientes:
#         if usuario_actual and usuario_actual['telefono'] == clientes[correo]['telefono']:
#             usuario_actual = None  # Cerrar la sesión del usuario si se está eliminando a sí mismo
#         del clientes[correo]
#         print("\nCliente eliminado con éxito!")
#     else:
#         print("\nError: Cliente no encontrado.")

# def menu_paquetes():
#     while True:
#         print("\n--- Menú de Paquetes Turísticos ---")
#         print("1. Mostrar Paquetes")
#         print("2. Crear Paquete Personalizado")
#         print("3. Volver al Menú Principal")

#         opcion = input("Seleccione una opción: ")

#         if opcion == '1':
#             mostrar_paquetes()
#         elif opcion == '2':
#             crear_paquete_personalizado()
#         elif opcion == '3':
#             break
#         else:
#             print("Opción no válida. Intente nuevamente.")

# def mostrar_paquetes():
#     paquetes_turisticos = {
#         1: {'nombre': 'Paquete Turístico Económico', 'descripcion': 'Hotel 1 Estrella, Desayuno Incluido, Vuelo de ida incluido', 'precio': 300000},
#         2: {'nombre': 'Paquete Turístico Básico', 'descripcion': 'Hotel 3 Estrellas, Todas las comidas incluidas, Transporte al hotel', 'precio': 500000},
#         3: {'nombre': 'Paquete Turístico Premium', 'descripcion': 'Hotel 5 Estrellas, Alimentación completa, Vuelos de ida y vuelta, Transporte al hotel', 'precio': 900000}
#     }

#     print("\n--- Paquetes Turísticos Disponibles ---")
#     for key, paquete in paquetes_turisticos.items():
#         print(f"{key}. {paquete['nombre']}")
#         print(f"   Descripción: {paquete['descripcion']}")
#         print(f"   Precio: ${paquete['precio']} COP\n")

# def crear_paquete_personalizado():
#     nombre_paquete = input("Ingrese un nombre para el paquete personalizado: ")
#     descripcion = input("Ingrese la descripción del paquete: ")
#     precio = input("Ingrese el precio del paquete (en COP): ")

#     print("\n--- Paquete Personalizado Creado ---")
#     print(f"Nombre del paquete: {nombre_paquete}")
#     print(f"Descripción: {descripcion}")
#     print(f"Precio: ${precio} COP")

# def reservar_vuelos():
#     print("\n--- Reserva de Vuelos ---")
#     print("1. Vuelo Económico: $200,000 COP")
#     print("2. Vuelo Regular: $400,000 COP")
#     print("3. Vuelo Premium: $800,000 COP")
#     print("4. Volver al Menú Principal")

#     opcion = input("Seleccione una opción: ")

#     if opcion == '1':
#         print("Ha seleccionado el Vuelo Económico. ¡Reserva completada!")
#     elif opcion == '2':
#         print("Ha seleccionado el Vuelo Regular. ¡Reserva completada!")
#     elif opcion == '3':
#         print("Ha seleccionado el Vuelo Premium. ¡Reserva completada!")
#     elif opcion == '4':
#         print("Volviendo al Menú Principal...")
#     else:
#         print("Opción no válida. Intente nuevamente.")

# def reserva_hoteles():
#     hoteles = {
#         'Cartagena': [
#             {'nombre': 'Hilton: 5 estrellas', 'tipos': [('Habitación individual', 120000), ('Habitación doble', 200000)]},
#             {'nombre': 'Sentar: 4 estrellas', 'tipos': [('Habitación individual', 100000), ('Habitación doble', 180000)]}
#         ],
#         'Santa Marta': [
#             {'nombre': 'Hilton: 5 estrellas', 'tipos': [('Habitación individual', 120000), ('Habitación doble', 200000)]},
#             {'nombre': 'Sentir: 4 estrellas', 'tipos': [('Habitación individual', 100000), ('Habitación doble', 180000)]}
#         ]
#     }

#     destino = input("Ingrese el destino (Cartagena o Santa Marta): ").strip().title()
#     if destino not in hoteles:
#         print("Destino no disponible. Por favor elija entre 'Cartagena' o 'Santa Marta'.")
#         return

#     print(f"\n--- Hoteles disponibles en {destino} ---")
#     for idx, hotel in enumerate(hoteles[destino]):
#         print(f"{idx + 1}. {hotel['nombre']}")
#         for room_idx, (tipo, precio) in enumerate(hotel['tipos']):
#             print(f"   {room_idx + 1}. {tipo} - ${precio} COP por noche")

#     try:
#         hotel_idx = int(input("Seleccione el número del hotel: ")) - 1
#         habitacion_idx = int(input("Seleccione el número del tipo de habitación: ")) - 1
#         noches = int(input("¿Cuántas noches se hospedará?: "))

#         hotel_seleccionado = hoteles[destino][hotel_idx]
#         tipo_habitacion, precio_noche = hotel_seleccionado['tipos'][habitacion_idx]
#         costo_total = precio_noche * noches

#         print(f"\nResumen de la reserva en {hotel_seleccionado['nombre']}")
#         print(f"Habitación: {tipo_habitacion}")
#         print(f"Total: ${costo_total} COP")
#         confirmacion = input("¿Está seguro de la reserva? (sí/no): ").strip().lower()
#         if confirmacion in ['sí', 'si']:
#             print("¡Reserva completada con éxito!")
#         else:
#             print("Reserva cancelada.")
#     except (IndexError, ValueError):
#         print("Error: Entrada inválida. Por favor, intente de nuevo.")


# main_menu()


clientes = {}
usuario_actual = None  

def main_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar Usuarios")
        print("2. Paquetes")
        print("3. Reserva de Vuelos")
        print("4. Reserva de Hoteles")
        print("5. Mostrar Clientes y Reservas")  
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_principal_usuarios()
        elif opcion in ['2', '3', '4']:
            if usuario_actual:
                if opcion == '2':
                    menu_paquetes()
                elif opcion == '3':
                    reservar_vuelos()
                elif opcion == '4':
                    reserva_hoteles()
            else:
                print("\nDebe iniciar sesión para acceder a estas funciones.")
        elif opcion == '5':
            mostrar_clientes_y_reservas() 
        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_principal_usuarios():
    global usuario_actual
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Registrar Cliente")
        print("2. Iniciar Sesión")
        print("3. Cerrar Sesión")
        print("4. Modificar Cliente")
        print("5. Eliminar Cliente")
        print("6. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            if usuario_actual:
                print(f"Cerrando sesión del usuario {usuario_actual['nombre']} {usuario_actual['apellido']}.")
                usuario_actual = None
            else:
                print("No hay ningún usuario conectado.")
        elif opcion == '4':
            if usuario_actual:
                modificar_cliente()
            else:
                print("\nDebe iniciar sesión para modificar un cliente.")
        elif opcion == '5':
            eliminar_cliente()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def registrar_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo: ")
    telefono = input("Ingrese su número de teléfono: ")

    if not nombre or not apellido or not correo or not telefono:
        print("\nError: Todos los campos son obligatorios. Intente nuevamente.")
        return

    if correo in clientes:
        print("\nError: Ya existe un cliente registrado con este correo.")
        return

    clientes[correo] = {
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'reservas': []  
    }
    print("\nCliente registrado con éxito!")

def iniciar_sesion():
    global usuario_actual
    correo = input("Ingrese su correo para iniciar sesión: ")
    telefono = input("Ingrese su número de teléfono como contraseña: ")

    if correo in clientes and clientes[correo]['telefono'] == telefono:
        usuario_actual = clientes[correo]
        print(f"\nInicio de sesión exitoso. Bienvenido/a {usuario_actual['nombre']} {usuario_actual['apellido']}!")
    else:
        print("\nError: Correo o número de teléfono incorrectos.")

def modificar_cliente():
    global usuario_actual
    correo = input("Ingrese el correo del cliente que desea modificar: ")

    if correo not in clientes:
        print("\nError: Cliente no encontrado.")
        return

    print("\n¿Qué dato desea modificar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Correo")
    print("4. Teléfono")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        if nuevo_nombre:
            clientes[correo]['nombre'] = nuevo_nombre
            print("\nNombre actualizado con éxito!")
    elif opcion == '2':
        nuevo_apellido = input("Ingrese el nuevo apellido: ")
        if nuevo_apellido:
            clientes[correo]['apellido'] = nuevo_apellido
            print("\nApellido actualizado con éxito!")
    elif opcion == '3':
        nuevo_correo = input("Ingrese el nuevo correo: ")
        if nuevo_correo and nuevo_correo not in clientes:
            clientes[nuevo_correo] = clientes.pop(correo)
            print("\nCorreo actualizado con éxito!")
            if usuario_actual and usuario_actual['telefono'] == clientes[nuevo_correo]['telefono']:
                usuario_actual = clientes[nuevo_correo]
        else:
            print("\nError: El correo ingresado ya existe o no es válido.")
    elif opcion == '4':
        nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
        if nuevo_telefono:
            clientes[correo]['telefono'] = nuevo_telefono
            print("\nTeléfono actualizado con éxito!")
    else:
        print("\nOpción no válida. Intente nuevamente.")

def eliminar_cliente():
    global usuario_actual
    correo = input("Ingrese el correo del cliente que desea eliminar: ")

    if correo in clientes:
        if usuario_actual and usuario_actual['telefono'] == clientes[correo]['telefono']:
            usuario_actual = None 
        del clientes[correo]
        print("\nCliente eliminado con éxito!")
    else:
        print("\nError: Cliente no encontrado.")

def menu_paquetes():
    while True:
        print("\n--- Menú de Paquetes Turísticos ---")
        print("1. Mostrar Paquetes")
        print("2. Crear Paquete Personalizado")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_paquetes()
        elif opcion == '2':
            crear_paquete_personalizado()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def mostrar_paquetes():
    paquetes_turisticos = {
        1: {'nombre': 'Paquete Turístico Económico', 'descripcion': 'Hotel 1 Estrella, Desayuno Incluido, Vuelo de ida incluido', 'precio': 300000},
        2: {'nombre': 'Paquete Turístico Básico', 'descripcion': 'Hotel 3 Estrellas, Todas las comidas incluidas, Transporte al hotel', 'precio': 500000},
        3: {'nombre': 'Paquete Turístico Premium', 'descripcion': 'Hotel 5 Estrellas, Alimentación completa, Vuelos de ida y vuelta, Transporte al hotel', 'precio': 900000}
    }

    print("\n--- Paquetes Turísticos Disponibles ---")
    for key, paquete in paquetes_turisticos.items():
        print(f"{key}. {paquete['nombre']}")
        print(f"   Descripción: {paquete['descripcion']}")
        print(f"   Precio: ${paquete['precio']} COP\n")

def crear_paquete_personalizado():
    nombre_paquete = input("Ingrese un nombre para el paquete personalizado: ")
    descripcion = input("Ingrese la descripción del paquete: ")
    precio = input("Ingrese el precio del paquete (en COP): ")

    print("\n--- Paquete Personalizado Creado ---")
    print(f"Nombre del paquete: {nombre_paquete}")
    print(f"Descripción: {descripcion}")
    print(f"Precio: ${precio} COP")

def reservar_vuelos():
    print("\n--- Reserva de Vuelos ---")
    print("1. Vuelo Económico: $200,000 COP")
    print("2. Vuelo Regular: $400,000 COP")
    print("3. Vuelo Premium: $800,000 COP")
    print("4. Volver al Menú Principal")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("Ha seleccionado el Vuelo Económico. ¡Reserva completada!")
        agregar_reserva_a_cliente("Vuelo Económico")  
    elif opcion == '2':
        print("Ha seleccionado el Vuelo Regular. ¡Reserva completada!")
        agregar_reserva_a_cliente("Vuelo Regular")  
    elif opcion == '3':
        print("Ha seleccionado el Vuelo Premium. ¡Reserva completada!")
        agregar_reserva_a_cliente("Vuelo Premium")  
    elif opcion == '4':
        print("Volviendo al Menú Principal...")
    else:
        print("Opción no válida. Intente nuevamente.")

def reserva_hoteles():
    hoteles = {
        'Cartagena': [
            {'nombre': 'Hilton: 5 estrellas', 'tipos': [('Habitación individual', 120000), ('Habitación doble', 200000)]},
            {'nombre': 'Sentar: 4 estrellas', 'tipos': [('Habitación individual', 100000), ('Habitación doble', 180000)]}
        ],
        'Santa Marta': [
            {'nombre': 'Hilton: 5 estrellas', 'tipos': [('Habitación individual', 120000), ('Habitación doble', 200000)]},
            {'nombre': 'Sentar: 4 estrellas', 'tipos': [('Habitación individual', 100000), ('Habitación doble', 180000)]}
        ]
    }

    print("\n--- Reserva de Hoteles ---")
    for ciudad, lista_hoteles in hoteles.items():
        print(f"\nHoteles en {ciudad}:")
        for hotel in lista_hoteles:
            print(f"- {hotel['nombre']}:")
            for tipo, precio in hotel['tipos']:
                print(f"  {tipo}: ${precio} COP")
    
    ciudad_seleccionada = input("\nIngrese la ciudad donde desea reservar: ")
    if ciudad_seleccionada in hoteles:
        for hotel in hoteles[ciudad_seleccionada]:
            print(f"\nHotel: {hotel['nombre']}")
            for tipo, precio in hotel['tipos']:
                print(f"{tipo}: ${precio} COP")

            tipo_seleccionado = input("Ingrese el tipo de habitación que desea reservar: ")
            for tipo, precio in hotel['tipos']:
                if tipo_seleccionado.lower() in tipo.lower():
                    print(f"Ha seleccionado {tipo}. ¡Reserva completada!")
                    agregar_reserva_a_cliente(f"Hotel {hotel['nombre']}, {tipo}")  # Agregar reserva
                    break
            else:
                print("Tipo de habitación no válido.")
    else:
        print("Ciudad no válida.")

def agregar_reserva_a_cliente(reserva):
    if usuario_actual:
        usuario_actual['reservas'].append(reserva)
        print(f"Reserva '{reserva}' añadida a su perfil.")
    else:
        print("No hay usuario conectado.")

def mostrar_clientes_y_reservas():
    print("\n--- Clientes y Reservas ---")
    for correo, datos in clientes.items():
        print(f"Cliente: {datos['nombre']} {datos['apellido']} - Correo: {correo}")
        if datos['reservas']:
            print("  Reservas:")
            for reserva in datos['reservas']:
                print(f"   - {reserva}")
        else:
            print("  No tiene reservas.")

main_menu()
