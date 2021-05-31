from zope.interface import implementer
from ClasePersonal import Personal
from ClaseApoyo import Apoyo
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseNodo import Nodo
from InterfazControlador import IControlador
@implementer(IControlador)
class ListaPersonal:
    __comienzo= None
    __actual= None
    __indice= 0
    __tope= 0
    def __init__(self):
        self.__comienzo= None
        self.__actual= None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual= self.__comienzo
            self.__indice= 0
            raise StopIteration
        else:
            self.__indice += 1
            dato= self.__actual.getPersonal()
            self.__actual= self.__actual.getSiguiente()
            return dato
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            personal=[Personal.toJSON() for Personal in self]
            )
        return d
    def crearPersonal(self):
        tipo= int(input('Ingrese el tipo de agente que desea agregar a la coleccion, 1- Docente,2- Investigador,3- Apoyo,4- Docente Investigador: '))
        if tipo == 1:
            cu= input("Ingrese el cuil: ")
            ape= input('Ingrese el apellido: ')
            nom= input('Ingrese el nombre: ')
            suel= int(input('Ingrese el sueldo: '))
            anti= int(input('Ingrese la antiguedad: '))
            carre= input('Ingrese carrera en la que dicta clases: ')
            car= input('Ingrese el cargo del docente: ')
            cat= input('Ingrese la catedra: ')
            nuevoDocente= Docente(cu,ape,nom,suel,anti,carre,car,cat)
            return nuevoDocente
        elif tipo == 2:
            cu= input("Ingrese el cuil: ")
            ape= input('Ingrese el apellido: ')
            nom= input('Ingrese el nombre: ')
            suel= int(input('Ingrese el sueldo: '))
            anti= int(input('Ingrese la antiguedad: '))
            area= input('Ingrese el area de investigacion: ')
            tipo= input('Ingrese el tipo de investigacion: ')
            nuevoInvestigador= Investigador(cu,ape,nom,suel,anti,'','','',area,tipo)
            return nuevoInvestigador
        elif tipo == 3:
            cu= input("Ingrese el cuil: ")
            ape= input('Ingrese el apellido: ')
            nom= input('Ingrese el nombre: ')
            suel= int(input('Ingrese el sueldo: '))
            anti= int(input('Ingrese la antiguedad: '))
            cate= int(input('Ingrese la categoria del personal de apoyo: '))
            nuevoApoyo= Apoyo(cu,ape,nom,suel,anti,cate)
            return nuevoApoyo
        elif tipo == 4:
            cu= input("Ingrese el cuil: ")
            ape= input('Ingrese el apellido: ')
            nom= input('Ingrese el nombre: ')
            suel= int(input('Ingrese el sueldo: '))
            anti= int(input('Ingrese la antiguedad: '))
            carre= input('Ingrese carrera en la que dicta clases: ')
            car= input('Ingrese el cargo: ')
            cat= input('Ingrese la catedra: ')
            area= input('Ingrese el area de investigacion: ')
            tipo= input('Ingrese el tipo de investigacion: ')
            catInc= int(input('Ingrese la categoria en el programa de incentivos: '))
            imp= int(input('Ingrese el importe extra por docencia e investigacion: '))
            nuevoDocenteInvestigador= DocenteInvestigador(cu,ape,nom,suel,anti,carre,car,cat,area,tipo,catInc,imp)
            return nuevoDocenteInvestigador
        else:
            print("ERROR, tipo de agente incorrecto")
            return 1
    def insertarElemento(self,posicion1,elemento1):
        try:
            if posicion1 > 0:
                i= 1
                nuevo= Nodo(elemento1)
                anterior= None
                p= self.__comienzo
                if posicion1 == 1:
                    nuevo.setSiguiente(self.__comienzo)
                    self.__comienzo= nuevo
                    self.__tope += 1
                    self.__actual= self.__comienzo
                else:
                    while (p != None)and(i < posicion1):
                        anterior= p
                        p= p.getSiguiente()
                        i += 1
                    if p == None:
                        i = i/0
                    anterior.setSiguiente(nuevo)
                    nuevo.setSiguiente(p)
                    self.__tope += 1
                    print("AGENTE INSERTADO CON EXITO EN LA COLECCION")
            else:
                print("ERROR, La posicion debe ser de 1 en adelante")
        except ZeroDivisionError:
            print("ERROR, La posicion no es valida")
    def agregarElemento(self,elemento2):
        p= None
        nuevo= Nodo(elemento2)
        anterior= None
        if self.__comienzo == None:
            self.__comienzo= nuevo
            self.__tope += 1
            self.__actual= self.__comienzo
        else:
            p= self.__comienzo
            while p != None:
                anterior= p
                p= p.getSiguiente()
            anterior.setSiguiente(nuevo)
            self.__tope += 1
    def mostrarElemento(self,posicion2):
        try:
            if posicion2 > 0:
                i= 1
                aux= self.__comienzo
                while (aux != None)and(i < posicion2):
                    aux = aux.getSiguiente()
                    i += 1
                print("El tipo de agente almacenado en la posicion {} de la coleccion es: {}".format(posicion2,aux.getPersonal().__class__.__name__))
            else:
                print("ERROR, La posicion debe ser de 1 en adelante")
        except AttributeError:
            print("ERROR, La posicion no es valida")
    def listadoDocInv(self):
        carr= input("Ingrese el nombre de la carrera: ")
        aux= self.__comienzo
        listaDOCINV= []
        while (aux != None):
            if isinstance(aux.getPersonal(),DocenteInvestigador)and(carr.lower() == aux.getPersonal().getCarrera().lower()):
                listaDOCINV.append(aux.getPersonal())
            aux= aux.getSiguiente()
        if len(listaDOCINV) == 0:
            print("No se encontro ningun Docente Investigador cuya carrera es {}".format(carr))
        else:
            listaDOCINV.sort()
            for i in range(len(listaDOCINV)):
                print(listaDOCINV[i])
    def ContDocInvYInv(self):
        areaa= input("Ingrese el area de investigacion: ")
        cont1= 0
        cont2= 0
        aux= self.__comienzo
        while(aux != None):
            if isinstance(aux.getPersonal(),Investigador)and(areaa.lower() == aux.getPersonal().getArea().lower()):
                cont1 += 1
                if isinstance(aux.getPersonal(),DocenteInvestigador):
                    cont2 += 1
            aux= aux.getSiguiente()
        print("La cantidad de agentes Investigadores que trabajan en el area {} son: {}".format(areaa,cont1))
        print("La cantidad de agentes Docentes Investigadores que trabajan en el area {} son: {}".format(areaa,cont2))
    def listadoGeneral(self):
        aux= []
        print("NOMBRE Y APELLIDO      TIPO DE AGENTE          SUELDO")
        for dato in self:
            aux.append(dato)
        aux.sort()
        for i in range(len(aux)):
            print("{}{}{}".format((aux[i].getNombre()+' '+aux[i].getApellido()).ljust(23),(aux[i].__class__.__name__).ljust(24),aux[i].getSueldo()))
    def listarPorCategoria(self):
        cont= 0
        cat= input("Ingrese la categoria, pueden ser I,II,III,IV o V: ")
        aux= self.__comienzo
        if (cat == 'I')or(cat == 'II')or(cat == 'III')or(cat == 'IV')or(cat == 'V'):
            while (aux != None):
                if isinstance(aux.getPersonal(),DocenteInvestigador)and(cat == aux.getPersonal().getCategInc()):
                    print("Apellido: {}, Nombre: {}, Importe Extra: {}".format(aux.getPersonal().getApellido(),aux.getPersonal().getNombre(),aux.getPersonal().getImporteExtra()))
                    cont += aux.getPersonal().getImporteExtra()
                aux= aux.getSiguiente()
            print("Importe extra que cobran los Docentes Investigadores de la categoria {}: {}".format(cat,cont))
        else:
            print("La categoria que ingreso es incorrecta")
