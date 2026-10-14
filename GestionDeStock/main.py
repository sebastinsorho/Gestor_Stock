import json

def mostrar_menu():
    
    print("===================================================================================")
    print("GESTION DE STOCK")
    print("===================================================================================")

    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Agregar stock")
    print("5. Quitar stock")
    print("6. Quitar producto")
    print("7. Salir")

def agregar_producto():
    try:
        nombre = input("Ingrese nombre del producto: ")
    except ValueError:
        print("Entrada inválida. Ingrese un nombre válido.")
        return
    try:
        precio = float(input("Ingrese precio del producto: "))
    except ValueError:
        print("Entrada inválida. Ingrese un precio válido.")
        return
    try:
        stock = int(input("Ingrese cantidad de stock: "))
    except ValueError:
        print("Entrada inválida. Ingrese una cantidad válida.")
        return
    
    def Guardar_Productos():
        with open("productos.json", "w") as Archivo:
            json.dump(Productos, Archivo, indent=4)
              
def Cargar_Productos():
    try:
        with open("productos.json", "r") as Archivo:
            return json.load(Archivo)
    except FileNotFoundError:
        return []
        
Productos = Cargar_Productos()

def Obtener_Producto_Por_ID(ID):
    for Producto in Productos:
        if Producto["ID"] == ID:
            return Producto
    return None

    producto = {
    "ID": len(Productos) + 1,
    "Nombre": nombre,
    "Precio": precio,
    "Stock": stock
    }
    Productos.append(producto)
    Guardar_Productos()
   
    print("El producto fue agregado correctamente")
    print("ID asignado:", producto["ID"])

def Ver_Productos():
    if len(Productos) == 0:
        print("No hay productos en el stock")
    else:
        print("============    PRODUCTOS    ============")
        for Producto in Productos:
            print(f"ID: {Producto['ID']}\nNombre: {Producto['Nombre']}\nPrecio: {Producto['Precio']}\nStock: {Producto['Stock']}")
            
def Buscar_Producto():
    try:
        ID_Buscar = int(input("Ingrese el id del producto a buscar: "))
    except ValueError:
        print("ID inválido. Ingrese un número entero.")
        return
    
    producto = Obtener_Producto_Por_ID(ID_Buscar)
    
    if producto is None:
        print("Producto no encontrado")
        return
    print("============    PRODUCTO ENCONTRADO   ============")
    print(f"ID: {producto['ID']}\nNombre: {producto['Nombre']}\nPrecio: {producto['Precio']}\nStock: {producto['Stock']}")

def Agregar_Stock():
    try:
        ID_Agregar = int(input("Ingrese el id del producto al que desea agregar stock: "))
    except ValueError:
        print("ID inválido. Ingrese un número entero.")
        return
    Encontrado = False
    for Producto in Productos:
        if Producto["ID"] == ID_Agregar:
            try:
                Cantidad_Agregar = int(input("Ingrese la cantidad a agregar: "))
            except ValueError:
                print("Cantidad inválida. Ingrese un número entero.")
                return
            Producto["Stock"] += Cantidad_Agregar
            Guardar_Productos()
            print(f"Se agrego {Cantidad_Agregar} unidades al producto {Producto['Nombre']}. Nuevo stock: {Producto['Stock']}")
            Encontrado = True
            break
    if not Encontrado:
        print("Producto no encontrado")
        
def Quitar_Stock():
    try:
        ID_Restar = int(input("Ingrese el id del producto del que desea quitar stock: "))
    except ValueError:
        print("ID inválido. Ingrese un número entero.")
        return
    Encontrado = False
    for Producto in Productos:
        if Producto["ID"] == ID_Restar:
            try:
                Cantidad_Restar = int(input("Ingrese la cantidad a quitar: "))
            except ValueError:
                print("Cantidad inválida. Ingrese un número entero.")
                return
            if Cantidad_Restar <= Producto["Stock"]:
                Producto["Stock"] -= Cantidad_Restar
                Guardar_Productos()
                print(f"Se quitaron {Cantidad_Restar} unidades del producto {Producto['Nombre']}. Nuevo stock: {Producto['Stock']}")
            else:
                print("No hay suficiente stock")
            Encontrado = True
            break
    if not Encontrado:
        print("Producto no encontrado")
        
def Eliminar_Producto():
    try:
        ID_Eliminar = int(input("Ingrese el id del producto que desea eliminar: "))
    except ValueError:
        print("ID inválido. Ingrese un número entero.")
        return
    Encontrado = False
    for Producto in Productos:
        if Producto["ID"] == ID_Eliminar:
            Productos.remove(Producto)
            Guardar_Productos()
            print(f"El producto {Producto['Nombre']} fue eliminado correctamente")
            Encontrado = True
            break
    if not Encontrado:
        print("Producto no encontrado")

while True:
    
    mostrar_menu()
    
    Opcion = input("Elegi una opcion: ")
    print("Elegiste: ", Opcion)
    
    if Opcion == "1":          
        agregar_producto()
        
    elif Opcion == "2":
        Ver_Productos()
        
    elif Opcion == "3":
        Buscar_Producto()
        
    elif Opcion == "4":
        Agregar_Stock()
        
    elif Opcion == "5":
        Quitar_Stock()
        
    elif Opcion == "6":
        Eliminar_Producto()
               
    elif Opcion == "8":
        print("Vamos a salir")
        break
    else:
        print("Esa opcion es invalida")

print("estoy escribiendo código desde el celular")