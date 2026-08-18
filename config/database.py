# Importa a classe MongoClient da biblioteca pymongo, que é a ferramenta 
# necessária para o Python conseguir comunicar com bases de dados MongoDB.
from pymongo import MongoClient

# Estabelece a ligação (o "cliente") à base de dados alojada na cloud (MongoDB Atlas). 
# O texto entre aspas é a "Connection String", que contém o utilizador, a password e o endereço do servidor.
client = MongoClient("mongodb+srv://joaoamaral1706_db_user:sgekjckPWERSzYNa@api-rest.jxef0hx.mongodb.net/?appName=API-REST")

# Seleciona a base de dados específica chamada 'product_db' a partir da ligação que acabámos de criar. 
# (Se a base de dados não existir, o MongoDB cria-a automaticamente quando inserires o primeiro dado).
db = client.product_db

# Dentro da base de dados 'product_db', seleciona a coleção (o equivalente a uma tabela no SQL) 
# chamada 'product_collection'. A partir daqui, esta variável é usada para inserir, ler ou apagar dados.
collection_name = db["product_collection"]