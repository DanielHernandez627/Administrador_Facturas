import json

global name_File
global name_File2
global name_File3
name_File = "productos.json"
name_File2 = "variablesword.json"
name_File3 = "constantes.json"


def read_Json_Category():
    category_Array = []
    with open(name_File, "r") as j:
        category = json.load(j)
        for data in category:
            category_Array.append(data)
    return category_Array


def read_Json_Product(category_select):
    product_Array = []
    with open(name_File, "r") as j:
        category = json.load(j)
    products = category[category_select]
    for data in products:
        product_Array.append(data['nombre'])
    return product_Array


def read_Json_Val_Product(category_select, product_select):
    valor = 0
    with open(name_File, "r") as j:
        category = json.load(j)
    products = category[category_select]
    for data in products:
        if data["nombre"] == product_select:
            valor = data["precio"]
    return valor


def search_id_Product(category_select, product_select):
    with open(name_File, "r") as j:
        category = json.load(j)
    products = category[category_select]
    for data in products:
        if data["nombre"] == product_select:
            valor = data["id"]
    return valor


def read_constants():
    with open(name_File3) as archivo:
        datos = json.load(archivo)

    constants_generals = datos["ConstantesGenerales"]
    constants_individuals = datos["ConstantesIndividual"]

    return constants_generals, constants_individuals
