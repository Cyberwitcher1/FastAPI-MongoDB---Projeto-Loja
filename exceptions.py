# Importa a classe ObjectId para converter textos (strings) no formato de ID único usado pelo MongoDB.
from bson import ObjectId

# Importa a ligação à coleção de produtos que configurámos no ficheiro de base de dados.
from config.database import collection_name

# Importa uma função de formatação (serialização) para converter os dados brutos 
# vindos do MongoDB num formato legível (normalmente um dicionário Python).
from schema.schemas import individual_serial

# Importa o HTTPException para podermos disparar respostas de erro HTTP 
# (como o erro 400 ou 404) quando algo corre mal na API.
from starlette.exceptions import HTTPException


# ==========================================
# VALIDAÇÃO DE PRODUTO NOVO OU ATUALIZADO
# ==========================================
def validate_product(product):
    # Verifica se o nome está vazio. Se estiver, interrompe o pedido e devolve um erro 400 (Bad Request).
    if product.nome == "":
        raise HTTPException(status_code=400, detail="É obrigatório o produto ter um nome!")

    # Garante que o preço tem um valor lógico (não pode ser zero nem negativo).
    if product.preco <= 0:
        raise HTTPException(status_code=400, detail="O preço não pode ser inferior ou igual a zero!")

    # Verifica se a categoria foi preenchida.
    if product.categoria == "":
        raise HTTPException(status_code=400, detail="É obrigatório o produto ter um nome para a categoria!")

    # Impede que um produto seja criado ou atualizado com stock negativo.
    if product.stock < 0:
        raise HTTPException(status_code=400, detail="O stock não pode ser inferior a zero!")

    # Se passar em todos os testes acima, a validação foi bem-sucedida e o código avança.
    else:
        return


# ==========================================
# VALIDAÇÃO ESPECÍFICA DE STOCK
# ==========================================
def validate_stock(stock):
    # Usado, por exemplo, ao subtrair uma quantidade após uma compra. 
    # Garante que a operação nunca deixa o stock abaixo de zero.
    if stock < 0:
        raise HTTPException(status_code=400,
                            detail="O stock não pode originar valores negativos ou ser inferior a zero!")
    else:
        return


# ==========================================
# VALIDAÇÃO DE PESQUISA / EXISTÊNCIA
# ==========================================
def validate_product_search(id):
    # Usa um bloco try/except porque a procura pode falhar por dois motivos:
    # 1. O 'id' fornecido não ser um formato válido para ObjectId do MongoDB.
    # 2. O produto não existir (retornando vazio e quebrando a função individual_serial).
    try:
        # Transforma o ID, procura-o na base de dados e tenta formatar o resultado.
        individual_serial(collection_name.find_one(ObjectId(id)))
    except:
        # Se qualquer passo no 'try' falhar, significa que não encontrámos o produto.
        # Devolve um erro 404 (Not Found).
        raise HTTPException(status_code=404, detail="Id de produto não encontrado!")

    # Se encontrou e formatou sem erros, a função simplesmente termina e o código principal prossegue.
    return