def individual_serial(product) -> dict:
    return {
        "id": str(product["_id"]),
        "nome": product["nome"],
        "preco": product["preco"],
        "categoria": product["categoria"],
        "stock": product["stock"],
        "descr": product["descr"],
    }



def list_serial(products) -> list:
    return [individual_serial(product) for product in products]


