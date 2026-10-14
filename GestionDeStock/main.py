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

while True:
    
    mostrar_menu()
    
    Opcion = input("Elegi una opcion: ")
    print("Elegiste: ", Opcion)
    
    if Opcion == "1":
        print("Vamos a agregar un producto")
        Nombre = input("Ingrese nombre del producto: ")
        try:
            Precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("Precio inválido. Ingrese un número.")
            continue
        try:
            Cantidad = int(input("Ingrese la cantidad de stock: "))
        except ValueError:
            print("Cantidad inválida. Ingrese un número entero.")
            continue
        Producto = {"Nombre" : Nombre, "Precio" : Precio, "Stock" : Cantidad, "ID" : len(Productos) + 1}
        Productos.append(Producto)
        Guardar_Productos()
        print("El producto fue agreagado correctamente")    
    elif Opcion == "2":
        if len(Productos) == 0:
            print("No hay productos en el stock")
        else:
            print("============    PRODUCTOS    ============")
        for Producto in Productos:
            print(f"ID: {Producto['ID']}\nNombre: {Producto['Nombre']}\nPrecio: {Producto['Precio']}\nStock: {Producto['Stock']}")
    elif Opcion == "3":
        try:
            ID_Buscar = int(input("Ingrese el id del producto a buscar: "))
        except ValueError:
            print("ID inválido. Ingrese un número entero.")
            continue
        Encontrado = False
        for Producto in Productos:
            if Producto["ID"] == ID_Buscar:
                print(f"ID: {Producto['ID']}\nNombre: {Producto['Nombre']}\nPrecio: {Producto['Precio']}\nStock: {Producto['Stock']}")
                Encontrado = True
                print("============    PRODUCTO ENCONTRADO   ============")
                break
        if not Encontrado:
            print("Producto no encontrado")
    elif Opcion == "4":
        try:
            ID_Agregar = int(input("Ingrese el id del producto al que desea agregar stock: "))
        except ValueError:
            print("ID inválido. Ingrese un número entero.")
            continue
        Encontrado = False
        for Producto in Productos:
            if Producto["ID"] == ID_Agregar:
                
                try:
                    Cantidad_Agregar = int(input("Ingrese la cantidad a agregar: "))
                except ValueError:
                    print("Cantidad inválida. Ingrese un número entero.")
                    continue
                Producto["Stock"] += Cantidad_Agregar
                Guardar_Productos()
                print(f"Se agrego {Cantidad_Agregar} unidades al producto {Producto['Nombre']}. Nuevo stock: {Producto['Stock']}")
                Encontrado = True
                break
        if not Encontrado:
            print("Producto no encontrado")
    elif Opcion == "5":
        try:
            ID_Restar = int(input("Ingrese el id del producto del que desea quitar stock: "))
        except ValueError:
            print("ID inválido. Ingrese un número entero.")
            continue
        Encontrado = False
        for Producto in Productos:
            if Producto["ID"] == ID_Restar:
                try:
                    Cantidad_Restar = int(input("Ingrese la cantidad a quitar: "))
                except ValueError:
                    print("Cantidad inválida. Ingrese un número entero.")
                    continue
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
    elif Opcion == "7":
        try:
            ID_Eliminar = int(input("Ingrese el id del producto que desea eliminar: "))
        except ValueError:
            print("ID inválido. Ingrese un número entero.")
            continue
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
               
    elif Opcion == "8":
        print("Vamos a salir")
        break
    else:
        print("Esa opcion es invalida")

print("estoy escribiendo código desde el celular")