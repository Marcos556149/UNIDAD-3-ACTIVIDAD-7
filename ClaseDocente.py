from ClasePersonal import Personal
class Docente(Personal):
    __carrera= ''
    __cargo= ''
    __catedra= ''
    def __init__(self,cu='',ape='',nom='',suel=0,anti=0,carre='',car='',cat='',area='',tipo=''):
        super().__init__(cu,ape,nom,suel,anti,carre,car,cat,area,tipo)
        self.__carrera= carre
        self.__cargo= car
        self.__catedra= cat
    def __str__(self):
        return 'DOCENTE\nCuil: {},Apellido: {},Nombre: {},SueldoBasico: {},Antiguedad: {}, Carrera: {}, Cargo: {}, Catedra: {}'.format(super().getCuil(),super().getApellido(),super().getNombre(),super().getSueldoBasico(),super().getAntiguedad(),self.__carrera,self.__cargo,self.__catedra)
    def getSueldo(self):
        basico= self.getSueldoBasico()
        total= basico + ((basico * 0.05)* self.getAntiguedad())
        if self.__cargo == 'simple':
            total += basico * 0.1
        elif self.__cargo == 'semiexclusivo':
            total += basico * 0.2
        elif self.__cargo == 'exclusivo':
            total += basico * 0.5
        return total
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cu= super().getCuil(),
                ape= super().getApellido(),
                nom= super().getNombre(),
                suel= super().getSueldoBasico(),
                anti= super().getAntiguedad(),
                carre= self.__carrera,
                car= self.__cargo,
                cat= self.__catedra
                     )
            )
        return d
