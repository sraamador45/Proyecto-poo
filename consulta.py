from Medicamentos import *
from cliente import*
from datetime import datetime
from Veterinario import*
class Consulta():
    def __init__(self,vetencar,cliente,medicamentos,animal,diagnostico=0,motivo=0,fechaconsulta=0) -> None:
        self.vetencar=vetencar
        self.cliente=cliente
        self.medicamentos=medicamentos

        
        self.animal=animal
        

    def __str__(self) -> str:
        return "-------------------------------\n" +"\nVeterinaria La Mascota fecha de emision"+" "+self.fechaconsulta +" \nVeterinario en turno :"+" "+self.vetencar+"\ncliente:"+" "+self.cliente+"\nPaciente:"+" "+self.animal+"\nMotivo de consulta :"+" "+self.motivo+"\nDiagnostico paciente :"+" "+self.diagnostico +"\nReceta medica "+" "+self.medicamentos

    def motivocon(self):
        sel= input("Ingrese motivo de consulta del paciente") 
        self.motivo=sel

    def diagnosticocon(self):
        inp=input("Diagnostico paciente")
        self.diagnostico=inp
    
    def fechafactura(self):
        now = datetime.now() # current date and time

        year = now.strftime("%Y")
        #print("year:", year)

        month = now.strftime("%m")
        #print("month:", month)

        day = now.strftime("%d")
       # print("day:", day)

        time = now.strftime("%H:%M:%S")
       # print("time:", time)

        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        self.fechaconsulta=date_time


class lista():
     def __init__(self, consulta=None):
            if consulta is None:
                self.consulta = []
            else:
                self.consulta = consulta

     def Crear(self, con):
         self.consulta.append(con)
        
    

     def print(self):
        for x in range(len(self.consulta)):
            print(self.consulta[x])

consulta1=Consulta(Veterinario1.getnombre(),cli2.getnombre(),Medicamento1.getnombre(),cli2.getmascota())
consulta1.fechafactura()
consulta1.motivocon()
consulta1.diagnosticocon()
print(consulta1)




    

        
    
