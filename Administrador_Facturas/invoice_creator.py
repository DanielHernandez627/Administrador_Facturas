from docxtpl import DocxTemplate
from datetime import datetime
import read_Files as rf


def replace_variables(iva, subtotal, total):
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
    doc = DocxTemplate('Formato_Factura.docx')
    constants_generals, constants_individuals = rf.read_constants()

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

    doc.render(new_dictionary)
    doc.save('Factura' + fecha_formateada + '.docx')
