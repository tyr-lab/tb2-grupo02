# En esta fase se recibe el inventario actualizado
# proveniente de la Fase 1. Luego se contabilizan
# los productos registrados, se recorre el inventario
# para obtener el nombre y la cantidad de cada producto,
# y finalmente se envía la información a la siguiente
# fase para su procesamiento.

# FASE 2

def procesar_inventario(inventario):

    total_productos = len(inventario)
    procesados = 0

    print("\n========== FASE 2 ==========")

    print(f"¡Inventario recibido! Preparando tus productos")

    print(f"Productos registrados: {total_productos}\n")

    for nombre, cantidad in inventario.items():

        print(f"Producto : {nombre}")
        print(f"Stock    : {cantidad}")

        procesados += 1

        print(f"Procesados: {procesados}/{total_productos}")
        print("-" * 40)

    if procesados == total_productos:
        print("\nTodos los productos fueron procesados correctamente.")
        print("\n Información preparada para la siguiente fase.")
        return inventario
    else:
        print("\nNo se pudieron procesar todos los productos.")
        return None