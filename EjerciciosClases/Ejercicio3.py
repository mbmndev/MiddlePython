#3. Dada la siguiente lista de productos. 
#
 #  ```
  # productos_lista = [
   #    {"nombre": "Leche", "precio": 2.50, "stock": 10},
    #   {"nombre": "Huevos", "precio": 1.50, "stock": 20},
     #  {"nombre": "Pan", "precio": 1.00, "stock": 15}
   #]
   #```

#   Crear un clase que represente los elementos de la lista, 
#con la clase crear objetos que rellenen una lista de productos.

class ListaProductos:


    def __init__(self,productos_lista=[],objeto={}):
        self.Productos_Lista=productos_lista

        self.Objeto=objeto

    def crearObjeto(self,objeto):
        self.Objeto=objeto
        self.Productos_Lista.append(self.Objeto)

    def mostrarProductos(self):
        for productos in self.Productos_Lista:
            print(productos)



productos_lista = [
       {"nombre": "Leche", "precio": 2.50, "stock": 10},
       {"nombre": "Huevos", "precio": 1.50, "stock": 20},
       {"nombre": "Pan", "precio": 1.00, "stock": 15}
   ]

objeto={"nombre": "", "precio": 0, "stock": 0}

nombre=""
precio=0
stock=0

listaProductos=ListaProductos(productos_lista,objeto)

while True:
    nombre=input("Ingrese el nombre del producto: ".capitalize())
    if(nombre.isalpha()):
        precio=input("Introduzca el precio del producto :")
        if precio.isdigit():
            precioInt=int(precio)
            stock=input("Introduzca el stock del producto :")
            if stock.isdigit():
                stockInt=int(stock)
                objeto["nombre"]=nombre
                objeto["precio"]=precioInt
                objeto["stock"]=stockInt

                listaProductos.crearObjeto(objeto)

                continuar=input("Escriba s si desea introducir otro producto:")
                if continuar!="s" or continuar!="S":
                    break
                continue
            else: print("Error al introducir el stock")
        else: print("Error al introducir el precio")
    else: print("Error al introducir el nombre")


listaProductos.mostrarProductos()
