from utils.conexion import Conexion

def relatorio_total_fretes_por_motorista():
    db = Conexion().get_connection()
    pipeline = [
        {
            "$group": {
                "_id": "$motorista_id",
                "total_fretes": {"$sum": 1},
                "valor_total": {"$sum": "$valor"}
            }
        },
        {
            "$lookup": {
                "from": "motoristas",
                "localField": "_id",
                "foreignField": "id_motorista",
                "as": "motorista"
            }
        },
        {
            "$unwind": "$motorista"
        },
        {
            "$project": {
                "motorista": "$motorista.nome",
                "total_fretes": 1,
                "valor_total": 1,
                "_id": 0
            }
        },
        {
            "$sort": {"valor_total": -1}
        }
    ]
    resultados = db.fretes.aggregate(pipeline)
    print("\n--- Total de Fretes por Motorista ---")
    for resultado in resultados:
        print(f"Motorista: {resultado['motorista']}")
        print(f"  Total de Fretes: {resultado['total_fretes']}")
        print(f"  Valor Total: R$ {resultado['valor_total']:.2f}")
        print()

def relatorio_detalhes_fretes():
    db = Conexion().get_connection()
    pipeline = [
        {
            "$lookup": {
                "from": "motoristas",
                "localField": "motorista_id",
                "foreignField": "id_motorista",
                "as": "motorista"
            }
        },
        {
            "$lookup": {
                "from": "veiculos",
                "localField": "veiculo_id",
                "foreignField": "id_veiculo",
                "as": "veiculo"
            }
        },
        {
            "$unwind": "$motorista"
        },
        {
            "$unwind": "$veiculo"
        },
        {
            "$project": {
                "id_frete": 1,
                "data": 1,
                "valor": 1,
                "destino": 1,
                "motorista": "$motorista.nome",
                "veiculo": "$veiculo.placa",
                "modelo": "$veiculo.modelo",
                "_id": 0
            }
        },
        {
            "$sort": {"data": -1}
        }
    ]
    resultados = db.fretes.aggregate(pipeline)
    print("\n--- Detalhes dos Fretes ---")
    for resultado in resultados:
        print(f"Frete ID: {resultado['id_frete']}")
        print(f"  Data: {resultado['data']}")
        print(f"  Destino: {resultado['destino']}")
        print(f"  Valor: R$ {resultado['valor']:.2f}")
        print(f"  Motorista: {resultado['motorista']}")
        print(f"  Veículo: {resultado['veiculo']} - {resultado['modelo']}")
        print()
    
