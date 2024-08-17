
"""El programa gestiona el registro y seguimiento de pacientes. 
El sistema debe permite almacenar los datos personales de cada paciente, 
como su nombre, edad, motivo de consulta, y tiempo de estadía
si es caso de ingreso. Además calcula si se aplica un cobro adicional 
en función del tiempo que el paciente generó por su motivo de ingreso."""

class Clinica():#clase principal
    Nombre=""
    Edad=""
    Telefono=""
    Motivo=""
    Estadia=0
    __CobroxNoche=0
    PrecioTotal=0
    Estado="No Registrado"
    
    #constructor
    def __init__(self):
        self.__CobroxNoche=50
    def CobroEstadia(self):
        return self.__CobroxNoche
    def RegistroPaciente(self):
        self.Estado="Registrado"
        return self.Estado
    #funcion que permite almacenar los datos del paciente en variables
    def DatosPacientes(self, NomP, EdadP,Tel ,MotP,Tiempo):
        self.Nombre=NomP
        self.Edad=EdadP
        self.Telefono=Tel
        self.Motivo=MotP
        self.Estadia=Tiempo
        self.PrecioTotal=Tiempo*self.__CobroxNoche
        self.RegistroPaciente()
    #funcion que lee los datos y se los pasa a la funcion DatosPacientes
    def RecibeDatosP(self):
        MotP=input("Motivo (Cita/Consulta/Ingreso): ").lower()
        if MotP.lower()=="cita":
            MotP="Cita"
            NomP=input("Nombre Completo: ")
            EdadP=int(input("Edad: "))
            Tel=int(input("Teléfono: "))
            self.DatosPacientes(NomP, EdadP,Tel ,MotP,0)
            
        elif MotP.lower()=="consulta":
            MotP="Consulta"
            NomP=input("Nombre Completo: ")
            EdadP=int(input("Edad: "))
            Tel=int(input("Teléfono: "))
            self.DatosPacientes(NomP, EdadP,Tel ,MotP,0)

        elif MotP.lower()=="ingreso":
            MotP="Ingreso"
            NomP=input("Nombre Completo: ")
            EdadP=int(input("Edad: "))
            Tel=int(input("Teléfono: "))
            Tiempo=int(input("Noches: "))
            self.DatosPacientes(NomP, EdadP,Tel ,MotP,Tiempo)
        else:
            print("No hay seguimiento")
        print("----------------------------------------------")
    #funcion que muestra los datos regitrados del paciente
    def MuestraDatosPaciente(self):
        print("Motivo: ", self.Motivo)
        print("Nombre de Paciente: ", self.Nombre)
        print(f"Edad: {self.Edad} años" )
        print("Teléfono de Paciente: ", self.Telefono)
        print(f"Estadia: {self.Estadia} días")
        if self.Motivo=="Ingreso":
            print("Cobro por noche:$ ", int(self.__CobroxNoche))
        print("Cobro Total:$ ", self.PrecioTotal)
        print("Estado: ", self.Estado)
        print("----------------------------------------------")
#objeto que representa la paciente
Paciente1=Clinica()
print("---------------DATOS--------------------------")
Paciente1.RecibeDatosP()
Paciente1.MuestraDatosPaciente()
        
    
        


    
        
    


