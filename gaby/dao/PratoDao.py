from models.model import Prato, db

class PratoDAO:
    @staticmethod
    def get_prato(id):
        return Prato.query.get(id)

    @staticmethod
    def get_all_pratos():
        return Prato.query.all()

    @staticmethod
    def add_prato(id, name,descr,preco):
        prato = Prato(id=id, name=name, descr=descr,preco=preco)
        db.session.add(prato)
        db.session.commit()
        return prato

    @staticmethod
    def att_prato(id, name,descr,preco):
        prato = PratoDAO.get_prato(id)
        if prato:
            prato.id=id
            prato.name = name
            prato.descr=descr
            prato.preco=preco
            db.session.commit()
        return prato

    @staticmethod
    def del_prato(id):
        prato = PratoDAO.get_prato(id)
        if prato:
            db.session.delete(prato)
            db.session.commit()
        return prato

class PratoDAO:
    @staticmethod
    def get_prato(id):
        return Prato.query.get(id)

    @staticmethod
    def get_all_pratos():
        return Prato.query.all()

    @staticmethod
    def add_prato(id, name,descr,preco):
        prato = Prato(id=id, name=name, descr=descr,preco=preco)
        db.session.add(prato)
        db.session.commit()
        return prato

    @staticmethod
    def att_prato(id, name,descr,preco):
        prato = PratoDAO.get_prato(id)
        if prato:
            prato.id=id
            prato.name = name
            prato.descr=descr
            prato.preco=preco
            db.session.commit()
        return prato

    @staticmethod
    def del_prato(id):
        prato = PratoDAO.get_prato(id)
        if prato:
            db.session.delete(prato)
            db.session.commit()
        return prato