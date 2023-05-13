import json

global name_File
name_File = "productos.json"


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


def read_Json_Val_Product(category_select,product_select):
    valor = 0
    with open(name_File, "r") as j:
        category = json.load(j)
    products = category[category_select]
    for data in products:
        if data["nombre"] == product_select:
            valor = data["precio"]
    return valor