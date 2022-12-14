opcion=100


print("Super Mercado")
print("**************************\n")

print("1. Nombre del producto")
print("2. Todos los productos registrados")
print("3. Ingresa un nuevo producto")
print("4. Para eliminar ultimo producto")
print("0. SALIR")


Productos=[]
while opcion != 0:
    opcion=int(input("digita una opcion: "))
    if opcion ==1:
        Producto=input("registre el nombre del producto a registrar: ")
        Productos.append(Producto)
    elif opcion ==2:
        for producto in Productos:
            print(f"los productos registrados son :{producto}")
    elif opcion ==3:
            Producto=input("registre el nombre del producto a registrar: ")
            Productos.append(Producto)
    elif opcion ==4:
            Productos.pop()
            
    elif opcion ==0:
        break
    else:
        print("Apreciado usuario, debe seleccionar una opcion valida...")