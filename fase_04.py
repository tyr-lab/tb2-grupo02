# FASE 4: Reporte final
def mostrar_reporte_final(inventario, stock_minimo):
    print(">>> Entrando a la Fase 4...")
    print("\n" + "="*40)
    print("   REPORTE FINAL DE INVENTARIO")
    print("="*40)

    urgentes = {k: v for k, v in inventario.items() if v == 0}
    alerta = {k: v for k, v in inventario.items() if 0 < v < stock_minimo}
    optimo = {k: v for k, v in inventario.items() if v >= stock_minimo}

    categorias = {
        "Compras Urgentes": urgentes,
        "Stock en Alerta": alerta,
        "Stock Óptimo": optimo
    }

    for titulo, productos in categorias.items():
        print(f"\n>> {titulo}:")
        
        if len(productos) > 0:
            for nombre, cantidad in productos.items():
                print(f" - {nombre.capitalize()}: {cantidad}")
        else:
            print("   No hay productos en esta categoría.")

    total_analizados = len(inventario)
    productos_con_problemas = len(urgentes) + len(alerta)
    porcentaje_desabastecimiento = (productos_con_problemas / total_analizados) * 100 if total_analizados > 0 else 0

    print("\n" + "-"*40)
    print("MÉTRICAS GLOBALES:")
    print(f" - Total de artículos analizados: {total_analizados}")
    print(f" - % de Desabastecimiento: {porcentaje_desabastecimiento:.2f}%")
    print("-"*40 + "\n")