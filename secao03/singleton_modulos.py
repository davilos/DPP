import meu_modulo


print(f'O nome é {meu_modulo.NOME}')

meu_modulo.funcao1()

# import meu_modulo as mm  # Aqui ele não imprime "O módulo foi importado",
# isso ocorre devido ao Singleton que existe na linguagem, como já tem uma
# instância criada, ela não cria outra

# mm.funcao2()
