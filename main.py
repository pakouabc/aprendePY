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
        print(f"ID2 ==> {id2}")
        if id == productos_identificadores[id2]:
            print(f"Encontrado {id2}")
            print(productos_identificadores[id2])
            print(productos_identificadores)
            index_borrar = id2  
    """Modulo para borrar"""
    # print(f"El valor de index_borrar = {index_borrar}")
    # if index_borrar:
    #     x = productos_identificadores.pop(index_borrar)
    #     print(f"Borrer al {x}")
    # print(productos_identificadores)


def agregar(id):
    """ Seccion  para ingresar un nuevo producto"""
    identificador = input("Dame el numero de id: ")
    if repetido(identificador):
        print("Producto ya existe")
    else :
        nombre = input("Dame el name: ")
        cantidad = input("Dame la cantidad: ")
        productos_lista.append(nombre)
        productos_cantidades.append(cantidad)
        productos_identificadores.append(identificador)
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
        

identificador = input("Dame el codigo identificador del producto :: ")
buscalo(identificador)
identificador = input("Dame el codigo identificador del producto para borrarlo:: ")
borralo(identificador)
        



