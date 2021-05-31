from ClasePersonal import Personal
class Apoyo(Personal):
    __categoria= 0
    def __init__(self,cu='',ape='',nom='',suel=0,anti=0,cate=0):
        super().__init__(cu,ape,nom,suel,anti)
        self.__categoria= cate
    def __str__(self):
        return 'PERSONAL APOYO\nCuil: {},Apellido: {},Nombre: {},SueldoBasico: {},Antiguedad: {}, Categoria: {}'.format(super().getCuil(),super().getApellido(),super().getNombre(),super().getSueldoBasico(),super().getAntiguedad(),self.__categoria)
    def getSueldo(self):
        basico= self.getSueldoBasico()
        total= basico + ((basico * 0.05)* self.getAntiguedad())
        if (self.__categoria > 0)and(self.__categoria < 11):
            total += basico * 0.1
        elif (self.__categoria > 10)and(self.__categoria < 21):
            total += basico * 0.2
        elif (self.__categoria == 21)or(self.__categoria == 22):
            total += basico * 0.3
        return total
    def toJSON(self):
        d= dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cu= super().getCuil(),
                ape= super().getApellido(),
                nom= super().getNombre(),
                suel= super().getSueldoBasico(),
                anti= super().getAntiguedad(),
                cate= self.__categoria
                     )
            )
        return d
