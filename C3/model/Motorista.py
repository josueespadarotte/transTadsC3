class Motorista:
    def __init__(self, id_motorista, nome, cnh, telefone):
        self.id_motorista = id_motorista
        self.nome = nome
        self.cnh = cnh
        self.telefone = telefone

    def to_dict(self):
        return {
            'id_motorista': self.id_motorista,
            'nome': self.nome,
            'cnh': self.cnh,
            'telefone': self.telefone
        }

    def to_string(self):
        return f"Motorista: {self.nome} (ID: {self.id_motorista})"