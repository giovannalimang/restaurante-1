from dao.FuncionarioDao import FuncionarioDAO

class FuncionarioRepository:
    def __init__(self) -> None:
        self.funcionarioDao = FuncionarioDAO()

    def get_all_funcionario(self):
        return self.funcionarioDao.get_all_funcionarios()

    def get_funcionario_by_id(self, funcionario_id):
        return self.funcionarioDao.get_funcionario_by_id(funcionario_id)

    def create_funcionario(self, name, email):
        return self.funcionarioDao.create_funcionario(name, email)

    def update_funcionario(self, funcionario_id, name, email):
        return self.funcionarioDao.update_funcionario(funcionario_id, name, email)

    def delete_funcionario(self, funcionario_id):
        return self.funcionarioDao.delete_funcionario(funcionario_id)