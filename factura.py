from Medicamentos import *

class factura:

    def __init__(self,gastos_medicamentos,gastos_vet,nombremedicamento,ISV=0,metodos_pago=0,total=0):
         self.gastos_medicamentos= gastos_medicamentos
         self.gastos_vet= gastos_vet
         self.nombremedicamento=nombremedicamento
         
         
        
    def __str__(self):
        return "medicamento comprado"+self.nombremedicamento+"subtotal"+str(self.gastos_medicamentos+self.gastos_vet)+"ISV lempiras"+str(self.ISV)+" total  L."+''+str(self.total)+"fue pagado en "+" "+self.metodos_pago 
 
    
    def total_factura(self):               
        self.total=self.gastos_medicamentos+self.gastos_vet+self.ISV


    def forma_pago(self):
        sel= input("Ingrese su metodo de pago\n a-> Efectivo\n b-> Tarjeta\n")    
        if sel=='a':
            print("Su metodo de pago es EFECTIVO")
            self.metodos_pago=" Efectivo"   
        else:
          print("su metodo de pago es TARJETA")
          self.metodos_pago="Tarjeta"

    def imp_vent(self):
        self.ISV=(self.gastos_medicamentos+self.gastos_vet)*(0.15)
        print(self.ISV)

class lista():
     def __init__(self, factura=None):
            if factura is None:
                self.factura = []
            else:
                self.factura= factura

     def Crear(self, fac):
         self.factura.append(fac)
        
    

     def print(self):
        for x in range(len(self.factura)):
            print(self.factura[x])


factura1=factura(Medicamento1.getprecio(),524,Medicamento1.getnombre())
factura1.forma_pago()
factura1.imp_vent()
factura1.total_factura()
#print(factura1)
lista1fac=lista()
lista1fac.Crear(factura1)
lista1fac.print()





