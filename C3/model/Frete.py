class Frete:
    def __init__(self, id_frete, veiculo_id, motorista_id, data, valor, destino):
        self.id_frete = id_frete
        self.veiculo_id = veiculo_id
        self.motorista_id = motorista_id
        self.data = data
        self.valor = valor
        self.destino = destino

    def to_dict(self):
        return {
            'id_frete': self.id_frete,
            'veiculo_id': self.veiculo_id,
            'motorista_id': self.motorista_id,
            'data': self.data,
            'valor': self.valor,
            'destino': self.destino
        }

    def to_string(self):
        return f"Frete: {self.id_frete} - Destino: {self.destino} - Valor: R${self.valor}"
