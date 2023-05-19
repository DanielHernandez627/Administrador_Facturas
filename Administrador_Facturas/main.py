import tkinter as tk
from tkinter import ttk
import read_Files as rf

global products
global price
products = []
price = 0


def read_products(category_selected):
    for data in rf.read_Json_Product(category_selected):
        products.append(data)
    price = rf.read_Json_Val_Product(category_selected, "Manzanas")
    lb2.config(text="Valor Producto: " + str(price))


def read_Categories():
    read_products("frutas")
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
    lb2.config(text="Valor Producto: " + str(price))


# Interfaz
window = tk.Tk()
window.title('Generado de Facturas')
window.geometry('670x450')
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
select_list_products.place(x=190, y=110)

# Events
select_list_products.bind("<<ComboboxSelected>>", on_select_products)

# Diseño de la tabla
table = ttk.Treeview(window, columns=("column1", "column2", "column3"), show="headings")
table.column("column1", width=100)
table.column("column2", width=150)
table.column("column3", width=200)
table.heading("column1", text="ID")
table.heading("column2", text="Nombre")
table.heading("column3", text="Precio")
table.insert("", tk.END, values=(1, "Manzanas", 2500))
table.insert("", tk.END, values=(2, "Plátanos", 2000))
table.insert("", tk.END, values=(3, "Fresas", 4000))
table.insert("", tk.END, values=(4, "Piñas", 5000))
table.place(x=20, y=150)


def run():
    window.mainloop()


if __name__ == '__main__':
    run()
