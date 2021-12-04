
class Animal():

    def __init__(self,nombre ,especie, raza, edad, sexo, peso):
        self.nombre=nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.peso = peso

    def __str__(self):
        return "nombre de animal"+self.nombre+"es un"+self.especie+" "+self.raza+" "+self.edad+" "+"anios"+self.sexo+" "+str(self.peso)
    
    def getnombre(self):
        return self.nombre
    


class lista():
    def __init__(self, animal=None):
            if animal is None:
                self.animal = []
            else:
                self.animal = animal

    def Crear(self, anim):
        
        self.animal.append(anim)

    def print(self):
        for x in range(len(self.animal)):
            print(self.animal[x])


animal2 = Animal("Akila","Perro","labrador","2 años","hembra",12)
animal1=Animal("Princesa","Gato","Persa","2 años","hembra",2)
lista1 = lista()

lista1.Crear(animal2)

