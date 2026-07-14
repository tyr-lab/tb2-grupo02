import fase_01
import fase_02
import fase_03
import fase_04
from inventario import inventario_dict

STOCK_MINIMO_INVENTARIO = 30


def main():
    # Mensaje de bienvenida
    fase_01.mensaje("Bienvenido al manejo de inventario")

    while True:
        print("1 - Mostrar Inventario")
        print("2 - Registrar/Actualizar un producto")
        print("3 - Procesar Inventario (Fases 2, 3 y 4)")
        print("0 - Salir")

        opcion = input("Seleccione una opción #: ")

        if opcion == "0":
            break
        elif opcion == "1":
            fase_01.mostrar_inventario(inventario_dict)
        elif opcion == "2":
            prod = input("Producto: ").lower().strip()
            fase_01.registrar_o_actualizar_producto(inventario_dict, prod)
        elif opcion == "3":
            datos_preparados = fase_02.procesar_inventario(inventario_dict)
            if datos_preparados is not None:
                fase_03.procesar_fase3(datos_preparados, STOCK_MINIMO_INVENTARIO)
                fase_04.mostrar_reporte_final(datos_preparados, STOCK_MINIMO_INVENTARIO)
                input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()

