# Importa a classe BaseModel da biblioteca Pydantic, que serve para criar modelos 
# de dados. Estes modelos garantem que os dados inseridos têm o formato correto 
# (por exemplo, que o 'preco' é sempre um número decimal e não um texto).
from pydantic import BaseModel

# Modelo de Produto Genérico: 
# Usado para produtos simples onde a descrição é apenas um texto (str).
class Product(BaseModel):
    nome: str
    preco: float
    categoria: str
    stock: int
    # Caracteristicas = descrição
    descr: str


# ==========================================
# ELECTRONIC/TECH MODELS (Modelos de Tecnologia)
# ==========================================

# Sub-modelo para a descrição: Define que a descrição de um produto tecnológico 
# não é apenas um texto, mas sim um objeto com marca, modelo e cor.
class DescrTechnology(BaseModel):
    marca: str
    modelo: str
    cor: str

# Modelo do Produto Tecnológico: Herda a estrutura base (nome, preco, etc.) mas 
# exige que o campo 'descr' siga a estrutura detalhada do modelo DescrTechnology.
class ProductTechnology(BaseModel):
    nome: str
    preco: float
    categoria: str
    stock: int
    # Caracteristicas = descrição
    descr: DescrTechnology


# ==========================================
# APPAREL/CLOTHING MODELS (Modelos de Vestuário)
# ==========================================

# Sub-modelo para a descrição: Produtos de vestuário precisam de detalhes 
# específicos como tamanho e material, além da cor.
class DescrApparel(BaseModel):
    tamanho: str
    cor: str
    material: str

# Modelo do Produto de Vestuário: Semelhante aos anteriores, mas aqui a 
# descrição (descr) tem de corresponder obrigatoriamente à classe DescrApparel.
class ProductApparel(BaseModel):
    nome: str
    preco: float
    categoria: str
    stock: int
    descr: DescrApparel


# ==========================================
# DECORATION/HOME MODELS (Modelos de Decoração)
# ==========================================

# Sub-modelo para a descrição: Produtos de decoração têm características 
# mais simples, focadas geralmente na marca e na cor.
class DescrDecoration(BaseModel):
    marca: str
    cor: str

# Modelo do Produto de Decoração: Agrupa os dados gerais do produto com a 
# sua descrição específica (DescrDecoration) voltada para artigos de casa.
class ProductDecoration(BaseModel):
    nome: str
    preco: float
    categoria: str
    stock: int
    descr: DescrDecoration