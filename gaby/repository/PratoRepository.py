from dao.PratoDao import PratoDAO

class PratoRepository:
    def __init__(self) -> None:
        self.pratoDao = PratoDAO()

    def get_all_prato(self):
        return self.pratoDao.get_all_pratos()

    def get_prato_by_id(self, prato_id):
        return self.pratoDao.get_prato_by_id(prato_id)

    def create_prato(self, name, email):
        return self.pratoDao.create_prato(name, email)

    def update_prato(self, prato_id, name, email):
        return self.pratoDao.update_prato(prato_id, name, email)

    def delete_prato(self, prato_id):
        return self.pratoDao.delete_prato(prato_id)