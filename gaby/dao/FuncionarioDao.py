from models.model import Funcionario, db

class FuncionarioDAO:
    @staticmethod
    def get_funcionario(id):
        return Funcionario.query.get(id)

    @staticmethod
    def get_all_funcionarios():
        return Funcionario.query.all()

    @staticmethod
    def add_funcionario(id, name,descr,preco,cargo,salario):
        funcionario = Funcionario(id=id, name=name, descr=descr,preco=preco,cargo=cargo,salario=salario)
        db.session.add(funcionario)
        db.session.commit()
        return funcionario

    @staticmethod
    def att_funcionario(id, name, email, cpf, cargo, salario):
        funcionario = FuncionarioDAO.get_funcionario(id)
        if funcionario:
            funcionario.id=id
            funcionario.name = name
            funcionario.email = email
            funcionario.cpf=cpf
            funcionario.cargo=cargo
            funcionario.salario=salario
            db.session.commit()
        return funcionario

    @staticmethod
    def del_funcionario(id):
        funcionario = FuncionarioDAO.get_funcionario(id)
        if funcionario:
            db.session.delete(funcionario)
            db.session.commit()
        return funcionario