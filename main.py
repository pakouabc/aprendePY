"""
GLOBAL:
    Sistema de almacen para llevar el control de entradas y salidas de productos.
Especifica:
    - indentificador, descripcion, foto, precio, cantidad, 
        fecha llegada, fecha de salida, fecha caducidad, size, ubicacion, 
    Modulos:
        -Agregar productos
        -Consultar
        -Sacar producto
        -Dar de baja o cancelar
        -Reportes (Inventario 'semanas, mes', por Caducar, fecha llegada)
        -Bitacora
"""
#datos globales
productos_lista = ["Botes","Coca-cola", "Cafe", "Pan Birote", "Papitas"]
productos_identificadores = ["312","8712","323","1010", "21"]
productos_cantidades = [10,45,2,9,0 ]
rango = len(productos_lista)

def buscalo(identificador):
    for id in range(rango):
        if identificador == productos_identificadores[id]:
            print("Puesss si lo encontre")
            print(productos_lista[id])
            print(productos_cantidades[id])
            return True
    return False

def repetido(id):
    for id in range(rango):
        if identificador == productos_identificadores[id]:
            return True
    return False

def borralo(id):
    index_borrar = False
    for id2 in range(rango):
        if id == productos_identificadores[id2]:
            print(f"Encontrado {id2}")
            print(productos_identificadores[id2])
            print(productos_identificadores)
            index_borrar = id2  
            print(f"\tEl valor de index_borrar = {index_borrar}")
    """Modulo para borrar"""
    if index_borrar:
         x = productos_identificadores.pop(index_borrar)
         print(f"\t Borrer al {x}")
    else:
        print("\t **Producto no encontrado**")
    print(productos_identificadores)


def agregar():
    """ Seccion  para ingresar un nuevo producto"""
    print("\tAgregando producto nuevo")
    identificador = input("Dame el id: ")
    if repetido(identificador):
        print("\t __Producto ya existe__")
    else :
        nombre = input("Nombre: ")
        cantidad = input("Cantidad: ")
        productos_lista.append(nombre)
        productos_cantidades.append(cantidad)
        productos_identificadores.append(identificador)
        print("\t--Producto Agregado--")
        print(productos_lista)



identificador = input("Dame el codigo identificador del producto :: ")
buscalo(identificador)
identificador = input("Dame el codigo identificador del producto para borrarlo:: ")
borralo(identificador)
agregar()        
print(productos_lista)

#almacen = [productos_lista, productos_identificadores, productos_cantidades]
# bandera = True
# if rango != len(productos_identificadores):
#     print("Errorrrrrr identificadores")
#     bandera = False
    
# if rango != len(productos_cantidades):
#     print("Errorrrrrr cantidades")
#     bandera = False

# if bandera:
#     for p in range(rango):
#         print(f"productos:{productos_identificadores[p]}:{productos_lista[p]},{productos_cantidades[p]}")
        

