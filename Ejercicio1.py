#Clase principal
class veterinaria():
    nombre=""
    edad= 0
    sexo=""
    raza=""
    peso=0
    tamaño=""
    esterilización=""
    estado="NO ATENDIDO"
    #funcion para actualizar el estado del registro
    def RegistroPerro(self):
        self.estado= "ATENDIDO"
        return self.estado
    #funcion que almacena los datos en las variables
    print("****************************************")
    def DatosPerro(self, nombreP,edadP, sexoP,
                   razaP,pesoP,estP):
        self.nombre=nombreP
        self.edad=edadP
        self.sexo=sexoP
        self.raza=razaP
        self.peso=pesoP
        self.esterilización=estP
        if (pesoP <= 10):
            self.tamaño= "Perro Pequeño"
        else:
            self.tamaño= "Perro Grande"
    

        
    #funcion que captura lo que ingresa el usuario
    def RecibeDatosPerro(self):
        print("****************************************")
        nombreP=input("Nombre del perro: ")
        edadP=int(input("Edad del perro en años: "))
        sexoP=input("Sexo del perro: ")
        razaP=input("Raza del perro: ")
        pesoP= float(input("Peso en kg: "))
        estP=input("Esterización (S/N): ")
        
        self.DatosPerro(nombreP,edadP,sexoP,razaP,pesoP,estP)
        self.RegistroPerro()

        
        #funcion que contiene los datos registrados para presentar
    def MuestraDatosPerro(self):
        print("*****************DOCTORpet**********************")
        print("Nombre: ",self.nombre)
        print(f"Edad: {self.edad} años")
        print("Sexo: ",self.sexo)
        print("Raza: ", self.raza)
        print(f"Peso: {self.peso} kg")
        print("Tamaño: ", self.tamaño)
        print("Esterelizado/a: ", self.esterilización)
        print("Estado: ", self.estado)
        print("*******************2024©***********************")
        
#objeto
perro1=veterinaria()
print("DATOS DEL PERRO")
#el metodo recibe al objeto y es ejecutado sobre los datos recibidos
perro1.RecibeDatosPerro()

# el metodo muestra los datos del objeto que capturó 
perro1.MuestraDatosPerro()







    
