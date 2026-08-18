# Importa a classe MongoClient para permitir a ligação do Python ao MongoDB.
from pymongo import MongoClient

# Estabelece a ligação à tua base de dados na cloud (MongoDB Atlas).
client = MongoClient("mongodb+srv://joaoamaral1706_db_user:sgekjckPWERSzYNa@api-rest.jxef0hx.mongodb.net/?appName=API-REST")

# Seleciona a base de dados 'product_db'.
db = client.product_db

# Seleciona a coleção 'product_collection' dentro da base de dados.
collection_name = db["product_collection"]

# Cria uma lista em Python (iniciada por '[') que contém múltiplos dicionários (iniciados por '{').
# Cada dicionário representa um "documento" (um produto) que será inserido na base de dados.
# Esta lista organiza os dados exatamente com a mesma estrutura que definiste nos teus modelos Pydantic.
new_list_insert = [

    # ------------------ TECNOLOGIA ------------------
    {
        "nome": "Smartphone Samsung Galaxy S24",
        "preco": 900,
        "categoria": "Tecnologia",
        "stock": 50,
        "descr": {
            "marca": "Samsung",
            "modelo": "S24",
            "cor": "Preto"
        }
    },
    {
        "nome": "Apple MacBook Air M3",
        "preco": 1200,
        "categoria": "Tecnologia",
        "stock": 15,
        "descr": {
            "marca": "Apple",
            "modelo": "Air M3",
            "cor": "Cinza Sideral"
        }
    },
    {
        "nome": "Rato Wireless Logitech MX Master 3S",
        "preco": 110,
        "categoria": "Tecnologia",
        "stock": 30,
        "descr": {
            "marca": "Logitech",
            "modelo": "MX Master 3S",
            "cor": "Preto"
        }
    },
    {
        "nome": "Monitor LG UltraGear 27",
        "preco": 350,
        "categoria": "Tecnologia",
        "stock": 25,
        "descr": {
            "marca": "LG",
            "modelo": "UltraGear 27",
            "cor": "Preto e Vermelho"
        }
    },
    {
        "nome": "Teclado Mecânico Razer BlackWidow",
        "preco": 150,
        "categoria": "Tecnologia",
        "stock": 40,
        "descr": {
            "marca": "Razer",
            "modelo": "BlackWidow V4",
            "cor": "Verde e Preto"
        }
    },
    {
        "nome": "Auscultadores Sony WH-1000XM5",
        "preco": 300,
        "categoria": "Tecnologia",
        "stock": 35,
        "descr": {
            "marca": "Sony",
            "modelo": "WH-1000XM5",
            "cor": "Prata"
        }
    },
    {
        "nome": "Tablet iPad Pro 11",
        "preco": 850,
        "categoria": "Tecnologia",
        "stock": 20,
        "descr": {
            "marca": "Apple",
            "modelo": "Pro 11",
            "cor": "Prata"
        }
    },
    {
        "nome": "Smartwatch Garmin Fenix 7",
        "preco": 600,
        "categoria": "Tecnologia",
        "stock": 12,
        "descr": {
            "marca": "Garmin",
            "modelo": "Fenix 7",
            "cor": "Preto"
        }
    },
    {
        "nome": "Coluna Bluetooth JBL Flip 6",
        "preco": 130,
        "categoria": "Tecnologia",
        "stock": 60,
        "descr": {
            "marca": "JBL",
            "modelo": "Flip 6",
            "cor": "Azul"
        }
    },
    {
        "nome": "Drone DJI Mini 4 Pro",
        "preco": 800,
        "categoria": "Tecnologia",
        "stock": 10,
        "descr": {
            "marca": "DJI",
            "modelo": "Mini 4 Pro",
            "cor": "Branco"
        }
    },

    # ------------------ ROUPA ------------------
    {
        "nome": "T-Shirt Básica Zara",
        "preco": 15,
        "categoria": "Roupa",
        "stock": 100,
        "descr": {
            "tamanho": "L",
            "cor": "Branco",
            "material": "Algodão"
        }
    },
    {
        "nome": "Calças de Ganga Levi's 501",
        "preco": 90,
        "categoria": "Roupa",
        "stock": 45,
        "descr": {
            "tamanho": "32/32",
            "cor": "Azul Escuro",
            "material": "Denim"
        }
    },
    {
        "nome": "Casaco de Inverno The North Face",
        "preco": 250,
        "categoria": "Roupa",
        "stock": 20,
        "descr": {
            "tamanho": "M",
            "cor": "Preto",
            "material": "Nylon e Penas"
        }
    },
    {
        "nome": "Sapatilhas Adidas Ultraboost",
        "preco": 160,
        "categoria": "Roupa",
        "stock": 30,
        "descr": {
            "tamanho": "42",
            "cor": "Branco",
            "material": "Malha Reciclada"
        }
    },
    {
        "nome": "Camisola de Lã Massimo Dutti",
        "preco": 60,
        "categoria": "Roupa",
        "stock": 25,
        "descr": {
            "tamanho": "M",
            "cor": "Bege",
            "material": "Lã"
        }
    },
    {
        "nome": "Calções de Banho Billabong",
        "preco": 40,
        "categoria": "Roupa",
        "stock": 50,
        "descr": {
            "tamanho": "S",
            "cor": "Vermelho",
            "material": "Poliéster"
        }
    },
    {
        "nome": "Vestido de Verão Mango",
        "preco": 45,
        "categoria": "Roupa",
        "stock": 35,
        "descr": {
            "tamanho": "M",
            "cor": "Amarelo",
            "material": "Linho"
        }
    },
    {
        "nome": "Meias Desportivas Puma (Pack 3)",
        "preco": 12,
        "categoria": "Roupa",
        "stock": 150,
        "descr": {
            "tamanho": "39-42",
            "cor": "Branco",
            "material": "Algodão e Elastano"
        }
    },
    {
        "nome": "Casaco de Pele Sintética",
        "preco": 120,
        "categoria": "Roupa",
        "stock": 15,
        "descr": {
            "tamanho": "L",
            "cor": "Castanho",
            "material": "Poliuretano"
        }
    },
    {
        "nome": "Gorro Carhartt",
        "preco": 25,
        "categoria": "Roupa",
        "stock": 80,
        "descr": {
            "tamanho": "Único",
            "cor": "Laranja",
            "material": "Acrílico"
        }
    },

    # ------------------ DECORAÇÃO ------------------
    {
        "nome": "Candeeiro de Mesa Minimalista",
        "preco": 45,
        "categoria": "Decoracao",
        "stock": 25,
        "descr": {
            "marca": "IKEA",
            "cor": "Branco",
            "material": "Metal"
        }
    },
    {
        "nome": "Tapete Felpudo 160x230",
        "preco": 80,
        "categoria": "Decoracao",
        "stock": 15,
        "descr": {
            "marca": "Leroy Merlin",
            "cor": "Cinza",
            "material": "Poliéster"
        }
    },
    {
        "nome": "Quadro Decorativo Abstrato",
        "preco": 35,
        "categoria": "Decoracao",
        "stock": 40,
        "descr": {
            "marca": "Casa",
            "cor": "Multicolor",
            "material": "Tela e Madeira"
        }
    },
    {
        "nome": "Vaso de Cerâmica",
        "preco": 20,
        "categoria": "Decoracao",
        "stock": 60,
        "descr": {
            "marca": "H&M Home",
            "cor": "Terracota",
            "material": "Cerâmica"
        }
    },
    {
        "nome": "Almofada de Veludo",
        "preco": 15,
        "categoria": "Decoracao",
        "stock": 100,
        "descr": {
            "marca": "Zara Home",
            "cor": "Verde Esmeralda",
            "material": "Veludo"
        }
    },
    {
        "nome": "Espelho Redondo de Parede",
        "preco": 50,
        "categoria": "Decoracao",
        "stock": 20,
        "descr": {
            "marca": "Gato Preto",
            "cor": "Dourado",
            "material": "Vidro e Metal"
        }
    },
    {
        "nome": "Vela Aromática Baunilha",
        "preco": 12,
        "categoria": "Decoracao",
        "stock": 120,
        "descr": {
            "marca": "Rituals",
            "cor": "Branco",
            "aroma": "Baunilha"
        }
    },
    {
        "nome": "Relógio de Parede Vintage",
        "preco": 30,
        "categoria": "Decoracao",
        "stock": 35,
        "descr": {
            "marca": "Habitat",
            "cor": "Cobre",
            "material": "Aço"
        }
    },
    {
        "nome": "Cesto de Vime para Mantas",
        "preco": 28,
        "categoria": "Decoracao",
        "stock": 45,
        "descr": {
            "marca": "IKEA",
            "cor": "Natural",
            "material": "Vime"
        }
    },
    {
        "nome": "Planta Artificial Costela de Adão",
        "preco": 40,
        "categoria": "Decoracao",
        "stock": 30,
        "descr": {
            "marca": "Kinda Home",
            "cor": "Verde",
            "material": "Plástico"
        }
    }
]

# Em vez de inserir um produto de cada vez com 'insert_one', a função 'insert_many' 
# pega na lista inteira de dicionários (new_list_insert) e envia tudo para a base de dados
# numa única operação. É muito mais rápido e eficiente!
list_insert = collection_name.insert_many(new_list_insert)