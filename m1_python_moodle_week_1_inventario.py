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

"""
Este codigo esta dividido en tres apartados adaptados segun la guia

1) Entrada de variables: 
- Se pide al usuario ingresar el nombre del producto que desea, y lo ingresado se guarda en la variable "nombre"
- la variable "precio" se pide dentro del ciclo while con el objetivo de evaluar su validez y descartar cualquier opcion no valida. Una vez el usuario entra la variable se recorre cada caracter ingresado mediante la variable "p" usando el ciclo for. En casa iteraciòn se evalua mediante if si el caracter està dentro de la variable "numeros" (esto descarta que el caracter no sea un numero o un punto), si no esta se manda un mensaje de error y se sale del ciclo for mediante break y vuelve a pedir el "precio". Cuando todos los caracteres de "precio" estàn dentro de "numeros" se entra al else, donde se examina que el valor imgresado no sea un punto o que la suma de todos los puntos no supere uno solamente, es decir, que el valor ingresado sea un punto o varios o un numero con muchos puntos incluidos en èl. Si la variable "precio" cumple con todos los criterios se convierte a float.
- Un proceso similar al anterior se aplica a la variable "cantidad", con la intencion de descartar cualquier cadena de caracteres que no se ajuste a un numero entero mayor que cero, por lo que no se evalua los puntos, ya que no se permiten.

2) Calculo aritmetico:
Llegados a este paso y gracias al filtro aplicado a las variables nùmericas "precio" y "cantidad" se procede a calcular la variable "costo_total" para el producto en cuestion. Se multiplica la cantidad del producto por el precio de este y se guarda en "costo_total".

3) Mensaje de salida:
Finalmente, mediante la funcion f print se muestran el producto ingresado (En mayusculas para una mejor lectura), el precio, la cantidad y el costo total (se redondean los decimales a 2 con la funcion round())

"""