from database import db
class Prato:
    def __init__(self, id, nome,descr,preco,imagem):
        self.id = id
        self.nome = nome
        self.descr=descr
        self.preco = preco
        self.imagem=imagem
        

listaPratos = []
listaPratos.append(Prato(1, "Carne Argentina", "Prato suculento e macio, preparado com cortes selecionados e temperos especiais, para uma experiência saborosa e intensa.", 89.00, "gallery5.jpg"))
listaPratos.append(Prato(2, "Hamburguer","Um sanduíche suculento com carne grelhada, queijo e acompanhamentos variados.", 35.00, "hamburguer.jpg"))
listaPratos.append(Prato(3, "Frango","Peito ou coxa de frango suculenta, assada ou grelhada, com temperos que destacam o sabor caseiro e aconchegante.",45.00, "menu3.jpg"))
listaPratos.append(Prato(4, "Caipirinha"," O clássico brasileiro, feito com cachaça, limão e açúcar, trazendo um equilíbrio entre doce e azedo.",35.00, "drink1.jpg"))
listaPratos.append(Prato(5, "Fettucinne"," Cremoso e cheio de sabor, o fettucine é preparado com arroz arbóreo e ingredientes frescos, criando uma combinação irresistível.",58.00, "macarrao.jpg"))
listaPratos.append(Prato(6, "Salmão","Peixe nobre, levemente grelhado ou assado, com uma crosta dourada e interior macio, perfeito para um toque gourmet.",75.00, "peixe.jpg"))
listaPratos.append(Prato(7, "Margarita"," Combinação refrescante de tequila, limão e licor de laranja, perfeita para quem busca um toque cítrico e vibrante.",25.00, "drink2.jpg"))
listaPratos.append(Prato(8, "Suco"," Suco Natural de sabores diversos.",10.00, "drink3.jpg"))
listaPratos.append(Prato(9, "Carne"," Carne: Corte nobre de carne, suculento e perfeitamente temperado, grelhado ou assado para realçar seu sabor intenso e macio",78.00, "menu9.jpg"))
listaPratos.append(Prato(10, "Feijoada"," Um clássico brasileiro feito com feijão preto e carnes, servido com arroz e farofa.",66.00, "feijoada.jpg"))
listaPratos.append(Prato(11, "Torta"," Sobremesa delicada com recheio cremoso, perfeita para adoçar o dia.",20.00, "torta.jpg"))
listaPratos.append(Prato(12, "Brownie"," Um bolo denso e irresistível de chocolate, com textura macia e sabor intenso.",12.00, "brownie.jpg"))

usuarios = {
    "user": "1234",
    "admin": "5678"
}


def getPratos():
    return listaPratos

def autenticar(user, senha):
    if user in usuarios:
        if usuarios[user] == senha:
            return user
    return None

class Funcionario(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    cpf=db.Column(db.String(120), unique=True, nullable=False)

class Cardapio(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    preco=db.Column(db.String(80), nullable=False)

