from ViajeroFrecuente import claseViajeroFrecuente
import csv
class claseManejador:
    __lista = []    #lista de objetos viajero frecuente
    __archi = None    #para leer el archivo csv
    def __init__(self, lista = [], archi = open('ListaViajeros.csv')):
        self.__lista = lista
        self.__archi = archi
    def crearLista(self):   #se crea la lista de viajeros
        band = True
        reader = csv.reader(self.__archi, delimiter = ';')  #lee el archivo
        for fila in reader:
            if(band == True):   #saltea la primera fila del archivo
                band = False
            else:
                #se crea un objeto de la clase viajero frecuente
                unViajero = claseViajeroFrecuente(int(fila[0]), str(fila[1]), str(fila[2]),
                                                  str(fila[3]), float(fila[4]))
                self.__lista.append(unViajero)  #se añade el viajero a la lista
    def buscarViajero(self, num):   #se busca al viajero a partir del numero ingresado
        i = -1
        band = False
        pos = 0
        while(i<len(self.__lista) and band == False):
            i += 1
            if(num == self.__lista[i].getNum()):
                pos = i
                band = True
        return pos
    def consultarMillas(self, pos): #devuelve las millas que tiene acumuladas el viajero
        return self.__lista[pos].cantidadTotaldeMillas()
    def acumMilllas(self, pos, millas): #permite acumular más millas al viajero
        self.__lista[pos].acumularMillas(millas)
    def canjearMillas(self, pos, millas):   #canjea millas
        return self.__lista[pos].canjearMillas(millas)
    def test(self):
        print('Viajero1: {}'.format(self.__lista[0].getNom()))