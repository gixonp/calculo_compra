"""
Programa: Cálculo del precio total de una compra con descuento e impuesto.
Materia: Programación Básica
"""

def calcular_total_compra(precio_unitario, cantidad, descuento_porc, impuesto_porc):
    """
    Función que calcula el precio total de una compra aplicando un descuento 
    y un impuesto porcentual.
    
    Parámetros:
        precio_unitario (float): El precio de cada unidad del producto.
        cantidad (int): El número de unidades que se compran.
        descuento_porc (float): Porcentaje de descuento (ej. 10 para 10%).
        impuesto_porc (float): Porcentaje de impuesto/IVA (ej. 15 para 15%).
        
    Retorna:
        float: El precio final a pagar.
    """
    # 1. Calcular el subtotal bruto
    subtotal = precio_unitario * cantidad
    
    # 2. Aplicar el descuento
    monto_descuento = subtotal * (descuento_porc / 100)
    subtotal_con_descuento = subtotal - monto_descuento
    
    # 3. Aplicar el impuesto (IVA)
    monto_impuesto = subtotal_con_descuento * (impuesto_porc / 100)
    
    # 4. Calcular el precio total final
    total_final = subtotal_con_descuento + monto_impuesto
    
    return total_final

# --- Bloque Principal (Ejecución del programa) ---
if __name__ == "__main__":
    print("=== SISTEMA DE FACTURACIÓN DE TIENDA ===")
    
    # Datos de ejemplo de un problema de la vida real (ej. comprar zapatos o repuestos)
    precio = 45.50
    cant = 3
    descuento = 10.0  # 10% de descuento
    iva = 15.0        # 15% de impuesto
    
    # Llamada a la función asignando los argumentos
    total_pagar = calcular_total_compra(precio, cant, descuento, iva)
    
    # Mostrar resultados en pantalla
    print(f"Precio unitario: ${precio:.2f}")
    print(f"Cantidad comprada: {cant}")
    print(f"Descuento aplicado: {descuento}%")
    print(f"Impuesto (IVA): {iva}%")
    print(f"-----------------------------------")
    print(f"El precio total de la compra es: ${total_pagar:.2f}")