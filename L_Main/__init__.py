from _operator import is_not 

class LS:
    def __init__(self, dato = None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
        
class Lineal_LS: 
    def __init__(self):
        self.cabeza = None
        
    def es_vacia(self):
        if self.cabeza==None:
            return None
        else:
            return self.cabeza

    def agregar(self, dato):
        self.cabeza = LS(dato=dato, siguiente=self.cabeza)  
        
    def buscar(self,dato):
        auxiliar = self.cabeza
        ver = 0
        if  self.es_vacia() != None:
            while auxiliar != None:
                if auxiliar.dato==dato:
                    print(f"Se encontro el dato: {dato}")
                    ver= 1
                auxiliar = auxiliar.siguiente
        else:
            print("La lista se encuentra vacia")
        if ver == 0:
            print("No se encontro el dato")
        
        return ver
    
    def modificar(self,dato,nuevo):
        auxiliar = self.cabeza
        if  self.buscar(dato) != 0:
            while auxiliar != None:
                if auxiliar.dato==dato:
                    auxiliar.dato=nuevo
                    print("Dato modificado")
                auxiliar = auxiliar.siguiente
        else:
            print("No se encuentra el dato")
    
    def eliminar(self, dato):
        auxiliar = self.cabeza
        temporal = None
        ver=0
        while auxiliar and auxiliar.dato != dato:
            temporal = auxiliar
            auxiliar = auxiliar.siguiente
        if temporal is None:
            self.cabeza = auxiliar.siguiente
            ver=1
        elif auxiliar:
            temporal.siguiente = auxiliar.siguiente
            auxiliar.siguiente = None
            ver=1
        
        if ver != 0:
            print("Se elimino el dato")
        else:
            print(f"No se encontro el dato {dato}")

    def lista( self ):
        i = self.cabeza
        while i != None:
            if i.siguiente != None:
                print(i.dato, end =" => ")
            else:
                print(i.dato, end =" => NULL")
                print()
            i = i.siguiente


s = Lineal_LS()


def menu():
    for i in range(0,5):
        print("\n")

    print ("Seleccione una opcion")
    print ("\t1 - Insertar")
    print ("\t2 - Modificar")
    print ("\t3 - Eliminar")
    print ("\t4 - Listar")
    print ("\t5 - Salir")

while True:
    menu()
    opcionMenu = input("Opcion: ")
    
    if opcionMenu=="1":
        print ("")
        dato = input("Dato a agregar: ")
        s.agregar(dato)
        input("Se ha agregado exitosamente \npulsa una tecla para continuar")
        
    elif opcionMenu=="2":
        print ("")
        dato = input("Dato a modificar: ")
        nuevo = input("Nuevo dato: ")
        s.modificar(dato, nuevo)
        input("pulsa una tecla para continuar")

    elif opcionMenu=="3":
        print ("")
        dato = input("Dato a eliminar: ")
        s.eliminar(dato)
        input("\npulsa una tecla para continuar")
        
    elif opcionMenu=="4":
        print ("")
        s.lista()
        input("pulsa una tecla para continuar")
        
    elif opcionMenu=="5":
        break
    else:
        print ("")
        input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")

