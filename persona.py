
class Persona :
    def __init__(self,nombre,apellido,ID,numtel) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self.ID=ID
        self.numtel=numtel

    def print(self):
        return'{} {} {} {}'.format(self.nombre,self.apellido,self.ID,self.numtel)

