from persona import*
class Veterinario(Persona):
    def __init__(self, nombre, apellido, ID, numtel,especialidad,turno):
        
        super().__init__(nombre, apellido, ID, numtel)
        self.especialidad=especialidad
        self.turno=turno
    def __str__(self):
         return self.nombre+" "+ self.apellido+"  "+self.especialidad+" "+self.turno
    def getnombre(self):
        return self.nombre+" "+self.apellido

class lista():
    def __init__(self,Veterinarios=None):
        if Veterinarios is None:
            self.Veterinarios=[]
        else:
            self.Veterinarios=Veterinarios

    def agregar(self,vet):
        
        self.Veterinarios.append(vet)

    def print(self):
        for x in range(len(self.Veterinarios)):
            print (self.Veterinarios[x])
    
    

Veterinario1=Veterinario("Yovanni", "Amador","0801200105001","99989899","perros","nocturno")
Veterinario2=Veterinario("Leo","MESS","232432432","4325235235","GATOS","DIURNO")
lista1=lista()
lista1.agregar(Veterinario1) 
lista1.agregar(Veterinario2)  

    
    

