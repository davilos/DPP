from abc import ABC, abstractclassmethod
from uuid import uuid4


class Pessoa(ABC):

    def __init__(self, nome: str) -> None:
        super().__init__()
        self.__nome = nome

    @abstractclassmethod
    def ganhar_dinheiro(self) -> None:
        pass


class Aluno(Pessoa):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.__matricula = str(uuid4()).split('-')[0].upper()

    def ganhar_dinheiro(self) -> None:
        print('Como ganhar dinheiro?')


aluno1 = Aluno('Felicity')
print(aluno1.__dict__)
