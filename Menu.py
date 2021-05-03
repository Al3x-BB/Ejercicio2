from Manejador import claseManejador
import os
class claseMenu:
    __pos = 0
    __manejador = None
    def __init__(self, pos = 0, manejador = claseManejador()):
        self.__pos = pos
        self.__manejador = manejador
    def Iniciar(self):
        self.__manejador.crearLista()
    def buscar(self, num):
        self.__pos = self.__manejador.buscarViajero(num)
        if(self.__pos != -1):
            print('DATO: viajero encontrado')
        else:
            print('ERROR: viajero no encontrado')
        return self.__pos
    def menu(self, op):
        if(op == 1):    #cunsultar la cantidad de millas acumuladas
           print(('Millas acumuladas: {}'.format(self.__manejador.consultarMillas(self.__pos))))
           os.system('pause')
        elif(op == 2):  #acumular millas
            self.__manejador.acumMilllas(self.__pos, float(input('Millas a acumular: ')))
        elif(op == 3):  #canjear millas
            print('Millas sobrantes: {}'.format(self.__manejador.canjearMillas(self.__pos,
                                                                               float(input('Millas a canjear: ')))))
            os.system('pause')
        elif(op == 4):
            print('DATO: finalizando...')
        else:
            print('ERROR: opción inválida')