# En esta fase se recopila la información inicial del inventario.
# El usuario podrá revisar los productos existentes,
# registrar nuevos artículos o actualizar cantidades
# antes de iniciar el análisis del stock.

# FASE 1
def mensaje(msj: str):
    print("\n")
    print("#" * 40)
    print(f"{msj}")
    print("#" * 40)
    print("\n")


def mostrar_inventario(diccionario_productos: dict[str, int]):
    mensaje("Lista de productos")

    for producto, cantidad in diccionario_productos.items():
        print(f"Producto: {producto.ljust(30)} | Stock: {cantidad}")

    print("\n")


def registrar_o_actualizar_producto(inv, nombre_producto):
    existe = nombre_producto in inv
    adjetivo, accion = ("nueva", "actualizado") if existe else ("inicial", "registrado")

    while True:
        cantidad_ingresada = input(
            f"Ingrese la cantidad {adjetivo} para {nombre_producto}: "
        ).strip()

        if cantidad_ingresada.isdigit():
            cantidad = int(cantidad_ingresada)
            inv[nombre_producto] = cantidad

            mensaje(
                f"EXITO - {nombre_producto} {accion} correctamente con {cantidad} productos"
            )
            break
        else:
            mensaje("ADVERTENCIA: Cantidad no valida")
