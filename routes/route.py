# Importa o módulo de exceções (validações) que criaste noutro ficheiro.
import exceptions
# Importa APIRouter (para criar rotas em ficheiros separados) e HTTPException (para erros).
from fastapi import APIRouter, HTTPException
# Importa os teus modelos Pydantic para garantir que os dados recebidos estão corretos.
from models.products import ProductApparel, ProductDecoration, ProductTechnology
# Importa a ligação à base de dados MongoDB.
from config.database import collection_name
# Importa as funções que convertem os dados do MongoDB para dicionários legíveis em Python.
from schema.schemas import list_serial, individual_serial
# Importa ObjectId para converter o ID em texto no formato especial que o MongoDB usa (_id).
from bson import ObjectId
from starlette.exceptions import HTTPException

# Cria a instância do router, que vai agrupar todos os endpoints (caminhos) deste ficheiro.
router = APIRouter()


# ---------------------------------------------- GET Request Methods ----------------------------------------------#
# Rota base para ir buscar todos os produtos.
@router.get("/")
async def get_products():
    # collection_name.find() vai buscar todos os documentos. 
    # list_serial() converte essa resposta bruta numa lista de dicionários Python.
    products = list_serial(collection_name.find())
    return products


# Rota para ir buscar apenas UM produto, através do seu ID.
@router.get("/produto")
async def get_one_product(id: str):
    # Primeiro valida se o ID existe na base de dados usando a tua função de validação.
    exceptions.validate_product_search(id)
    # Se existir, procura-o no MongoDB (find_one) e formata o resultado.
    product = individual_serial(collection_name.find_one(ObjectId(id)))
    return product


# ----------------------- GET Request Methods - FILTERS - PESQUISA DE PRODUTOS POR STOCK, CATEGORIA E CARACTERISTICA -----------------------#
# Rota para encontrar produtos que tenham um stock SUPERIOR ao valor especificado (stockFilter).
@router.get("/produtos/stock")
async def get_products_stock(stockFilter: int):
    # Vai buscar todos os produtos à base de dados.
    products = list_serial(collection_name.find())
    productFound = []
    # Percorre todos os produtos e guarda apenas aqueles cujo stock é maior que o filtro.
    for product in products:
        if product['stock'] > stockFilter:
            productFound.append(product)
    return productFound


# GET POR CATEGORIA - FILTER
# Rota para procurar produtos por uma categoria específica.
@router.get("/produtos/categoria/{categoria}")
async def get_products_category(categoryFilter: str):
    products = list_serial(collection_name.find())
    productFound = []
    for product in products:
        # Usa o .lower() para garantir que a pesquisa não falha por causa de letras maiúsculas/minúsculas.
        if product['categoria'].lower() == categoryFilter.lower():
            productFound.append(product)
    # Se a lista continuar vazia após o loop, significa que não encontrou nada.
    if productFound == []:
        return {"Nenhum produto encontrado!"}

    return productFound


# ---------------------------------------------- GET Request Methods - POR CARACTERISTICA - FILTER ----------------------------------------------#
# Rota mais complexa para pesquisar por uma característica específica dentro da descrição (marca, modelo, cor, tamanho, etc).
@router.get("/descrFilter")
async def get_products_descr(descrFilter: str):
    products = list_serial(collection_name.find())
    productFound = []
    # Itera sobre todos os produtos e verifica a categoria primeiro, 
    # para saber quais os campos que existem dentro do dicionário 'descr'.
    for product in products:
        if product['categoria'] == "Tecnologia":
            # Verifica marca, modelo ou cor (ignorando maiúsculas/minúsculas)
            if product['descr']['marca'].lower() == descrFilter.lower():
                productFound.append(product)
            elif product['descr']['modelo'].lower() == descrFilter.lower():
                productFound.append(product)
            elif product['descr']['cor'].lower() == descrFilter.lower():
                productFound.append(product)
        elif product['categoria'] == "Roupa":
            # Verifica tamanho, cor ou material
            if product['descr']['tamanho'].lower() == descrFilter.lower():
                productFound.append(product)
            elif product['descr']['cor'].lower() == descrFilter.lower():
                productFound.append(product)
            elif product['descr']['material'].lower() == descrFilter.lower():
                productFound.append(product)
        elif product['categoria'] == "Decoracao":
            # Verifica marca ou cor
            if product['descr']['marca'].lower() == descrFilter.lower():
                productFound.append(product)
            elif product['descr']['cor'].lower() == descrFilter.lower():
                productFound.append(product)
        else:
            continue  # Se for outra categoria não programada, passa à frente.

    if productFound == []:
        return {"Nenhum produto com essa descrição encontrado!"}
    else:
        return productFound


# ---------------------------------------------- POST Request Methods ----------------------------------------------#
# Rotas para criar (inserir) novos produtos. São separadas por tipo para forçar a validação do respetivo modelo Pydantic.

@router.post("/product/technology")
async def post_product_technology(product: ProductTechnology):
    # Valida regras de negócio (ex: preço e stock > 0, nome preenchido, etc).
    exceptions.validate_product(product)
    # O model_dump() (antigo .dict() no Pydantic) converte o objeto Pydantic num dicionário padrão do Python.
    product_dict = product.model_dump()
    # insert_one guarda o documento no MongoDB.
    collection_name.insert_one(product_dict)
    return {"message": "Produto de tecnologia criado com sucesso!"}


@router.post("/product/apparel")
async def post_product_apparel(product: ProductApparel):
    exceptions.validate_product(product)
    product_dict = product.model_dump()
    collection_name.insert_one(product_dict)
    return {"message": "Produto de roupa/moda criado com sucesso!"}


@router.post("/product/decoration")
async def post_product_decoration(product: ProductDecoration):
    exceptions.validate_product(product)
    product_dict = product.model_dump()
    collection_name.insert_one(product_dict)
    return {"message": "Produto de decoração/casa criado com sucesso!"}


# ----------------------- PUT Request Method - Modificar completamente um produto especifico ------------------------#
# Os métodos PUT normalmente substituem todo o recurso atual pelos dados novos fornecidos.

@router.put("/technology/{id}")
async def put_product_technology(id: str, product: ProductTechnology):
    # Valida as regras do produto e se o ID existe antes de tentar atualizar.
    exceptions.validate_product(product)
    exceptions.validate_product_search(id)
    product_dict = product.model_dump()
    # O operador "$set" do MongoDB atualiza os campos do documento com os dados de product_dict.
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(product_dict)})
    return {"message": "Produto de Tecnologia modificado com sucesso!"}


@router.put("/apparel/{id}")
async def put_product_apparel(id: str, product: ProductApparel):
    exceptions.validate_product(product)
    exceptions.validate_product_search(id)
    product_dict = product.model_dump()
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(product_dict)})
    return {"message": "Produto de Roupa modificado com sucesso!"}


@router.put("/decoration/{id}")
async def put_product_decoration(id: str, product: ProductDecoration):
    exceptions.validate_product(product)
    exceptions.validate_product_search(id)
    product_dict = product.model_dump()
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(product_dict)})
    return {"message": "Produto de Decoração modificado com sucesso!"}


# ----------------------- PATCH REQUEST METHOD - Mudar, adicionar ou remover apenas o stock de um produto específico -----------------------#
# O PATCH é usado para atualizações parciais. Aqui o objetivo é atualizar APENAS a quantidade em stock, mantendo o resto do produto intacto.

# Rota para definir um valor fixo (novo) para o stock.
@router.patch("/produtos/{id}/stock")
async def patch_stock_product(id: str, stock: int):
    exceptions.validate_product_search(id)
    exceptions.validate_stock(stock)  # Garante que o novo stock não é negativo.
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict({"stock": stock})})
    return {"message": "Stock do produto modificado com sucesso!"}


# Rota para adicionar unidades ao stock existente (ex: chegou nova encomenda ao armazém).
@router.patch("/produtos/{id}/adicionar/stock")
async def patch_add_stock_product(id: str, add_stock: int):
    exceptions.validate_product_search(id)
    # Vai buscar o produto atual para saber quanto stock tem neste momento.
    product = individual_serial(collection_name.find_one(ObjectId(id)))
    old_stock = product["stock"]
    # Soma o valor antigo com a quantidade a adicionar.
    product["stock"] = old_stock + add_stock
    # Atualiza apenas a chave "stock" na base de dados.
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict({"stock": product["stock"]})})
    return {"message": "Stock adicionado com sucesso!"}


# Rota para remover unidades do stock (ex: um cliente fez uma compra).
@router.patch("/produtos/{id}/remover/stock")
async def patch_remove_stock_product(id: str, remove_stock: int):
    exceptions.validate_product_search(id)
    product = individual_serial(collection_name.find_one(ObjectId(id)))
    old_stock = product["stock"]
    # Subtrai o valor indicado.
    product["stock"] = old_stock - remove_stock
    stock = product["stock"]
    # É super importante validar AQUI, pois a subtração pode ter gerado um número negativo!
    exceptions.validate_stock(stock)
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict({"stock": product["stock"]})})
    return {"message": "Stock removido com sucesso!"}


# ----------------------- DELETE REQUEST Method -----------------------#
# Rotas para apagar dados da coleção.

# Rota para apagar apenas um produto pelo seu ID.
@router.delete("/{id}")
async def delete_product(id: str):
    # Verifica primeiro se ele existe.
    exceptions.validate_product_search(id)
    # Procura pelo ID gerado pelo MongoDB e elimina esse documento.
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Produto apagado com sucesso!"}


# Rota para apagar TODOS os produtos de uma vez.
@router.delete("/")
async def delete_all_products():
    try:
        # Passar um dicionário vazio {} ao delete_many significa "aplica a todos os documentos".
        collection_name.delete_many({})
    except:
        # Se a base de dados falhar (ex: por timeout), lança um erro HTTP.
        raise HTTPException(status_code=400, detail="Não foi possível apagar os produtos com sucesso!")
    return {"message": "Todos os produtos apagados com sucesso!"}