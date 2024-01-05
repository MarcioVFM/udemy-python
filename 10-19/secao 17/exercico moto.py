class Moto:
    def __init__(self, marca, modelo, cor, marcha, motor = False):        
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha
        self.__motor = motor
        if self.__marcha < 0 or self.__marcha > 6:
            raise ValueError('Valor iserido na marcha é invalido')
        
    def imprimir(self):
        print(f'marca: {self.__marca}, modelo: {self.__modelo}, cor: {self.__cor}, marcha: {self.__marcha}, estado do motor: {self.__motor}')
    
    def subir_marcha(self):
        if self.__marcha == 6:
            print('Não e possivel aumentar a marcha')
        else:
            self.__marcha += 1
        
    def descer_marcha(self):
        if self.__marcha == 0:
            print('Não e possivel diminuir a marcha')
        else:
            self.__marcha -= 1
    
    def ligar_desligar(self):
            self.__motor = not self.__motor


moto1 = Moto('fodase', 'fodase', 'fodase', 5)
moto1.imprimir()
moto1.subir_marcha()
moto1.imprimir()
moto1.ligar_desligar()
moto1.imprimir()


