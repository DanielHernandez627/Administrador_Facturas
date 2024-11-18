import tkinter as tk
from tkinter import ttk
import read_Files as rf
import invoice_creator as ic

global products
global price
products = []
total = 0
invoice_products = []


def read_products(category_selected):
    for data in rf.read_Json_Product(category_selected):
        products.append(data)
    price = rf.read_Json_Val_Product(category_selected, "Preparación de almuerzos")
    lb2.config(text="Valor Producto: " + str(price))


def read_Categories():
    read_products("alimentacion")
    return rf.read_Json_Category()


def on_modified_value(event):
    amount = event.widget.get("1.0")
    select_category = select_list_categories.get()
    select_product = select_list_products.get()
    price = rf.read_Json_Val_Product(select_category, select_product)
    if amount != "\n":
        amount_int = int(amount)
        result = price * amount_int
        lb2.config(text="Valor Producto: " + str(result))


def on_select(event):
    products.clear()
    select = event.widget.get()
    for data in rf.read_Json_Product(select):
        products.append(data)
    select_list_products.configure(values=products)
    select_list_products.current(0)
    price = rf.read_Json_Val_Product(select, products[0])
    lb2.config(text="Valor Producto: " + str(price))


def on_select_products(event):
    select_category = select_list_categories.get()
    select_product = event.widget.get()
    price = rf.read_Json_Val_Product(select_category, select_product)
    producter = select_product
    lb2.config(text="Valor Producto: " + str(price))
    return select_product


def create_row():
    category = select_list_categories.get()
    product = select_list_products.get()
    price = rf.read_Json_Val_Product(category, product)
    id = rf.search_id_Product(category, product)
    cantidad = int(text_box_cant.get("1.0")) * price
    add_values_products(cantidad)
    calcu_iva()
    calcu_total_pay()
    can1 = text_box_cant.get("1.0", 'end-1c')
    invoice_products.append([product, cantidad, price, can1])
    table.insert("", tk.END, values=(id, product, cantidad))


def create_invoice():
    subtotal = text_box_total.get("1.0", 'end-1c')
    iva = text_box_iva.get("1.0", 'end-1c')
    total = text_box_pagar.get("1.0", 'end-1c')
    ic.replace_variables(invoice_products, iva, subtotal, total)
    clean_interface()


def delete_row():
    selected_item = table.focus()
    desc_value_total()
    if selected_item:
        table.delete(selected_item)


def add_values_products(value):
    ant = text_box_total.get("1.0", 'end-1c')
    total = str(float(ant) + float(value))
    text_box_total.delete("1.0", tk.END)
    text_box_total.insert(tk.END, total)


def subtract_value(value):
    ant = text_box_total.get("1.0", 'end-1c')
    total = str(float(ant) - float(value))
    text_box_total.delete("1.0", tk.END)
    text_box_total.insert(tk.END, total)


def desc_value_total():
    ant = text_box_total.get("1.0", 'end-1c')
    selected_row = table.focus()
    if selected_row:
        values = table.item(selected_row, 'values')
        if values:
            column_value = values[2]
            desc_iva(column_value)
            desc_total_pay(column_value)
            subtract_value(column_value)


def calcu_iva():
    ant = text_box_total.get("1.0", 'end-1c')
    iva = float(ant) * 0.19
    text_box_iva.delete("1.0", tk.END)
    text_box_iva.insert(tk.END, iva)


def desc_iva(value):
    iva = float(value) * 0.19
    ant = text_box_iva.get("1.0", 'end-1c')
    total = float(ant) - iva
    text_box_iva.delete("1.0", tk.END)
    text_box_iva.insert(tk.END, total)


def calcu_total_pay():
    neto = text_box_total.get("1.0", 'end-1c')
    iva = text_box_iva.get("1.0", 'end-1c')
    pay = float(neto) + float(iva)
    text_box_pagar.delete("1.0", tk.END)
    text_box_pagar.insert(tk.END, pay)


def desc_total_pay(value):
    iva = float(value) * 0.19
    neto = float(value) + iva
    ant = text_box_pagar.get("1.0", 'end-1c')
    total = float(ant) - neto
    text_box_pagar.delete("1.0", tk.END)
    text_box_pagar.insert(tk.END, total)


def clean_interface():
    #Limpieza de tabla
    for item in table.get_children():
        table.delete(item)
    #Limpieza de campos
    text_box_total.delete("1.0", tk.END)
    text_box_total.insert("1.0", 0)
    text_box_iva.delete("1.0", tk.END)
    text_box_iva.insert("1.0", 0)
    text_box_pagar.delete("1.0", tk.END)
    text_box_pagar.insert("1.0", 0)
    


# Interfaz
window = tk.Tk()
window.title('Generado de Facturas')
window.geometry('670x530')
window['bg'] = "#AFEEEE"
lb1 = tk.Label(window, text="Sistema Gestor de Facturas")
lb1.config(font=("Arial", 20, "bold"), background="#AFEEEE")
lb1.grid(column=0, row=0)
lb1.place(x=150, y=28)
lb2 = tk.Label(window, text="Valor Producto: ")
lb2.config(background="#AFEEEE")
lb2.grid(column=0, row=0)
lb2.place(x=475, y=110)
lb3 = tk.Label(window, text="Cantidad Unidades: ")
lb3.config(background="#AFEEEE")
lb3.grid(column=0, row=0)
lb3.place(x=345, y=85)
# campos de valor neto
lb4 = ttk.Label(window, text="Total sin IVA: ")
lb4.config(background="#AFEEEE")
lb4.grid(column=0, row=0)
lb4.place(x=490, y=280)
text_box_total = tk.Text(window, height=1, width=12)
text_box_total.place(x=500, y=300)
text_box_total.insert("1.0", 0)
# campos de valor solo iva
lb5 = ttk.Label(window, text="Valor con Impuesto")
lb5.config(background="#AFEEEE")
lb5.grid(column=0, row=0)
lb5.place(x=490, y=330)
text_box_iva = tk.Text(window, height=1, width=12)
text_box_iva.place(x=500, y=360)
text_box_iva.insert("1.0", 0)
# campos valor total a pagar
lb6 = ttk.Label(window, text="Valor a Pagar")
lb6.config(background="#AFEEEE")
lb6.place(x=490, y=390)
text_box_pagar = tk.Text(window, height=1, width=12)
text_box_pagar.place(x=500, y=420)
text_box_pagar.insert("1.0", 0)
# campos valor cantidad
text_box_cant = tk.Text(window, height=1, width=3)
text_box_cant.place(x=385, y=110)
text_box_cant.insert(tk.END, 1)
text_box_cant.bind("<KeyRelease>", on_modified_value)
select_list_categories = ttk.Combobox(window, values=read_Categories())
select_list_categories.bind("<<ComboboxSelected>>", on_select)
select_list_categories.place(x=25, y=110)
select_list_categories.current(0)
select_list_products = ttk.Combobox(window, values=products)
select_list_products.current(0)
select_list_products.place(x=180, y=110)
# boton de guardar compra
button_save = tk.Button(window, text="Guardar Compra", command=create_row)
button_save.pack()
button_save.place(x=520, y=150)
# boton de eliminar compra
button_delete = tk.Button(window, text="Eliminar Compra", command=delete_row)
button_delete.pack()
button_delete.place(x=520, y=195)
# boton de Finalizar compra
button_save = tk.Button(window, text="Finalizar Compra", command=create_invoice)
button_save.pack()
button_save.place(x=520, y=240)

# Events
select_list_products.bind("<<ComboboxSelected>>", on_select_products)

# Diseño de la tabla
table = ttk.Treeview(window, height=13, columns=("column1", "column2", "column3"), show="headings")
table.column("column1", width=100)
table.column("column2", width=150)
table.column("column3", width=200)
table.heading("column1", text="ID")
table.heading("column2", text="Nombre")
table.heading("column3", text="Precio")
table.place(x=20, y=150)


def run():
    window.mainloop()


if __name__ == '__main__':
    run()
