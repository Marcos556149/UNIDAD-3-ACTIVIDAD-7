class Personal:
    __cuil= ''
    __apellido= ''
    __nombre= ''
    __sueldoBasico= 0
    __antiguedad= 0
    def __init__(self,cu='',ape='',nom='',suel=0,anti=0,area='',tipo='',carre='',car='',cat=''):
        self.__cuil= cu
        self.__apellido= ape
        self.__nombre= nom
        self.__sueldoBasico= suel
        self.__antiguedad= anti
    def toJSON(self):
        pass
    def getSueldo(self):
        pass
    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldoBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def __gt__(self,otro):
        return self.__apellido > otro.getApellido()
