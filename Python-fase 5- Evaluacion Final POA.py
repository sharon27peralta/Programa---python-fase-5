#Nombre: Sharon Juliana Peralta Romero
#Grupo: 213022_806
#Programa: Fundamentos de programación
#Codigo fuente: Autoria propia

#Matriz inventario SJ_METANOIA 
inventario = [
    [101, "Zapatos_nike", 10, 30],
    [102, "Zapatos_adidas", 15, 20],
    [103, "Zapatos_NB", 25, 25],
    [104, "Zapatos_puma", 10, 15]
]
#Función para calcular el stock de los productos 
def calcular_stock(stock_actual, stock_minimo_requerido):
    
    #Calcular si stock actual es menor al mínimo requerido
    if stock_actual < stock_minimo_requerido:

        #Calcular la diferencia entre el stock mínimo requerido y el stock actual
        return stock_minimo_requerido - stock_actual
        
    #Si el stock actual es suficiente, no se necesita reponer
    else:
        return 0

#Lista de productos
print("Lista de productos: ")

#Recorrer la matriz y mostrar los productos
for articulo in inventario:

    # Guardar datos en variables
    codigo = articulo[0]
    nombre_producto = articulo[1]
    stock_actual = articulo[2]
    stock_minimo_requerido = articulo[3]
    
    #Datos en variable
    print("codigo: ", codigo, 
    "nombre: ", nombre_producto, 
    "stock actual: ", stock_actual, 
    "stock mínimo requerido: ", stock_minimo_requerido)
    
    #Calcular el stock necesario para reponer
    stock_necesario = calcular_stock(stock_actual, stock_minimo_requerido
    )
    #Mostrar el stock para reponer
    print(nombre_producto, "- Reponer producto: ", stock_necesario, " unidades"
    )


