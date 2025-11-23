from pymongo import MongoClient

class Conexion:
    def __init__(self):
        self.client = None
        self.db = None

    def get_connection(self):
        if self.db is None:
            try:
                self.client = MongoClient('localhost', 27017)
                self.db = self.client['transportadora']
                print("Conexão com MongoDB estabelecida.")
            except Exception as e:
                print(f"Erro ao conectar com MongoDB: {e}")
                return None
        return self.db
    


    
