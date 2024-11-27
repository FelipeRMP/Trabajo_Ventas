import random

def generar_codigo_venta():
    while True:
        codigo = random.randint(30000, 80000)
        if codigo % 5 == 0:
            return codigo

def calcular_precio(tipo_producto):
    if tipo_producto == "computadoras":
        while True:
            precio = random.randint(500, 1500)
            if precio % 2 == 0:
                return precio
    elif tipo_producto == "telefonos moviles":
        while True:
            precio = random.randint(300, 800)
            if precio % 3 == 0:
                return precio
    elif tipo_producto == "accesorios electronicos":
        while True:
            precio = random.randint(50, 300)
            if precio % 2 != 0:
                return precio

def calcular_precven(beneficio_tributario, precio_sin_igv):
    if beneficio_tributario == "si":
        return round(precio_sin_igv, 2)
    return round(precio_sin_igv * 1.18, 2)

def ingresar_productos(productos):
    tipo = input("Ingrese el producto: ")
    descripcion = input("Ingrese una descripcion del producto: ")
    beneficio_tributario = input("Tiene beneficio tributario (si/no): ")
    precio_sin_igv = calcular_precio(tipo)
    codigo_producto = generar_codigo_venta()

    producto = {
        'codigo': codigo_producto,
        'tipo': tipo,
        'descripcion': descripcion,
        'beneficio_tributario': beneficio_tributario,
        'precio_sin_igv': precio_sin_igv
    }
    productos.append(producto)
    print("Producto ingresado con éxito")
    return productos

def registrar_venta(productos, ventas, numero_venta):
    codigo_producto = int(input("Ingresar código de servicio: "))
    cantidad = int(input("Ingresar cantidad (1-10): "))

    if cantidad < 1 or cantidad > 10:
        print("Cantidad inválida.")
        return numero_venta

    producto = 0
    for k in productos:
        if k['codigo'] == codigo_producto:
            producto = k
            break
    if producto == 0:
        print("Producto no encontrado.")
        return numero_venta

    precio_venta = calcular_precven(producto['beneficio_tributario'], producto['precio_sin_igv'])
    total_venta = precio_venta * cantidad

    venta = {
        'numero': numero_venta,
        'codigo_producto': codigo_producto,
        'cantidad': cantidad,
        'precio_venta': precio_venta,
        'total_venta': total_venta
    }
    ventas.append(venta)
    print("Venta registrada con éxito.")
    print(venta)
    return numero_venta + 1

def modificar_venta(ventas):
    numero_venta = int(input("Ingrese el número de la venta a modificar: "))
    for venta in ventas:
        if venta['numero'] == numero_venta:
            nueva_cantidad = int(input("Ingrese la nueva cantidad (1-10): "))
            if 1 <= nueva_cantidad <= 10:
                venta['cantidad'] = nueva_cantidad
                venta['total_venta'] = venta['precio_venta'] * nueva_cantidad
                print("Venta modificada con éxito.")
            else:
                print("Cantidad inválida.")
            return
    print("Venta no encontrada.")

def ordenar_ventas_burbuja(ventas):
    n = len(ventas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ventas[j]['total_venta'] > ventas[j + 1]['total_venta']:
                ventas[j], ventas[j + 1] = ventas[j + 1], ventas[j]
    print("Ventas ordenadas por total con éxito.")

def quicksort_ventas(ventas):
    if len(ventas) <= 1:
        return ventas
    else:
        pivot = ventas[0]
        menores = [v for v in ventas[1:] if v['numero'] <= pivot['numero']]
        mayores = [v for v in ventas[1:] if v['numero'] > pivot['numero']]
        return quicksort_ventas(menores) + [pivot] + quicksort_ventas(mayores)

def buscar_venta_binaria(ventas, numero_venta):
    inicio = 0
    fin = len(ventas) - 1
    encontrado = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if ventas[medio]['numero'] == numero_venta:
            encontrado = True
            print("Venta encontrada:", ventas[medio])
            break
        elif ventas[medio]['numero'] < numero_venta:
            inicio = medio + 1
        else:
            fin = medio - 1

    if not encontrado:
        print("Venta no encontrada.")

def mayor_venta(ventas):
    if len(ventas) == 0:
        print("Aún no se ha registrado ventas.")
        return

    mayor_venta = ventas[0]
    for venta in ventas:
        if venta['total_venta'] > mayor_venta['total_venta']:
            mayor_venta = venta

    print(f"Venta con mayor total: {mayor_venta}")


def guardar_informacion(productos, ventas):
    with open('servicios.txt', 'w') as f_productos:
        for producto in productos:
            f_productos.write(
                f"Código: {producto['codigo']}, Tipo: {producto['tipo']}, Descripción: {producto['descripcion']}, "
                f"Beneficio Tributario: {producto['beneficio_tributario']}, Precio: {producto['precio_sin_igv']}\n"
            )

    with open('ventas.txt', 'w') as f_ventas:
        for venta in ventas:
            f_ventas.write(
                f"Número: {venta['numero']}, Código de Producto: {venta['codigo_producto']}, "
                f"Cantidad: {venta['cantidad']}, Precio de Venta: {venta['precio_venta']}, "
                f"Total de Venta: {venta['total_venta']}\n"
            )

    print("Información guardada en archivos de texto.")

def leer_servicios(nom_archivo):
    servicios = []
    f = open(nom_archivo, 'r')
    for line in f:
        partes = line.strip().split(", ")
        servicio = {
            'codigo': int(partes[0].split(": ")[1]),
            'tipo': partes[1].split(": ")[1],
            'descripcion': partes[2].split(": ")[1],
            'beneficio_tributario': partes[3].split(": ")[1],
            'precio_sin_igv': float(partes[4].split(": ")[1])
        }
        servicios.append(servicio)
    f.close()
    return servicios

def leer_ventas(nom_archivo):
    ventas = []
    f = open(nom_archivo, 'r')
    for line in f:
        partes = line.strip().split(", ")
        venta = {
            'numero': int(partes[0].split(": ")[1]),
            'codigo_producto': int(partes[1].split(": ")[1]),
            'cantidad': int(partes[2].split(": ")[1]),
            'precio_venta': float(partes[3].split(": ")[1]),
            'total_venta': float(partes[4].split(": ")[1])
        }
        ventas.append(venta)
    f.close()
    return ventas

def cargar_informacion():
    productos = leer_servicios('servicios.txt')
    ventas = leer_ventas('ventas.txt')
    print("Información cargada con éxito.")
    return productos, ventas

def menu_principal():
    productos = []
    ventas = []
    numero_venta = 100
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar producto")
        print("2. Registrar venta")
        print("3. Modificar venta")
        print("4. Ordenar ventas")
        print("5. Buscar venta")
        print("6. Venta con total más alto")
        print("7. Guardar datos")
        print("8. Cargar datos")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_productos(productos)
        elif opcion == "2":
            numero_venta = registrar_venta(productos, ventas, numero_venta)
        elif opcion == "3":
            modificar_venta(ventas)
        elif opcion == "4":
            ordenar_ventas_burbuja(ventas)
        elif opcion == "5":
            ventas = quicksort_ventas(ventas)
            numero = int(input("Ingrese el número de venta a buscar: "))
            buscar_venta_binaria(ventas, numero)
        elif opcion == "6":
            mayor_venta(ventas)
        elif opcion == "7":
            guardar_informacion(productos, ventas)
        elif opcion == "8":
            productos, ventas = cargar_informacion()
            print("Datos recargados desde los archivos.")
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

menu_principal()
