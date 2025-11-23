from model.veiculo import Veiculo
from utils.conexion import Conexion

class ControllerVeiculo:
    def __init__(self):
        self.db = Conexion().get_connection()

    def inserir_veiculo(self, veiculo):
        try:
            collection = self.db.veiculos
            result = collection.insert_one(veiculo.to_dict())
            return result.inserted_id
        except Exception as e:
            print(f"Erro ao inserir veículo: {e}")
            return None

    def listar_veiculos(self):
        try:
            collection = self.db.veiculos
            veiculos = list(collection.find())
            return veiculos
        except Exception as e:
            print(f"Erro ao listar veículos: {e}")
            return []

    def buscar_veiculo_por_id(self, id_veiculo):
        try:
            collection = self.db.veiculos
            veiculo = collection.find_one({'id_veiculo': id_veiculo})
            return veiculo
        except Exception as e:
            print(f"Erro ao buscar veículo: {e}")
            return None

    def atualizar_veiculo(self, id_veiculo, dados_atualizados):
        try:
            collection = self.db.veiculos
            result = collection.update_one(
                {'id_veiculo': id_veiculo},
                {'$set': dados_atualizados}
            )
            return result.modified_count
        except Exception as e:
            print(f"Erro ao atualizar veículo: {e}")
            return 0

    def excluir_veiculo(self, id_veiculo):
        try:
            collection = self.db.veiculos
            result = collection.delete_one({'id_veiculo': id_veiculo})
            return result.deleted_count
        except Exception as e:
            print(f"Erro ao excluir veículo: {e}")
            return 0

    def contar_veiculos(self):
        try:
            collection = self.db.veiculos
            return collection.count_documents({})
        except Exception as e:
            print(f"Erro ao contar veículos: {e}")
            return 0
