from persona import*
from animalfinal import*

class cliente(Persona):
    def __init__(self, nombre, apellido, ID, numtel,ubicacion,mascota) -> None:
        super().__init__(nombre, apellido, ID, numtel)
        self.ubicacion=ubicacion
        self.mascota=mascota

    

    def __str__(self) -> str:
        return self.nombre + " "+self.apellido+ " "+"propietario"+" "+"mascota"+" "+str(self.mascota)


class lista():
     def __init__(self, cliente=None):
            if cliente is None:
                self.cliente = []
            else:
                self.cliente = cliente

     def Crear(self, cli):
         self.cliente.append(cli)
        
    

     def print(self):
        for x in range(len(self.cliente)):
            print(self.cliente[x])

cli1=cliente("Yovanni","Amador","0801-2001-05001","88548282","perros",animal2.getnombre())
list1=lista()
list1.Crear(cli1)
cli2=cliente("Raul","Gonzales","0801-2000-23232","99494494","TGU",animal2.getnombre())
list1.Crear(cli2)
list1.print()
