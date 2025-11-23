from utils.conexion import Conexion

class SplashScreen:
    def __init__(self):
        self.db = Conexion().get_connection()
        self.exibir()

    def exibir(self):
        qtd_motoristas = self.db.motoristas.count_documents({}) if self.db else 0
        qtd_veiculos = self.db.veiculos.count_documents({}) if self.db else 0
        qtd_fretes = self.db.fretes.count_documents({}) if self.db else 0

        print("===============================================")
        print("           SISTEMA DE TRANSPORTADORA          ")
        print("             (Banco de Dados MongoDB)         ")
        print("===============================================")
        print("Integrantes do Grupo:")
        print("  - Clara Berilli")
        print("  - Josué Felipe ")
        print("  - Glaupierre Oliveira")
        print("  - Leandro Bahia")
        print("  - Kaio Pacheco")
        print("  - Saulo Zambon")
        print("\nDisciplina: Banco de Dados")
        print("Professor: Howard Roatti")
        print("\nStatus do Banco:")
        print(f"  Motoristas: {qtd_motoristas}")
        print(f"  Veículos: {qtd_veiculos}")
        print(f"  Fretes: {qtd_fretes}")
        print("===============================================")
        input("Pressione ENTER para continuar...")
