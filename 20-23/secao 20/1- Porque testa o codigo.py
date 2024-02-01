"""
Testes automatizados

Porque testa o nosso codigo?
-Reduzir bugs
-Teste garaem que novos recursos da sua aplicação nao quebrem (alterem) recursos anigos;
-testes garantem que bugs (problemas) que foram corrigidos anteriormene cotiuam corrigidos;
-Testes garantem que a refatoração que cotumamos a fazer nao tragam novos bugs

TDD - Test Driver esagios de desenvolvimento

Com TD e utilizado esagios de desenvolvimeto:
-Voce escreve seu teste primeiro;
-entao refatora o codigo para realizar a funcionalidade e testa novamente;
-uma vez que o tese passe, o recurso e considerado completo;

estagios de desenvolvimento
-Red, Green, Refactor
"""

class Gato:

    def __ini__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def miar(self):
        return f"{self.__nome} esta miando... "