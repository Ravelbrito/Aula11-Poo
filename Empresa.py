class Empresa:
    def __init__(self, funcionario):
        ...
        self.funcionario = funcionario

    def adicionar_funcionario(self,novo):
        self.funcionario.append(novo)

    def remover_funcionario(self,remover):
            for i in range(len(self.funcionario)):
                if self.funcionario[i].nome ==remover:
                    self.funcionario.pop(i)
                    break

    def listar_funcionario(self):
        for funcionario in self.funcionario:
            print('')
            print('funcionario_nome')
            print('funcionario_cargo')
            print('funcionario.salario')