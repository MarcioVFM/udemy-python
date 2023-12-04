"""
Classes

Em POO, classes nada mais sao do que modelos dos objetos do mundo real
sendo representados computacionalmente

Imagine que voce queira fazer um sistr3ema para automaticas o controle das
lâmpadas da sua casa

Classes podem tconter:
    -Atributos: Representam as caracteristicas do objeto. Ou seja,
    pelos atributos conseguimos representar computacionalmente os
    estados do objeto. No caso cores, voltagem, luminosidade , etc.

    -Métodos (funções): Representam os comportamentos do objeto. Ou seja,
    as acoes que este objeto pode realizar no seu sistema. No caso da 
    lâmpada, por exemplo, um comportamento comum que muito provavelmente 
    iriamos querer representar no nosso sistema é o de ligar e desligar a 
    mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python qyando temos um bloco de codigo
que ainda nao esta implementado.

OBS: Quando nomeamos nosas classe em Python utilizamos por conveção o nome 
com inicial em maiusculo. Se o nome for composto, utiliza-se as iniciais em
ambas as palavras em maiusculo, e todas juntas
"""

class Lampada:
    pass

class ContaCorrente:
    pass
lamp = Lampada()
print(type(lamp))#Cria um tipo de dado chamado lampada 
