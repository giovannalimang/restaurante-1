from flask import Flask
from database import init_db
from repository.PratoRepository import PratoRepository
from repository.FuncionarioRepository import FuncionarioRepository
from controller import prato_controllers

app = Flask(__name__)

pratoRepository=PratoRepository()
funcionarioRepository = FuncionarioRepository()
app.secret_key = 'sua_chave_secreta_aqui' 

app.register_blueprint(prato_controllers)


if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)