class SanidadeCheck:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SanidadeCheck.__instance:
            SanidadeCheck.__instance = super(SanidadeCheck, cls).__new__(
                cls,
                *args,
                **kwargs
            )
        return SanidadeCheck.__instance

    def __init__(self) -> None:
        self.__servidores: list = []

    def checar_servidor(self, srv):
        print(f'Checando o {self.__servidores[srv]}')

    def add_servidor(self):
        self.__servidores.extend(
            ['Servidor 1', 'Servidor 2', 'Servidor 3', 'Servidor 4']
        )

    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append('Servidor 5')


sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

sc1.add_servidor()

print(f'Cronograma de checagem de sanidade dos servidores A...')
for sv in range(4):
    sc1.checar_servidor(sv)

sc2.mudar_servidor()

print(f'Cronograma de checagem de sanidade dos servidores B...')
for sv in range(4):
    sc2.checar_servidor(sv)
