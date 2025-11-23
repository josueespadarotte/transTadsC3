DOCUMENTAÇÃO DO SISTEMA DE TRANSPORTADORA - LINUX
INSTALAÇÃO DAS DEPENDÊNCIAS
bash
sudo apt update && sudo apt upgrade 

# Instalar Python e pip
sudo apt install python3 python3-pip git 

# Instalar MongoDB
sudo apt install mongodb 
# Iniciar MongoDB
sudo systemctl start mongodb
sudo systemctl enable mongodb

# Verificar status
sudo systemctl status mongodb
CONFIGURAÇÃO DO PROJETO
ESTRUTURA DE ARQUIVOS
text
sistema-transportadora-mongo/
 model/ (classes das entidades)
 controller/ (operações CRUD)
 reports/ (relatórios MongoDB)
 utils/ (conexão e utilidades)
 principal.py (arquivo principal)
 requirements.txt
INSTALAÇÃO DAS DEPENDÊNCIAS PYTHON
bash

cd sistema-transportadora-mongo

# Instalar PyMongo
pip3 install pymongo

EXECUÇÃO DO SISTEMA
PRIMEIRA EXECUÇÃO
bash
python3 principal.py
FLUXO RECOMENDADO DE USO

Primeiro: Inserir Motoristas
Segundo: Inserir Veículos
Terceiro: Inserir Fretes
Depois: Utilizar relatórios e outras funcionalidades

MENUS E FUNCIONALIDADES
MENU PRINCIPAL

1.  Relatórios
2.  Inserir Documentos
3.  Remover Documentos
4.  Atualizar Documentos
5.  Sair
   
RELATÓRIOS DISPONÍVEIS
Total de Fretes por Motorista (Agregação com GROUP BY)
Detalhes dos Fretes (Junção entre coleções)

CONFIGURAÇÃO
O sistema usa MongoDB local na porta padrão 27017
Database: transportadora
Coleções: motoristas, veiculos, fretes



