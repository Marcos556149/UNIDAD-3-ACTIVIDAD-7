from ClasePersonal import Personal
from ClaseListaPersonal import ListaPersonal
from ClaseObjectEndoder import ObjectEndoder
if __name__=='__main__':
    jsonF= ObjectEndoder()
    d= jsonF.leerJSONArchivo('personal.json')
    personal= jsonF.decodificarDiccionario(d)
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Insertar a agentes a la colección")
        print("[2]...Agregar agentes a la colección")
        print("[3]...Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición")
        print("[4]...Listado de agentes que se desempeñan como docentes investigadores")
        print("[5]...Contar la cantidad de agentes que son docente investigador, y la cantidad de investigadores que trabajen en un area")
        print("[6]...Generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido")
        print("[7]...Listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen una categoría")
        print("[8]...Almacenar los datos de todos los agentes en el archivo “personal.json”")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(9):
                if op == 1:
                    nuevoPersonal= personal.crearPersonal()
                    if isinstance(nuevoPersonal,Personal):
                        posicion1= int(input("Ingrese la posicion en la que desea insertar el agente: "))
                        personal.insertarElemento(posicion1,nuevoPersonal)
                if op == 2:
                    nuevoPersonal1= personal.crearPersonal()
                    if isinstance(nuevoPersonal1,Personal):
                        personal.agregarElemento(nuevoPersonal1)
                if op == 3:
                    posicion2= int(input('Ingrese la posicion de la lista: '))
                    personal.mostrarElemento(posicion2)
                if op == 4:
                    personal.listadoDocInv()
                if op == 5:
                    personal.ContDocInvYInv()
                if op == 6:
                    personal.listadoGeneral()
                if op == 7:
                    personal.listarPorCategoria()
                if op == 8:
                    d= personal.toJSON()
                    jsonF.guardarJSONArchivo(d,'personal.json')
                if op == 0:
                    print("_____MENU FINALIZADO_____")
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 0 al 8")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
