#Clase principal
class libreria():
      TipoArticulo=""
      NumHojas=""
      TipoLapices=""
      PrecioVenCuaderno=0
      PrecioVenLap=0
      PrecioComCuaderno=0
      PrecioComLap=0

      #constructor
      def __init__(self):
        self.__MarcaCuaderno="HOJITAS"
        self.__MarcaLapices="RAYAS"
        
      #funcion para registrar el item seleccionado
      def RegistrarArticulo(self):
            self.TipoArticulo=input("Tipo de Artículo (Cuaderno/Lapices): ").lower()
            if self.TipoArticulo.lower()=="cuaderno":
               self.TipoArticulo="Cuaderno"
               self.NumHojas= int (input("Número de hojas (50/100): ")) 
               self.PrecioComCuaderno=float(input("Precio de Compra:$ "))
               self.PrecioVenCuaderno= self.PrecioComCuaderno*1.30
            elif self.TipoArticulo=="lapices":
                 self.TipoArticulo="Lapices"
                 self.TipoLapices=input("Tipo de lápices (Grafito/Colores): ")
                 self.PrecioComLap= float(input("Precio de Compra:$ "))
                 self.PrecioVenLap= self.PrecioComLap*1.30
            else:
             print("Articulo no encontrado")
             self.RegistrarArticulo()
             return
            
            print("------------------------------------------------------------") 
            print("---------------Papelería Y Librería La Fe--------------------")

       #funcion que muestra los detalles del item     
      def MostrarArticulo(self):
         if self.TipoArticulo=="Cuaderno":
            print("Articulo:",self.TipoArticulo)
            print("Marca:",self.__MarcaCuaderno)
            print("Número de Hojas:", self.NumHojas)
            print("Precio de Compra:$ ", self.PrecioComCuaderno)
            print("Precio de Venta:$ ", float(self.PrecioVenCuaderno))
         elif self.TipoArticulo=="Lapices":
            print("Articulo:",self.TipoArticulo)
            print("Marca:",self.__MarcaLapices)
            print("Tipo de lápices:", self.TipoLapices)
            print("Precio de Compra:$ ",self.PrecioComLap)
            print("Precio de Venta:$ ", float(self.PrecioVenLap))
            print("----------------------------------------------------------")
            print("-----------------------2024©------------------------------")

#objeto
Papeleria=libreria()
print("Registrar primer item:")
#Metodo para capturar los datos puestos en la funcion y presentarla
Papeleria.RegistrarArticulo()
#Metodo para mostrar los datos finales obtenidos del objeto
Papeleria.MostrarArticulo()

#segundo item para registrar
print("Registrar segundo item:")
Papeleria.RegistrarArticulo()
Papeleria.MostrarArticulo()











        
        




