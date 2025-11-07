print('*** Tienda ***\n')

# ------  ENTRADA DE DATOS ------
# Variable nombre
nombre = input('Ingrese nombre del producto: \n')

# ingreso de precio y validación
numeros = '0123456789.' # valores de validacion
while True:
    precio = input('\nIngrese el precio para "' + nombre + '" : ')
    for p in precio:
        if p not in numeros:
            print('Error: Ingrese un precio válido:')
            break
    else:
        if precio.count('.') > 1 or precio == '.' :
            print('Error: Ingrese un precio válido:')
            continue
        else:
            precio = float(precio)
            break

# Ingreso de cantidad y validacion
enteros = '0123456789' # valores de validacion
while True:
    cantidad = input('\nIngrese la cantidad de "' + nombre + '" que desea: ')
    for c in cantidad:
        if c not in enteros:
            print('Error: por favor ingrese un número entero: ')
            break
    else:
        cantidad = int(cantidad)
        break
  

# ------- OPERACION MATEMATIVA ------
costo_total = precio * cantidad


# ------- Mostrando resultados en consola ------
print(f'\n- Producto:           {nombre.upper()}\n- Precio unitario:    {precio}\n- Cantidad:           {cantidad}\n- Costo final =       {round(costo_total, 2)}')
