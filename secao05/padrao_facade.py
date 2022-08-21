# Façade
class GerenciamentoEventos:

    def __init__(self) -> None:
        print('GerenciamentoEventos :: Vou organizar com todo mundo!\n\n')

    def organizar(self) -> None:
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()


# Subsistema 1:
class SalaoFestas:

    def __init__(self) -> None:
        print('SalaoFestas :: Agendando o salão de festas para o casamento...')

    def esta_disponivel(self) -> bool:
        print('SalaoFestas :: Este salão de festas está disponível?')
        return True

    def agendar(self) -> None:
        if self.esta_disponivel():
            print('SalaoFestas :: Agendamento do salão realizado.\n')


# Subsistema 2
class Florista:

    def __init__(self) -> None:
        print('Florista :: Flores para um evento?')

    def arranjar_flores(self) -> None:
        print('Florista :: Rosas, Margaridas e Lírios serão usados...\n')


# Subsistema 3
class Restaurante:

    def __init__(self) -> None:
        print('Restaurante :: Comida para eventos...')

    def preparar(self):
        print('Restaurante :: Comida chinesa e brasileira serão sevidas...\n')


# Subsistema 4
class Banda:

    def __init__(self) -> None:
        print('Banda :: Aranjos musicais para o evento...')

    def montar_palco(self):
        print(
            'Banda :: Preparando o palco para tocar jazz e rock no evento.\n'
        )


# Cliente
class Cliente:

    def __init__(self) -> None:
        print('Cliente :: Uau! Preparação para o casamento.')

    def contrata_gerente_eventos(self):
        print('Cliente :: Vou contratar uma empresa para gerenciar eventos.\n')

        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print(
            'Cliente :: Foi muito simples organizar este evento com o Façade!'
        )


if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()
