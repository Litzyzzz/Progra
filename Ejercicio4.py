#Clase principal
class dispositivos(): 

    DispositivoElectronico=""
    __marca=""
    Modelo=""
    Color=""
    SistemaOp=""
    Capacidad=""
    Año=""
    Ram=""
    PrecioVent=0
    __PrecioCom=0
    
    #Constructor
    def __init__(self):
        self.__marca="PHR"
        
        #Funcion para obtener los datos que el usuario ingresa
    def DatosDispositivo(self):
        self.DispositivoElectronico=input("Tipo de dispositivo (Celular/Tablet/Portatil): ").lower()
        if self.DispositivoElectronico.lower()=="celular":
            self.DispositivoElectronico="Celular"
            self.Modelo=input("Modelo del Cecular: ")
            self.Color=input("Color del Celular: ")
            self.SistemaOp=input("Sistema Operativo: ")
            self.Capacidad=input("Almacenamiento: ")
            self.Ram=input("RAM: ")
            self.Año=input("Año de lanzamiento: ")
            self.__PrecioCom=float(input("Precio Compra: "))
        elif self.DispositivoElectronico=="tablet":
            self.DispositivoElectronico="Tablet"
            self.Modelo=input("Modelo de la Tablet: ")
            self.Color=input("Color de la Tablet: ")
            self.SistemaOp=input("Sistema Operativo: ")
            self.Capacidad=input("Almacenamiento: ")
            self.Ram=input("RAM: ")
            self.Año=input("Año de lanzamiento: ")
            self.__PrecioCom=float(input("Precio Compra: "))

        elif self.DispositivoElectronico=="portatil":
            self.DispositivoElectronico="Portatil"
            self.Modelo=input("Modelo del Portatil: ")
            self.Color=input("Color del Portatil: ")
            self.SistemaOp=input("Sistema Operativo: ")
            self.Capacidad=input("Almacenamiento: ")
            self.Ram=input("RAM: ")
            self.Año=input("Año de lanzamiento: ")
            self.__PrecioCom=float(input("Precio Compra: "))
        else:
            print("Dispositivo no disponible")
          

     #funcion en donde se hace la operacion matematica del Precio Venta
    def PVenta(self):
        self.PrecioVent= self.__PrecioCom*1.7

        
    print("--------------------------REGISTRO------------------------------")
    #funcion que muestra los datos registrados    
    def MostrarDispositivo(self):
        print("--------------------ALMACEN PCWARE---------------------------")
        if self.DispositivoElectronico in ["Celular", "Tablet", "Portatil"]:
            print("Dispositivo: ", self.DispositivoElectronico)
            print("Marca: ", self.__marca)
            print("Modelo: ", self.Modelo)
            print("Color: ", self.Color)
            print("SO: ", self.SistemaOp)
            print("Almacenamiento: ", self.Capacidad)
            print("Memoria RAM: ", self.Ram)
            print("Año: ", self.Año)
            print("Precio Compra: ", self.__PrecioCom)
            self.PVenta()
            print("Precio Venta: ", self.PrecioVent)
            print("-----------------------2024©---------------------------")
#Objeto que nos permite representar el dispositivo a registrar
Dispositivo1=dispositivos()
#Metodo para capturar los datos puestos en la funcion y presentarla
Dispositivo1.DatosDispositivo()
print("Información del Articulo")
#Metodo para mostrar los datos finales obtenidos del objeto
Dispositivo1.MostrarDispositivo()            

            


