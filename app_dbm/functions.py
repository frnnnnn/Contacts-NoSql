from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import re

import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import *
from main import add_set



myclient = pymongo.MongoClient(
    "mongodb://localhost:27017/"
)
mydb = myclient["telefono"]
mycol = mydb["contactos"]




def add_contact(nm, ag, ct, ad, nb, fv):
    insert = {
        "nombre": nm,
        "edad": ag,
        "datos_de_contacto": [{"categoria": ct, "direccion": ad, "telefono": nb}],
        "favorito": fv,
    }

    x = mycol.insert_one(insert)


def search_contactByNum(nm, tx1, tx2, tx3, tx4, tx5, tx6):
    filtro = {"datos_de_contacto.telefono": nm}
    find = mycol.find(filtro)
    count = mycol.count_documents(filtro)
    button = None
    if count > 0:
        for i in find:
            tx1.set(f"""Nombre: {i["nombre"]}""")
            tx2.set(f"""Edad: {i["edad"]}""")
            tx3.set(f"""Categoria: {i["datos_de_contacto"][0]["categoria"]}""")
            tx4.set(f"""Direccion: {i["datos_de_contacto"][0]["direccion"]}""")
            tx5.set(f"""Telefono: {i["datos_de_contacto"][0]["telefono"]}""")
            if i["favorito"] == True:
                tx6.set(f"""Favorito: Si""")
            else:
                tx6.set(f"""Favorito: No""")
    else:
        tx1.set("No encontrado")
        tx2.set("")
        tx3.set("")
        tx4.set("")
        tx5.set("")
        tx6.set("")


def search_contactByName(nm, tx1, tx2, tx3, tx4, tx5, tx6, vo):
    regex = re.compile(nm, re.IGNORECASE)
    find = mycol.find({"nombre": {"$regex": regex}})
    count = mycol.count_documents({"nombre": {"$regex": regex}})
    button = vo.children.get("add_set_button")

    for i in find:
        tx1.set(f"""Nombre: {i["nombre"]}""")
        tx2.set(f"""Edad: {i["edad"]}""")
        tx3.set(f"""Categoria: {i["datos_de_contacto"][0]["categoria"]}""")
        tx4.set(f"""Direccion: {i["datos_de_contacto"][0]["direccion"]}""")
        tx5.set(f"""Telefono: {i["datos_de_contacto"][0]["telefono"]}""")
        if i["favorito"] == True:
            tx6.set(f"""Favorito: Si""")
        else:
            tx6.set(f"""Favorito: No""")

        if button is None:
            button = tk.Button(vo, text="Agregar set de Datos", command=lambda: add_set(vo), name="add_set_button")
            button.pack()

    if count == 0:
        tx1.set("No encontrado")
        tx2.set("")
        tx3.set("")
        tx4.set("")
        tx5.set("")
        tx6.set("")
        if button is not None:
            button.destroy()




def verify_telefono(nm, t1, t2, t3, t4, t5, t6):
    try:
        num = nm.get()
        numero = int(num)
        sw = True
    except:
        sw = False
    if not sw:
        messagebox.showinfo(
            "Alerta", "El numero de telefono debe ser de tipo Entero o Numerico."
        )
    else:
        if len(num) < 8 or len(num) > 10:
            messagebox.showinfo(
                "Alerta", "El numero de telefono debe tener entre 8 y 10 caracteres."
            )
        else:
            op = search_contactByNum(numero, t1, t2, t3, t4, t5, t6)


def verify_nombre(nm, t1, t2, t3, t4, t5, t6, v):
    try:
        nombre = nm.get()
        sw = True
    except:
        sw = False
    if not sw:
        messagebox.showinfo("Alerta", "El nombre debe ser de tipo texto.")
    else:
        if len(nombre) < 3:
            messagebox.showinfo("Alerta", "El nombre debe tener mas de 3 caracteres.")
        else:
            op = search_contactByName(nombre, t1, t2, t3, t4, t5, t6, v)


def cerrar_nueva_ventana1(nv, ov):
    nv.destroy()  # Cerrar la nueva ventana
    ov.deiconify()  # Mostrar nuevamente la ventana principal


def verify_num(nm):
    filtro = {"datos_de_contacto.telefono": nm}
    find = mycol.find(filtro)
    count = mycol.count_documents(filtro)
    if count > 0:
        return False
    else:
        return True


def add_set_contact(nms, ctg, drc, tel, old_tel):
    patron_regex = re.compile(f"^{nms}.*")
    filtro = {
        "$or": [
            {"nombre": {"$regex": patron_regex}},
            {"datos_de_contacto.telefono": old_tel}
        ]
    }
    new_vals = {
        "$push": {
            "datos_de_contacto": {"categoria": ctg, "direccion": drc, "telefono": tel}
        }
    }
    mycol.update_one(filtro, new_vals)
    messagebox.showinfo("Alerta", "Contacto agregado con exito")




def list_all(tx1, tx2, tx3, tx4, tx5, tx6, vo):
    find = mycol.find()
    labels = []  # Lista para almacenar las etiquetas o variables

    for i, document in enumerate(find):
        # Crear nuevas etiquetas o variables
        new_label1 = tk.StringVar()
        new_label2 = tk.StringVar()
        new_label3 = tk.StringVar()
        new_label4 = tk.StringVar()
        new_label5 = tk.StringVar()
        new_label6 = tk.StringVar()

        # Establecer los valores en las nuevas etiquetas o variables
        new_label1.set(f"Nombre: {document['nombre']}")
        new_label2.set(f"Edad: {document['edad']}")
        new_label3.set(f"Categoria: {document['datos_de_contacto'][0]['categoria']}")
        new_label4.set(f"Direccion: {document['datos_de_contacto'][0]['direccion']}")
        new_label5.set(f"Telefono: {document['datos_de_contacto'][0]['telefono']}")
        if document.get("favorito"):
            new_label6.set("Favorito: Si")
        else:
            new_label6.set("Favorito: No")

        # Agregar las nuevas etiquetas o variables a la lista
        labels.append((new_label1, new_label2, new_label3, new_label4, new_label5, new_label6))

    # Mostrar todas las etiquetas o variables en la interfaz
    for label_set in labels:
        tx1_label = tk.Label(vo, textvariable=label_set[0])
        tx2_label = tk.Label(vo, textvariable=label_set[1])
        tx3_label = tk.Label(vo, textvariable=label_set[2])
        tx4_label = tk.Label(vo, textvariable=label_set[3])
        tx5_label = tk.Label(vo, textvariable=label_set[4])
        tx6_label = tk.Label(vo, textvariable=label_set[5])
        tex7_label = tk.Label(vo, text="_______________________________")

        tx1_label.pack()
        tx2_label.pack()
        tx3_label.pack()
        tx4_label.pack()
        tx5_label.pack()
        tx6_label.pack()
        tex7_label.pack()

def delete_set(screen,name,number, t1, t2, t3, t4, t5, t6, btn):
    filtro = {
        "$or": [
            {"nombre": name},
            {"datos_de_contacto.telefono": number}
        ]
    }

    mycol.delete_one(filtro)
    messagebox.showinfo("Alerta", "Contacto eliminado con exito")
    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")
    t6.set("")
    btn.destroy()
