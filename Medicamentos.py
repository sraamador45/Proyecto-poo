
class Medicamentos:
    def __init__(self, nom_med, codigo, dosis,fecha_elab,fecha_ven,precio):
        self.nom_med = nom_med
        self.codigo = codigo
        self.dosis = dosis
        self.fecha_elab= fecha_elab
        self.fecha_ven= fecha_ven
        self.precio = precio 

    def __str__(self):
        return self.nom_med+" "+self.codigo+" "+self.dosis+" "+self.fecha_elab+" "+self.fecha_ven+" "+self.precio
    def getprecio(self):
        return self.precio
    def getnombre(self):
        return self.nom_med+" "+self.dosis

        

class lista():
    def __init__(self,Medicamentos=None):
        if Medicamentos is None:
            self.Medicamentos=[]
        else:
            self.Medicamentos=Medicamentos

    def agregar(self,med):
        print('añadido el med',(med))
        self.Medicamentos.append(med)

    def print(self):
        for x in range(len(self.Medicamentos)):
            print(self.Medicamentos[x])

Medicamento1= Medicamentos("Panadol", "007", "10 tabletas", "2/FEB/2018", "2/FEB/2022",500)





