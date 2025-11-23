from model.motorista import Motorista
from utils.conexion import Conexion

class ControllerMotorista:
    def __init__(self):
        self.db = Conexion().get_connection()

    def inserir_motorista(self, motorista):
        try:
            collection = self.db.motoristas
            result = collection.insert_one(motorista.to_dict())
            return result.inserted_id
        except Exception as e:
            print(f"Erro ao inserir motorista: {e}")
            return None

    def listar_motoristas(self):
        try:
            collection = self.db.motoristas
            motoristas = list(collection.find())
            return motoristas
        except Exception as e:
            print(f"Erro ao listar motoristas: {e}")
            return []

    def buscar_motorista_por_id(self, id_motorista):
        try:
            collection = self.db.motoristas
            motorista = collection.find_one({'id_motorista': id_motorista})
            return motorista
        except Exception as e:
            print(f"Erro ao buscar motorista: {e}")
            return None

    def atualizar_motorista(self, id_motorista, dados_atualizados):
        try:
            collection = self.db.motoristas
            result = collection.update_one(
                {'id_motorista': id_motorista},
                {'$set': dados_atualizados}
            )
            return result.modified_count
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")
            return 0

    def excluir_motorista(self, id_motorista):
        try:
            collection = self.db.motoristas
            result = collection.delete_one({'id_motorista': id_motorista})
            return result.deleted_count
        except Exception as e:
            print(f"Erro ao excluir motorista: {e}")
            return 0

    def contar_motoristas(self):
        try:
            collection = self.db.motoristas
            return collection.count_documents({})
        except Exception as e:
            print(f"Erro ao contar motoristas: {e}")
            return 0
