import re
class claseViajeroFrecuente():
    __num = 0
    __dni = ''
    __nom = ''
    __ape = ''
    __millasAcum = 0.0
    def __init__(self, num, dni, nom, ape, millas):
        self.__num = num
        self.__dni = dni
        self.__nom = nom
        self.__ape = ape
        self.__millasAcum = millas
    def getNum(self):
        return self.__num
    def cantidadTotaldeMillas(self):
        return self.__millasAcum
    def acumularMillas(self, millas):
        self.__millasAcum += millas
    def canjearMillas(self, millas):
        if(millas <= self.__millasAcum):
            self.__millasAcum-=millas
        else:
            print('ERROR: operación incorrecta')
        return self.__millasAcum