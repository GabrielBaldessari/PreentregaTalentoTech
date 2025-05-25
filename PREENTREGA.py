productos = []

while True:
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    entrada = input("Ingrese opción: ")

    if entrada.isdigit():
        opcion = int(entrada)
        if opcion < 1 or opcion > 5:
            print("Número fuera de rango.")
            continue
    else:
        print("No es un número o está vacío.")
        continue

    match opcion:
        case 1:
            while True:
                producto = str(input("Ingrese producto (escriba 'salir' para terminar): ")).strip()
                if producto.lower() == "salir":
                    break
                if producto == " ":
                    print("Está vacío.")
                    continue
                while True:
                    categoria = input("Ingrese la categoría del producto: ").strip()
                    if categoria == "" or categoria.isdigit():
                        print("Categoría inválida. Reintente.")
                        continue
                    else:
                        categoria = categoria.capitalize()
                        break
                while True:
                    precio = input("Ingrese precio del producto: ")
                    if precio.isdigit():
                        precio = float(precio)
                        break
                    else:
                        print("Inválido. Reintente.")
                        continue
                list_producto = [producto.capitalize(), categoria, precio]
                productos.append(list_producto)

        case 2:
            for i, pd in enumerate(productos):
                print(f"{i+1}- PRODUCTO: {pd[0]}   CATEGORÍA: {pd[1]}  PRECIO: {pd[2]}")
            stop = input("(-----------------ENTER PARA VOLVER AL MENÚ---------------) ")

        case 3:
            while True:
                buscar_producto = input("Nombre del producto que desea buscar (escriba 'salir' para dejar de buscar): ").strip()
                if buscar_producto == "" or buscar_producto.isdigit():
                    print("Está vacío o es un número.")
                    continue
                elif buscar_producto == "salir":
                    print("Saliendo...")
                    break
                buscar_producto = str(buscar_producto)
                f = 0
                for i, producto in enumerate(productos):
                    if producto[0] == buscar_producto.capitalize():
                        print("¡Se encontró el producto!")
                        print(f"Posición {i+1}, {producto[0]}, CATEGORÍA: {producto[1]} PRECIO: ${producto[2]}")
                        f = 1
                if f == 0:
                    print("No se encontró el producto.")
                stop = input("------------------ ENTER PARA CONTINUAR --------------")

        case 4:
            while True:
                for i, pd in enumerate(productos):
                    print(f"{i+1}- PRODUCTO: {pd[0]}   CATEGORÍA: {pd[1]}  PRECIO: {pd[2]}")
                Eliminar_producto = input("¿Qué producto desea eliminar por palabra o número? (escriba 'salir'): ")
                if Eliminar_producto == "":
                    print("Vacío. Intente de nuevo...")
                    continue
                if Eliminar_producto.lower() == "salir":
                    print("Saliendo al menú...")
                    break
                elif Eliminar_producto.isdigit():
                    numero = int(Eliminar_producto)
                    if numero < 1 or numero > len(productos):
                        print("Fuera de rango.")
                        continue
                    else:
                        productos.pop(numero - 1)
                        print("Producto removido.")
                        stop = input("--------------ENTER PARA CONTINUAR-----------")
                        continue
                else:
                    f = 0
                    for i, pd in enumerate(productos):
                        if Eliminar_producto.capitalize() == pd[0]:
                            f = 1
                            productos.pop(i)
                            print("Producto removido.")
                            stop = input("--------------ENTER PARA CONTINUAR-----------")
                            break
                    if f == 0:
                        print("El producto no se encontró.")
                        continue

        case 5:
            carga = ["....", ".......", "...."]
            for i, cargas in enumerate(carga):
                print(f"Saliendo del programa{carga[i]}")
            print("¡Cerrado!")
            break
