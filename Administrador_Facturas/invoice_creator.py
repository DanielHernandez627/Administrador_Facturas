import os

from docxtpl import DocxTemplate
from datetime import datetime
import read_Files as rf
import xml.etree.ElementTree as ET


def replace_variables(data, iva, subtotal, total):
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
    doc = DocxTemplate('Formato_Factura.docx')
    constants_generals, constants_individuals = rf.read_constants()
    file_name = ""

    new_dictionary = {
        'Nombrecompania': constants_generals["NombreCompania"],
        'Representante': constants_generals["Representante"],
        'Direccion': constants_generals["Direccion"],
        'Ciudad': constants_generals["Ciudad"],
        'Telefono': constants_generals["Telefono"],
        'Nombreindividual': constants_individuals["NombreIndividual"],
        'Nombrecomindividual': constants_individuals["NombreCompaniaIndividual"],
        'Direccionindividual': constants_individuals["DireccionIndividual"],
        'Ciudadindividual': constants_individuals["CiudadIndividual"],
        'TelefonoIndividual': constants_individuals["Telefonoindividual"],
        'fecha_actual': fecha_formateada,
        'Subtotal': subtotal,
        'Impuesto': iva,
        'Total': total
    }

    # Contadores para la tabla
    cantelement = 0

    for elemento in data:
        cantelement = cantelement + 1
        for i in range(len(elemento)):
            if i == 0:
                clave = f'Descripcion{cantelement}'
                valor = elemento[i]
                new_dictionary[clave] = valor
            elif i == 3:
                clave = f'can{cantelement}'
                valor = elemento[i]
                new_dictionary[clave] = valor
            elif i == 1:
                clave = f'unt{cantelement}'
                valor = elemento[i]
                new_dictionary[clave] = valor
            elif i == 2:
                clave = f'tv{cantelement}'
                valor = elemento[i]
                new_dictionary[clave] = valor

    doc.render(new_dictionary)
    file_name = file_checker('Factura' + fecha_formateada)
    xml_generator(file_name,new_dictionary)
    doc.save(file_name + '.docx')


def file_checker(nombre_archivo):
    contador = 1
    nombre_base, extension = os.path.splitext(nombre_archivo+'.docx')

    while os.path.exists(nombre_archivo):
        nombre_archivo = f"{nombre_base}_{contador}{extension}"
        contador += 1

    return nombre_archivo

def xml_generator(nombre_archivo,diccionario):
    root = ET.Element("Factura")

    for key, value in diccionario.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(str(nombre_archivo)+".xml", encoding="utf-8", xml_declaration=True)
