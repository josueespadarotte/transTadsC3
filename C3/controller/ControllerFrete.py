from model.frete import Frete
from utils.conexion import Conexion

class ControllerFrete:
    def __init__(self):
        self.db = Conexion().get_connection()

    def inserir_frete(self, frete):
        try:
            collection = self.db.fretes
            result = collection.insert_one(frete.to_dict())
            return result.inserted_id
        except Exception as e:
            print(f"Erro ao inserir frete: {e}")
            return None

    def listar_fretes(self):
        try:
            collection = self.db.fretes
            fretes = list(collection.find())
            return fretes
        except Exception as e:
            print(f"Erro ao listar fretes: {e}")
            return []

    def buscar_frete_por_id(self, id_frete):
        try:
            collection = self.db.fretes
            frete = collection.find_one({'id_frete': id_frete})
            return frete
        except Exception as e:
            print(f"Erro ao buscar frete: {e}")
            return None

    def atualizar_frete(self, id_frete, dados_atualizados):
        try:
            collection = self.db.fretes
            result = collection.update_one(
                {'id_frete': id_frete},
                {'$set': dados_atualizados}
            )
            return result.modified_count
        except Exception as e:
            print(f"Erro ao atualizar frete: {e}")
            return 0

    def excluir_frete(self, id_frete):
        try:
            collection = self.db.fretes
            result = collection.delete_one({'id_frete': id_frete})
            return result.deleted_count
        except Exception as e:
            print(f"Erro ao excluir frete: {e}")
            return 0

    def contar_fretes(self):
        try:
            collection = self.db.fretes
            return collection.count_documents({})
        except Exception as e:
            print(f"Erro ao contar fretes: {e}")
            return 0
