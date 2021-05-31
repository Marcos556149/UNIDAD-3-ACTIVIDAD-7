from ClaseInvestigador import Investigador
from ClaseDocente import Docente
class DocenteInvestigador(Investigador, Docente):
    __categoriaIncentivos= ''
    __importeExtra= 0
    def __init__(self,cu='',ape='',nom='',suel=0,anti=0,carre='',car='',cat='',area='',tipo='',catInc='',imp=0):
        super().__init__(cu,ape,nom,suel,anti,carre,car,cat,area,tipo)
        self.__categoriaIncentivos= catInc
        self.__importeExtra= imp
    def __str__(self):
        return 'DOCENTE INVESTIGADOR\nCuil: {},Apellido: {},Nombre: {},SueldoBasico: {},Antiguedad: {}, Carrera: {}, Cargo: {}, Catedra: {}, AreaInv: {}, TipoInv: {}, CategoriaInc: {}, ImporteExtra: {}'.format(super().getCuil(),super().getApellido(),super().getNombre(),super().getSueldoBasico(),super().getAntiguedad(),super().getCarrera(),super().getCargo(),super().getCatedra(),super().getArea(),super().getTipo(),self.__categoriaIncentivos,self.__importeExtra)
    def getSueldo(self):
        total= Docente.getSueldo(self) + self.__importeExtra
        return total
    def getCategInc(self):
        return self.__categoriaIncentivos
    def getImporteExtra(self):
        return self.__importeExtra
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cu= super().getCuil(),
                ape= super().getApellido(),
                nom= super().getNombre(),
                suel= super().getSueldoBasico(),
                anti= super().getAntiguedad(),
                carre= super().getCarrera(),
                car= super().getCargo(),
                cat= super().getCatedra(),
                area= super().getArea(),
                tipo= super().getTipo(),
                catInc= self.__categoriaIncentivos,
                imp= self.__importeExtra,
                      )
            )
        return d
    def __gt__(self,otro):
        return self.getNombre() > otro.getNombre()
