from utils.splash_screen import SplashScreen
from controller.controller_motorista import ControllerMotorista
from controller.controller_veiculo import ControllerVeiculo
from controller.controller_frete import ControllerFrete
from reports.relatorios import relatorio_total_fretes_por_motorista, relatorio_detalhes_fretes

class Principal:
    def __init__(self):
        self.controller_motorista = ControllerMotorista()
        self.controller_veiculo = ControllerVeiculo()
        self.controller_frete = ControllerFrete()

    def menu_principal(self):
        while True:
            print("\n========== MENU PRINCIPAL ==========")
            print("1. Relatórios")
            print("2. Inserir Documentos")
            print("3. Remover Documentos")
            print("4. Atualizar Documentos")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.menu_relatorios()
            elif opcao == '2':
                self.menu_inserir()
            elif opcao == '3':
                self.menu_remover()
            elif opcao == '4':
                self.menu_atualizar()
            elif opcao == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida!")

    def menu_relatorios(self):
        while True:
            print("\n--------- RELATÓRIOS ---------")
            print("1. Total de Fretes por Motorista")
            print("2. Detalhes dos Fretes")
            print("3. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                relatorio_total_fretes_por_motorista()
            elif opcao == '2':
                relatorio_detalhes_fretes()
            elif opcao == '3':
                break
            else:
                print("Opção inválida!")

    def menu_inserir(self):
        while True:
            print("\n--------- INSERIR DOCUMENTOS ---------")
            print("1. Motorista")
            print("2. Veículo")
            print("3. Frete")
            print("4. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.inserir_motorista()
            elif opcao == '2':
                self.inserir_veiculo()
            elif opcao == '3':
                self.inserir_frete()
            elif opcao == '4':
                break
            else:
                print("Opção inválida!")

    def menu_remover(self):
        while True:
            print("\n--------- REMOVER DOCUMENTOS ---------")
            print("1. Motorista")
            print("2. Veículo")
            print("3. Frete")
            print("4. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.remover_motorista()
            elif opcao == '2':
                self.remover_veiculo()
            elif opcao == '3':
                self.remover_frete()
            elif opcao == '4':
                break
            else:
                print("Opção inválida!")

    def menu_atualizar(self):
        while True:
            print("\n--------- ATUALIZAR DOCUMENTOS ---------")
            print("1. Motorista")
            print("2. Veículo")
            print("3. Frete")
            print("4. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.atualizar_motorista()
            elif opcao == '2':
                self.atualizar_veiculo()
            elif opcao == '3':
                self.atualizar_frete()
            elif opcao == '4':
                break
            else:
                print("Opção inválida!")

    def inserir_motorista(self):
        print("\n--- Inserir Motorista ---")
        id_motorista = int(input("ID do motorista: "))
        nome = input("Nome: ")
        cnh = input("CNH: ")
        telefone = input("Telefone: ")

        from model.motorista import Motorista
        motorista = Motorista(id_motorista, nome, cnh, telefone)
        resultado = self.controller_motorista.inserir_motorista(motorista)
        if resultado:
            print("Motorista inserido com sucesso!")
        else:
            print("Erro ao inserir motorista.")

    def inserir_veiculo(self):
        print("\n--- Inserir Veículo ---")
        id_veiculo = int(input("ID do veículo: "))
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        capacidade = float(input("Capacidade (kg): "))

        from model.veiculo import Veiculo
        veiculo = Veiculo(id_veiculo, placa, modelo, capacidade)
        resultado = self.controller_veiculo.inserir_veiculo(veiculo)
        if resultado:
            print("Veículo inserido com sucesso!")
        else:
            print("Erro ao inserir veículo.")

    def inserir_frete(self):
        print("\n--- Inserir Frete ---")
        id_frete = int(input("ID do frete: "))
        veiculo_id = int(input("ID do veículo: "))
        motorista_id = int(input("ID do motorista: "))
        data = input("Data (YYYY-MM-DD): ")
        valor = float(input("Valor: "))
        destino = input("Destino: ")

        from model.frete import Frete
        frete = Frete(id_frete, veiculo_id, motorista_id, data, valor, destino)
        resultado = self.controller_frete.inserir_frete(frete)
        if resultado:
            print("Frete inserido com sucesso!")
        else:
            print("Erro ao inserir frete.")

    def remover_motorista(self):
        print("\n--- Remover Motorista ---")
        id_motorista = int(input("ID do motorista a remover: "))
        motorista = self.controller_motorista.buscar_motorista_por_id(id_motorista)
        if motorista:
            print(f"Motorista encontrado: {motorista['nome']}")
            confirmacao = input("Tem certeza que deseja remover? (s/n): ")
            if confirmacao.lower() == 's':
                # Verificar se o motorista tem fretes
                fretes = self.controller_frete.listar_fretes()
                fretes_do_motorista = [f for f in fretes if f['motorista_id'] == id_motorista]
                if fretes_do_motorista:
                    print("Este motorista possui fretes. Não pode ser removido.")
                    return
                resultado = self.controller_motorista.excluir_motorista(id_motorista)
                if resultado:
                    print("Motorista removido com sucesso!")
                else:
                    print("Erro ao remover motorista.")
        else:
            print("Motorista não encontrado.")

    def remover_veiculo(self):
        print("\n--- Remover Veículo ---")
        id_veiculo = int(input("ID do veículo a remover: "))
        veiculo = self.controller_veiculo.buscar_veiculo_por_id(id_veiculo)
        if veiculo:
            print(f"Veículo encontrado: {veiculo['placa']} - {veiculo['modelo']}")
            confirmacao = input("Tem certeza que deseja remover? (s/n): ")
            if confirmacao.lower() == 's':
                # Verificar se o veículo tem fretes
                fretes = self.controller_frete.listar_fretes()
                fretes_do_veiculo = [f for f in fretes if f['veiculo_id'] == id_veiculo]
                if fretes_do_veiculo:
                    print("Este veículo possui fretes. Não pode ser removido.")
                    return
                resultado = self.controller_veiculo.excluir_veiculo(id_veiculo)
                if resultado:
                    print("Veículo removido com sucesso!")
                else:
                    print("Erro ao remover veículo.")
        else:
            print("Veículo não encontrado.")

    def remover_frete(self):
        print("\n--- Remover Frete ---")
        id_frete = int(input("ID do frete a remover: "))
        frete = self.controller_frete.buscar_frete_por_id(id_frete)
        if frete:
            print(f"Frete encontrado: ID {frete['id_frete']} - Destino: {frete['destino']}")
            confirmacao = input("Tem certeza que deseja remover? (s/n): ")
            if confirmacao.lower() == 's':
                resultado = self.controller_frete.excluir_frete(id_frete)
                if resultado:
                    print("Frete removido com sucesso!")
                else:
                    print("Erro ao remover frete.")
        else:
            print("Frete não encontrado.")

    def atualizar_motorista(self):
        print("\n--- Atualizar Motorista ---")
        id_motorista = int(input("ID do motorista a atualizar: "))
        motorista = self.controller_motorista.buscar_motorista_por_id(id_motorista)
        if motorista:
            print(f"Motorista encontrado: {motorista['nome']}")
            print("Deixe em branco os campos que não deseja alterar.")
            nome = input(f"Novo nome ({motorista['nome']}): ") or motorista['nome']
            cnh = input(f"Nova CNH ({motorista['cnh']}): ") or motorista['cnh']
            telefone = input(f"Novo telefone ({motorista['telefone']}): ") or motorista['telefone']
            dados_atualizados = {
                'nome': nome,
                'cnh': cnh,
                'telefone': telefone
            }
            resultado = self.controller_motorista.atualizar_motorista(id_motorista, dados_atualizados)
            if resultado:
                print("Motorista atualizado com sucesso!")
            else:
                print("Erro ao atualizar motorista.")
        else:
            print("Motorista não encontrado.")

    def atualizar_veiculo(self):
        print("\n--- Atualizar Veículo ---")
        id_veiculo = int(input("ID do veículo a atualizar: "))
        veiculo = self.controller_veiculo.buscar_veiculo_por_id(id_veiculo)
        if veiculo:
            print(f"Veículo encontrado: {veiculo['placa']} - {veiculo['modelo']}")
            print("Deixe em branco os campos que não deseja alterar.")
            placa = input(f"Nova placa ({veiculo['placa']}): ") or veiculo['placa']
            modelo = input(f"Novo modelo ({veiculo['modelo']}): ") or veiculo['modelo']
            capacidade = input(f"Nova capacidade ({veiculo['capacidade']}): ") or veiculo['capacidade']
            dados_atualizados = {
                'placa': placa,
                'modelo': modelo,
                'capacidade': float(capacidade)
            }
            resultado = self.controller_veiculo.atualizar_veiculo(id_veiculo, dados_atualizados)
            if resultado:
                print("Veículo atualizado com sucesso!")
            else:
                print("Erro ao atualizar veículo.")
        else:
            print("Veículo não encontrado.")

    def atualizar_frete(self):
        print("\n--- Atualizar Frete ---")
        id_frete = int(input("ID do frete a atualizar: "))
        frete = self.controller_frete.buscar_frete_por_id(id_frete)
        if frete:
            print(f"Frete encontrado: ID {frete['id_frete']} - Destino: {frete['destino']}")
            print("Deixe em branco os campos que não deseja alterar.")
            veiculo_id = input(f"Novo ID do veículo ({frete['veiculo_id']}): ") or frete['veiculo_id']
            motorista_id = input(f"Novo ID do motorista ({frete['motorista_id']}): ") or frete['motorista_id']
            data = input(f"Nova data ({frete['data']}): ") or frete['data']
            valor = input(f"Novo valor ({frete['valor']}): ") or frete['valor']
            destino = input(f"Novo destino ({frete['destino']}): ") or frete['destino']
            dados_atualizados = {
                'veiculo_id': int(veiculo_id),
                'motorista_id': int(motorista_id),
                'data': data,
                'valor': float(valor),
                'destino': destino
            }
            resultado = self.controller_frete.atualizar_frete(id_frete, dados_atualizados)
            if resultado:
                print("Frete atualizado com sucesso!")
            else:
                print("Erro ao atualizar frete.")
        else:
            print("Frete não encontrado.")

def main():
    SplashScreen()
    principal = Principal()
    principal.menu_principal()

if __name__ == "__main__":
    main()
