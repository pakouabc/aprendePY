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

productos_lista = ["Botes","Coca-cola", "Cafe", "Pan Birote", "Papitas"]
productos_identificadores = ["312","8712","323","1010", "21"]
productos_cantidades = [10,45,2,9,0 ]
#almacen = [productos_lista, productos_identificadores, productos_cantidades]
rango = len(productos_lista)
bandera = True
if rango != len(productos_identificadores):
    print("Errorrrrrr identificadores")
    bandera = False
if rango != len(productos_cantidades):
    print("Errorrrrrr cantidades")
    bandera = False
if bandera:
    for p in range(rango):
        print(f"productos:{productos_identificadores[p]}:{productos_lista[p]},{productos_cantidades[p]}")
        
""""
Codigo para buscar un producto y mostrar su informacion
"""
id = input("Dame el codigo identificador del producto")