from Empresa import Empresa
from Funcionario import funcionario

class Menu:
    def __init__(self):
        ...

    def executar (self):
        empresa= Empresa([])
        while True:
            print('Digite o numero o correspondente a opção desejada: ')
            print('1- CADASTRAR FUNCIONARIO')
            print('2-REMOVER FUNCIONARIO')
            print('3- LISTAR FUNCIONARIO')
            opcao = input('--->  ')

            if opcao == '1':
                nome = input('Digite o nome do funcionario: ')
                cargo = input('Digite o cargo do funcionario: ')
                salario = float(input('Digite o salario: '))
                empresa.adicionar_funcionario(
                    funcionario(nome, cargo, salario)
                    )
            
            elif opcao =='2':
                empresa.remover_funcionario(input('Digite o nome do funcionario a ser removido: '))
                
            elif opcao == '3':
                Empresa.listar_funcionario()
Menu().executar()