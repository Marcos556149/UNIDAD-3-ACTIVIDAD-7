from ClasePersonal import Personal
class Investigador(Personal):
    __areaInvestigacion= ''
    __tipoInvestigacion= ''
    def __init__(self,cu='',ape='',nom='',suel=0,anti=0,carre='',car='',cat='',area='',tipo=''):
        super().__init__(cu,ape,nom,suel,anti,carre,car,cat,area,tipo)
        self.__areaInvestigacion= area
        self.__tipoInvestigacion= tipo
    def __str__(self):
        return 'INVESTIGADOR\nCuil: {},Apellido: {},Nombre: {},SueldoBasico: {},Antiguedad: {}, AreaInv: {}, TipoInv: {}'.format(super().getCuil(),super().getApellido(),super().getNombre(),super().getSueldoBasico(),super().getAntiguedad(),self.__areaInvestigacion,self.__tipoInvestigacion)
    def getSueldo(self):
        basico= self.getSueldoBasico()
        total= basico + ((basico * 0.05)* self.getAntiguedad())
        return total
    def getArea(self):
        return self.__areaInvestigacion
    def getTipo(self):
        return self.__tipoInvestigacion
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cu= super().getCuil(),
                ape= super().getApellido(),
                nom= super().getNombre(),
                suel= super().getSueldoBasico(),
                anti= super().getAntiguedad(),
                area= self.__areaInvestigacion,
                tipo= self.__tipoInvestigacion
                     )
            )
        return d
