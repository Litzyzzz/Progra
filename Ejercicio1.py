class veterinaria():
    nombre=""
    edad= 0
    sexo=""
    raza=""
    peso=0
    tamaño=""
    esterilización=""
    estado="NO ATENDIDO"
#hika
    def RegistroPerro(self):
        self.estado= "ATENDIDO"
        return self.estado
    
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
    
    def RecibeDatosPerro(self):

        print("****************************************")
        nombreP=input("Nombre del perro:")
        edadP=int(input("Edad del perro en años:"))
        sexoP=input("Sexo del perro:")
        razaP=input("Raza del perro:")
        pesoP= float(input("Peso en kg:"))
        estP=input("Esterización (S/N):")
        
        print("****************************************")
        self.DatosPerro(nombreP,edadP,sexoP,razaP,pesoP,estP)
        self.RegistroPerro()

    def MuestraDatosPerro(self):
        print("Nombre=",self.nombre)
        print(f"Edad={self.edad} años")
        print("Sexo=",self.sexo)
        print("Raza=", self.raza)
        print(f"Peso= {self.peso} kg")
        print("Tamaño=", self.tamaño)
        print("Esterelizado/a=", self.esterilización)
        print("Estado=", self.estado)

perro1=veterinaria()
print("DATOS DEL PERRO")
perro1.RecibeDatosPerro()
perro1.MuestraDatosPerro()







    
