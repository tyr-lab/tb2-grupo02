# En esta fase se reciben los datos provenientes de la Fase 2.
# Se compara el stock actual de cada producto con
# un stock mínimo establecido. Dependiendo del resultado,
# determina si necesita reposición o si cuenta con stock suficiente.
# Finalmente, envía el resultado a la siguiente fase.


# FASE 3

def evaluar_stock(nombre, stock_actual, stock_minimo):

    print(f"\nProducto: {nombre}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock mínimo: {stock_minimo}")


    if stock_actual < stock_minimo:

        estado = "Stock bajo"
        mensaje = "Se requiere reposición de stock"

        print("Estado: STOCK BAJO")
        print(f"Mensaje: {mensaje}")


    else:

        estado = "Stock suficiente"
        mensaje = "Producto disponible"

        print("Estado: STOCK SUFICIENTE")
        print(f"Mensaje: {mensaje}")


def procesar_fase3(datos_fase2, stock_minimo=10):

    print("\n========== FASE 3 ==========")

    print("Evaluando niveles de stock...\n")


    for nombre, cantidad in datos_fase2.items():

        evaluar_stock(nombre, cantidad, stock_minimo)

        print("-" * 40)