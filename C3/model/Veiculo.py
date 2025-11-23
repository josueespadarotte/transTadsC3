class Veiculo:
    def __init__(self, id_veiculo, placa, modelo, capacidade):
        self.id_veiculo = id_veiculo
        self.placa = placa
        self.modelo = modelo
        self.capacidade = capacidade

    def to_dict(self):
        return {
            'id_veiculo': self.id_veiculo,
            'placa': self.placa,
            'modelo': self.modelo,
            'capacidade': self.capacidade
        }

    def to_string(self):
        return f"Veículo: {self.modelo} (Placa: {self.placa})"
