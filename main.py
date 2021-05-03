from Menu import claseMenu
import os
if __name__ == '__main__':
    menu = claseMenu()
    salir = False
    menu.Iniciar()
    pos = menu.buscar(int(input('N° de viajero: ')))
    if(pos == -1):
        pass
    else:
        while not salir:
            print('----MENU----\n1. Consultar Cantidad de Millas\n2. Acumular Millas\n3. Canjear Millas'
                  '\n4. Salir')
            op = int(input('Opción: '))
            menu.menu(op)
            os.system('cls')
            salir = op == 4