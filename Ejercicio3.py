class concesionario():
    marca=""
    color=""
    vin=""
    año=""
    modelo=""
    __capacidad=""
    __tipo= ""
    condicion=""
    precioV=0
    precioC=0
    estado="No registrado"

    def __init__(self):
        self.__capacidad="5 personas"
        self.__tipo="4 ruedas"

    def RegistrarCarro(self):
        self.estado="Registrado"
        return self.estado
    
    #almacena lo del input
    def DatosCarro(self, MarcaCarro, ColorCarro,
                   NumVin, Year, NombreModelo, 
                     CondicionCarro, PrecioCom):
        self.marca=MarcaCarro
        self.color=ColorCarro
        self.vin=NumVin
        self.año=Year
        self.modelo=NombreModelo
        self.condicion=CondicionCarro
        self.precioV=PrecioCom*1.4
        
    
    def PrecioCom(self):
        return self.precioC
    def capacidad(self):
        return self.__capacidad
    def tipo(self):
        return self.__tipo
    
    #funcion que lee los datos
    
    print("----------------------------------------------------")
    def RecibeDatosCarros(self):
        MarcaCarro=input("Marca del Carro:")
        ColorCarro=input("Color del Carro:")
        NumVin=input("VIN:")
        Year=input("Año del Carro:")
        NombreModelo=input("Modelo Carro:")
        CondicionCarro=input("Condición del Carro? (Nuevo/Usado):")
        PrecioCom=float(input("Precio Compra:$"))
        self.DatosCarro(MarcaCarro, ColorCarro,
                   NumVin, Year, NombreModelo, 
                     CondicionCarro, PrecioCom)
        self.RegistrarCarro()
        
        print("----------------------------------------------------")
        print("---------------Global Motors INC--------------------")

    def MuestraDatosCarro(self):
        print("Marca:",self.marca)
        print("Color:", self.color)
        print("VIN:", self.vin)
        print("Año:", self.año)
        print("Modelo:",self.modelo)
        print("Capacidad:",self.__capacidad)
        print("Tipo Automovil:",self.__tipo)
        print("Condición:", self.condicion)
        print("Precio Venta:$",round(self.precioV))
        print("Estado:", self.estado)
        print("---------------------------------------------------")
        print("--------------------2024©--------------------------")

Carro1=concesionario()
print("Información del Carro")
Carro1.RecibeDatosCarros()
Carro1.MuestraDatosCarro()

        







    
