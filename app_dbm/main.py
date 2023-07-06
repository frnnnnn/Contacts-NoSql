import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import *
import functions
import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

myclient = pymongo.MongoClient(
    "mongodb+srv://gdtall:LtjjDyRa0S06jneh@cluster0.ysnuirr.mongodb.net/?retryWrites=true&w=majority"
)
mydb = myclient["telefono"]
mycol = mydb["contactos"]


def verify(
    nm,
    ag,
    ct,
    ad,
    nb,
    fv,
    name_entry,
    age_entry,
    category_combo,
    adress_entry,
    number_entry,
    favorite_combo,
):
    nombre = nm.get()
    edad = ag.get()
    categoria = ct.get()
    direccion = ad.get()
    numero = nb.get()
    fav = fv.get()

    if nombre == "":
        sw_nombre = False
        messagebox.showinfo("Alerta", "El NOMBRE no puede estar vacio")
    else:
        sw_nombre = True
    while True:
        try:
            if int(edad) < 0 or int(edad) > 100:
                messagebox.showinfo(
                    "Alerta", "La edad debe estar entre 0 y 100 anios")
                sw_edad = False
            else:
                new_edad = int(edad)
                sw_edad = True
            break
        except:
            messagebox.showinfo(
                "Alerta", "La edad debe ser te tipo Entero o Numerica.")
            sw_edad = False
            break
    if len(direccion) < 3:
        messagebox.showinfo(
            "Alerta", "La DIRECCION debe tener mas de 3 caracteres.")
        sw_direccion = False
    else:
        sw_direccion = True
    while True:
        try:
            new_numero = int(numero)
            if len(str(new_numero)) < 8 or len(str(new_numero)) > 10:
                messagebox.showinfo(
                    "Alerta",
                    "El NUMERO DE TELEFONO debe tener entre 8 y 10 caracteres. ",
                )
                sw_numero = False
            else:
                sw_numero = True

            break
        except:
            messagebox.showinfo(
                "Alerta", "El NUMERO DE TELEFONO debe ser de tipo Entero o Numerico."
            )
            sw_numero = False
            break

    if fav == "Si":
        fav = True
    elif fav == "No":
        fav = False

    if sw_nombre and sw_edad and sw_numero and sw_direccion:
        functions.add_contact(nombre, new_edad, categoria,
                              direccion, new_numero, fav)
        name_entry.delete(0, "end")  # Elimina el contenido del primer Entry

        messagebox.showinfo(
            "Exito", "El contacto se a agregado Correctamente!")
        age_entry.delete(0, "end")
        category_combo.current(0)
        adress_entry.delete(0, "end")
        number_entry.delete(0, "end")
        favorite_combo.current(1)

        # add  = messagebox.askokcancel(message="¿Desea continuar?", title="Agregar de nuevo")
        # print(add)


def abrir_nueva_ventana1():
    options = ["Particular", "Comercial", "Trabajo"]
    options1 = ["Si", "No"]
    global nueva_ventana
    ventana.withdraw()  # Ocultar la ventana principal
    nueva_ventana = tk.Toplevel()
    nueva_ventana.geometry("500x700")
    nueva_ventana.title("Nueva Pestaña")
    nueva_ventana.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana(nueva_ventana)
    )  # Asignar función de cierre a la nueva ventana

    # , font=font_style)
    titulo = tk.Label(nueva_ventana, text="NUEVO CONTACTO")
    titulo.pack(pady=(50, 20))

    name = StringVar()
    age = StringVar()
    category = StringVar()
    adress = StringVar()
    number = StringVar()
    favorite = StringVar()

    name_label = Label(nueva_ventana, text="Nombre")
    age_label = Label(nueva_ventana, text="Edad")
    category_label = Label(nueva_ventana, text="Categoria")
    adress_label = Label(nueva_ventana, text="Direccion")
    number_label = Label(nueva_ventana, text="Numero de Telefono")
    favorite_label = Label(nueva_ventana, text="Favorito")

    name_entry = tk.Entry(nueva_ventana, textvariable=name, width=40)
    age_entry = Entry(nueva_ventana, textvariable=age, width=40)
    category_combo = ttk.Combobox(
        nueva_ventana, textvariable=category, values=options, state="readonly", width=37
    )
    adress_entry = Entry(nueva_ventana, textvariable=adress, width=40)
    number_entry = Entry(nueva_ventana, textvariable=number, width=40)
    favorite_combo = ttk.Combobox(
        nueva_ventana,
        textvariable=favorite,
        width=37,
        values=options1,
        state="readonly",
    )
    name_label.pack()
    name_entry.pack()
    age_label.pack(pady=(20, 0))
    age_entry.pack()

    category_label.pack(pady=(20, 0))
    category_combo.current(0)
    category_combo.pack()

    adress_label.pack(pady=(20, 0))
    adress_entry.pack()

    number_label.pack(pady=(20, 0))
    number_entry.pack()

    favorite_label.pack(pady=(20, 0))
    favorite_combo.current(1)
    favorite_combo.pack()

    button = Button(
        nueva_ventana,
        text="Agregar Contacto",
        command=lambda: verify(
            name,
            age,
            category,
            adress,
            number,
            favorite,
            name_entry,
            age_entry,
            category_combo,
            adress_entry,
            number_entry,
            favorite_combo,
        ),
    )

    button.pack(pady=(20, 0))


def abrir_nueva_ventana2():
    global nueva_ventana2
    ventana.withdraw()  # Ocultar la ventana principal
    nueva_ventana2 = tk.Toplevel()
    nueva_ventana2.geometry("500x400")
    nueva_ventana2.title("Nueva Pestaña")
    nueva_ventana2.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana(nueva_ventana2)
    )  # Asignar función de cierre a la nueva ventana

    name = StringVar()
    telefono = StringVar()

    quest_des(nueva_ventana2)




def abrir_nueva_ventana3():
    global nueva_ventana3
    ventana.withdraw()  # Ocultar la ventana principal
    nueva_ventana3 = tk.Toplevel()
    nueva_ventana3.geometry("500x400")
    nueva_ventana3.title("Eliminar un contacto")
    nueva_ventana3.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana(nueva_ventana3)
    )  # Asignar función de cierre a la nueva ventana

    quest_des(nueva_ventana3)


def abrir_nueva_ventana4():
    global nueva_ventana4
    ventana.withdraw()  # Ocultar la ventana principal
    nueva_ventana4 = tk.Toplevel()
    nueva_ventana4.geometry("500x400")
    nueva_ventana4.title("Todos los Contactos")
    nueva_ventana4.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana(nueva_ventana4)
    )  # Asignar función de cierre a la nueva ventana
    
    texto1 = tk.StringVar()
    texto2 = tk.StringVar()
    texto4 = tk.StringVar()
    texto5 = tk.StringVar()
    texto6 = tk.StringVar()
    texto7 = tk.StringVar()

    texto1_label = tk.Label(nueva_ventana4, textvariable=texto1)
    texto2_label = tk.Label(nueva_ventana4, textvariable=texto2)
    texto4_label = tk.Label(nueva_ventana4, textvariable=texto4)
    texto5_label = tk.Label(nueva_ventana4, textvariable=texto5)
    texto6_label = tk.Label(nueva_ventana4, textvariable=texto6)
    texto7_label = tk.Label(nueva_ventana4, textvariable=texto7)

    texto1_label.pack()
    texto2_label.pack()
    texto4_label.pack()
    texto5_label.pack()

    functions.list_all(texto1, texto2, texto4, texto5, texto6, texto7, nueva_ventana4)



def quest_des():
    font_style = font.Font(family="Arial", size=16, weight="bold")
    desicion = StringVar()

    global ventana_qu
    ventana.withdraw()  # Ocultar la ventana principal
    ventana_qu = tk.Toplevel()
    ventana_qu.geometry("500x400")
    ventana_qu.title("Nueva Pestaña")
    ventana_qu.protocol("WM_DELETE_WINDOW",
                        lambda: cerrar_nueva_ventana(ventana_qu))
    titulo = tk.Label(ventana_qu, text="Buscar contacto por:", font=font_style)
    titulo.pack(pady=(100, 20))

    telefono = Button(
        ventana_qu,
        text="Telefono del Contacto",
        width=20,
        relief="groove",
        borderwidth=5,
        command=page_search1,
    ).pack()
    nombre = Button(
        ventana_qu,
        text="Nombre del Contacto",
        width=20,
        relief="groove",
        borderwidth=5,
        command=page_search2,
    ).pack(pady=10)

def quest_des1():
    font_style = font.Font(family="Arial", size=16, weight="bold")
    desicion = StringVar()

    global ventana_qu1
    ventana.withdraw()  # Ocultar la ventana principal
    ventana_qu1 = tk.Toplevel()
    ventana_qu1.geometry("500x400")
    ventana_qu1.title("Buscar contacto para Eliminar")
    ventana_qu1.protocol("WM_DELETE_WINDOW",
                        lambda: cerrar_nueva_ventana(ventana_qu1))
    titulo = tk.Label(ventana_qu1, text="Buscar contacto por:", font=font_style)
    titulo.pack(pady=(100, 20))

    telefono = Button(
        ventana_qu1,
        text="Telefono del Contacto",
        width=20,
        relief="groove",
        borderwidth=5,
        command=page_search1_1,
    ).pack()
    nombre = Button(
        ventana_qu1,
        text="Nombre del Contacto",
        width=20,
        relief="groove",
        borderwidth=5,
        command=page_search2_1,
    ).pack(pady=10)

def page_search1_1():
    global ventana_telefono
    ventana.withdraw()  # Ocultar la ventana principal
    ventana_qu1.destroy()

    ventana_telefono = tk.Toplevel()
    ventana_telefono.geometry("500x400")
    ventana_telefono.title("Buscar por Numero de Telefono")
    ventana_telefono.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana(ventana_telefono)
    )  # Asignar función de cierre a la nueva ventana

    titulo = tk.Label(
        ventana_telefono, text="INGRESAR NUMERO DE TELEFONO", font=font_style
    )
    titulo.pack(pady=(100, 20))

    telefono = StringVar()
    telefono_entry = tk.Entry(
        ventana_telefono, textvariable=telefono, width=40).pack()

    texto1 = StringVar()
    texto2 = StringVar()
    texto3 = StringVar()
    texto4 = StringVar()
    texto5 = StringVar()
    texto6 = StringVar()

    enviar = Button(
        ventana_telefono,
        text="Buscar",
        width=20,
        relief="groove",
        borderwidth=5,
        command=lambda: verify_telefono(
            telefono, texto1, texto2, texto3, texto4, texto5, texto6, ventana_telefono, op=False
        ),
    ).pack(pady=10)

    font_restyle = font.Font(family="Arial", size=10, weight="bold")

    r1 = Label(ventana_telefono, textvariable=texto1, font=font_restyle).pack()
    r2 = Label(ventana_telefono, textvariable=texto2, font=font_restyle).pack()
    r3 = Label(ventana_telefono, textvariable=texto3, font=font_restyle).pack()
    r4 = Label(ventana_telefono, textvariable=texto4, font=font_restyle).pack()
    r5 = Label(
        ventana_telefono,
        textvariable=texto5,
        font=("Arial", 10, "bold underline"),
        underline=0,
    ).pack()
    r6 = Label(ventana_telefono, textvariable=texto6, font=font_restyle).pack()

def page_search1():
    global ventana_telefono
    ventana.withdraw()  # Ocultar la ventana principal
    ventana_qu.destroy()

    ventana_telefono = tk.Toplevel()
    ventana_telefono.geometry("500x400")
    ventana_telefono.title("Buscar por Numero de Telefono")
    ventana_telefono.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana(ventana_telefono)
    )  # Asignar función de cierre a la nueva ventana

    titulo = tk.Label(
        ventana_telefono, text="INGRESAR NUMERO DE TELEFONO", font=font_style
    )
    titulo.pack(pady=(100, 20))

    telefono = StringVar()
    telefono_entry = tk.Entry(
        ventana_telefono, textvariable=telefono, width=40).pack()

    texto1 = StringVar()
    texto2 = StringVar()
    texto3 = StringVar()
    texto4 = StringVar()
    texto5 = StringVar()
    texto6 = StringVar()

    enviar = Button(
        ventana_telefono,
        text="Buscar",
        width=20,
        relief="groove",
        borderwidth=5,
        command=lambda: verify_telefono(
            telefono, texto1, texto2, texto3, texto4, texto5, texto6, ventana_telefono, op=True
        ),
    ).pack(pady=10)

    font_restyle = font.Font(family="Arial", size=10, weight="bold")

    r1 = Label(ventana_telefono, textvariable=texto1, font=font_restyle).pack()
    r2 = Label(ventana_telefono, textvariable=texto2, font=font_restyle).pack()
    r3 = Label(ventana_telefono, textvariable=texto3, font=font_restyle).pack()
    r4 = Label(ventana_telefono, textvariable=texto4, font=font_restyle).pack()
    r5 = Label(
        ventana_telefono,
        textvariable=texto5,
        font=("Arial", 10, "bold underline"),
        underline=0,
    ).pack()
    r6 = Label(ventana_telefono, textvariable=texto6, font=font_restyle).pack()

def verify_telefono(nm, t1, t2, t3, t4, t5, t6, ventana_telefono, op):
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
            op = search_contactByNum(numero, t1, t2, t3, t4, t5, t6,ventana_telefono, op)
def search_contactByNum(nm, tx1, tx2, tx3, tx4, tx5, tx6, vo, op):
    filtro = {"datos_de_contacto.telefono": nm}
    find = mycol.find(filtro)
    count = mycol.count_documents(filtro)
    button = vo.children.get("add_set_button")
    if count > 0:
        for i in find:
            tx1.set(f"""Nombre: {i["nombre"]}""")
            nombre = i["nombre"]
            tx2.set(f"""Edad: {i["edad"]}""")
            tx3.set(f"""Categoria: {i["datos_de_contacto"][0]["categoria"]}""")
            tx4.set(f"""Direccion: {i["datos_de_contacto"][0]["direccion"]}""")
            tx5.set(f"""Telefono: {i["datos_de_contacto"][0]["telefono"]}""")
            numerold = i["datos_de_contacto"][0]["telefono"]
            if i["favorito"] == True:
                tx6.set(f"""Favorito: Si""")
            else:
                tx6.set(f"""Favorito: No""")

            if button is None:
                if op == False:
                    button = tk.Button(vo, text="Eliminar Contacto", command=lambda: functions.delete_set(vo, nombre, numerold, tx1, tx2, tx3, tx4, tx5, tx6, button), name="add_set_button")
                    button.pack()
                elif op:
                    button = tk.Button(vo, text="Agregar set de Contactos", command=lambda: add_set(vo, nombre, numerold, op), name="add_set_button")
                    button.pack()


    else:
        tx1.set("No encontrado")
        tx2.set("")
        tx3.set("")
        tx4.set("")
        tx5.set("")
        tx6.set("")


def page_search2_1():
    global ventana_nombre
    ventana.withdraw()  # Ocultar la ventana principal
    ventana_qu1.destroy()

    ventana_nombre = tk.Toplevel()
    ventana_nombre.geometry("500x400")
    ventana_nombre.title("Buscar por Nombre del contacto")
    ventana_nombre.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana(ventana_nombre)
    )  # Asignar función de cierre a la nueva ventana

    titulo = tk.Label(
        ventana_nombre, text="INGRESAR NOMBRE DEL CONTACTO", font=font_style
    )
    titulo.pack(pady=(80, 20))

    nombre_search = StringVar()
    nombre_entry = tk.Entry(
        ventana_nombre, textvariable=nombre_search, width=40).pack()
    

    texto1 = StringVar()
    texto2 = StringVar()
    texto3 = StringVar()
    texto4 = StringVar()
    texto5 = StringVar()
    texto6 = StringVar()

    enviar = Button(
        ventana_nombre,
        text="Buscar",
        width=20,
        relief="groove",
        borderwidth=5,
        command=lambda: verify_nombre(
            nombre_search, texto1, texto2, texto3, texto4, texto5, texto6,ventana_nombre, op1=False
        )
    ).pack(pady=10)




    font_restyle = font.Font(family="Arial", size=10, weight="bold")

    r1 = Label(ventana_nombre, textvariable=texto1, font=font_restyle).pack()
    r2 = Label(ventana_nombre, textvariable=texto2, font=font_restyle).pack()
    r3 = Label(ventana_nombre, textvariable=texto3, font=font_restyle).pack()
    r4 = Label(ventana_nombre, textvariable=texto4, font=font_restyle).pack()
    r5 = Label(
        ventana_nombre,
        textvariable=texto5,
        font=("Arial", 10, "bold underline"),
        underline=0,
    ).pack()
    r6 = Label(ventana_nombre, textvariable=texto6, font=font_restyle).pack()
def page_search2():
    global ventana_nombre
    ventana.withdraw()  # Ocultar la ventana principal
    ventana_qu.destroy()

    ventana_nombre = tk.Toplevel()
    ventana_nombre.geometry("500x400")
    ventana_nombre.title("Buscar por Nombre del contacto")
    ventana_nombre.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana(ventana_nombre)
    )  # Asignar función de cierre a la nueva ventana

    titulo = tk.Label(
        ventana_nombre, text="INGRESAR NOMBRE DEL CONTACTO", font=font_style
    )
    titulo.pack(pady=(80, 20))

    nombre_search = StringVar()
    nombre_entry = tk.Entry(
        ventana_nombre, textvariable=nombre_search, width=40).pack()
    

    texto1 = StringVar()
    texto2 = StringVar()
    texto3 = StringVar()
    texto4 = StringVar()
    texto5 = StringVar()
    texto6 = StringVar()

    enviar = Button(
        ventana_nombre,
        text="Buscar",
        width=20,
        relief="groove",
        borderwidth=5,
        command=lambda: verify_nombre(
            nombre_search, texto1, texto2, texto3, texto4, texto5, texto6,ventana_nombre, op1=True
        )
    ).pack(pady=10)




    font_restyle = font.Font(family="Arial", size=10, weight="bold")

    r1 = Label(ventana_nombre, textvariable=texto1, font=font_restyle).pack()
    r2 = Label(ventana_nombre, textvariable=texto2, font=font_restyle).pack()
    r3 = Label(ventana_nombre, textvariable=texto3, font=font_restyle).pack()
    r4 = Label(ventana_nombre, textvariable=texto4, font=font_restyle).pack()
    r5 = Label(
        ventana_nombre,
        textvariable=texto5,
        font=("Arial", 10, "bold underline"),
        underline=0,
    ).pack()
    r6 = Label(ventana_nombre, textvariable=texto6, font=font_restyle).pack()

def verify_nombre(nm, t1, t2, t3, t4, t5, t6, v, op1):
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
            op = search_contactByName(nombre, t1, t2, t3, t4, t5, t6, v, op1)

def search_contactByName(nm, tx1, tx2, tx3, tx4, tx5, tx6, vo, op1):
    regex = re.compile(nm, re.IGNORECASE)
    find = mycol.find({"nombre": {"$regex": regex}})
    count = mycol.count_documents({"nombre": {"$regex": regex}})
    button = vo.children.get("add_set_button")

    for i in find:
        tx1.set(f"""Nombre: {i["nombre"]}""")
        nombre = i["nombre"]
        tx2.set(f"""Edad: {i["edad"]}""")
        tx3.set(f"""Categoria: {i["datos_de_contacto"][0]["categoria"]}""")
        tx4.set(f"""Direccion: {i["datos_de_contacto"][0]["direccion"]}""")
        tx5.set(f"""Telefono: {i["datos_de_contacto"][0]["telefono"]}""")
        numerold = i["datos_de_contacto"][0]["telefono"]
        if i["favorito"] == True:
            tx6.set(f"""Favorito: Si""")
        else:
            tx6.set(f"""Favorito: No""")

        if button is None:
                if op1 == False:
                    button = tk.Button(vo, text="Eliminar Contacto", command=lambda: functions.delete_set(vo, nombre, numerold, tx1, tx2, tx3, tx4, tx5, tx6, button), name="add_set_button")
                    button.pack()
                elif op1:
                    button = tk.Button(vo, text="Agregar set de Contactos", command=lambda: add_set(vo, nombre, numerold, op1), name="add_set_button")
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


def add_set(v,nom, numerold, op):
    options = ["Particular", "Comercial", "Trabajo"]

    global ventana_add
    v.withdraw()  # Ocultar la ventana principal

    ventana_modify = tk.Toplevel()
    ventana_modify.geometry("500x400")
    ventana_modify.title("Agregar datos de contacto")
    ventana_modify.protocol(
        "WM_DELETE_WINDOW", lambda: cerrar_nueva_ventana1(ventana_modify, v)
    )  # Asignar función de cierre a la nueva ventana

    titulo = tk.Label(
        ventana_modify, text=f"INGRESAR DATOS A: {nom}", font=("Arial", 16, "bold")
    )
    titulo.pack(pady=(80, 20))

    category = StringVar()
    adress = StringVar()
    number = StringVar()

    category_label = Label(ventana_modify, text="Categoria").pack()
    category_combo = ttk.Combobox(
    ventana_modify, textvariable=category, values=options, state="readonly", width=37
    ).pack()

    adress_label = Label(ventana_modify, text="Direccion").pack()
    adress_entry = Entry(ventana_modify, textvariable=adress, width=40).pack()

    number_label = Label(ventana_modify, text="Numero de Telefono").pack()
    number_entry = Entry(ventana_modify, textvariable=number, width=40).pack()

    button = Button(ventana_modify, text="Agregar", command=lambda: verify_add(ventana_modify, adress, number, category,nom, numerold)).pack(pady=(5,0))




def verify_add(v,ad,nb, ct, name, numerold):
    address = ad.get()
    number = nb.get()
    categoria = ct.get()

    try:
        numero = int(number)
        if len(address) < 3:
            messagebox.showerror("Error", "Ingresa una direccion con mas de 3 caracteres")
        elif len(number) < 8 or len(number) > 10:
            messagebox.showerror("Error", "Ingresa un numero entre 8 y 10 digitos")
        else:
            verificacion = functions.verify_num(number)
            if verificacion:
                functions.add_set_contact(name, categoria, address, numero, numerold)
            else:
                messagebox.showerror("Error", "El numero ya existe, por favor ingresa otro")
            #messagebox.showinfo("Informacion", "Contacto agregado con exito")
    except:
        messagebox.showerror("Error", "Ingresa un numero con caracteres numericos")

def cerrar_nueva_ventana(nv):
    nv.destroy()  # Cerrar la nueva ventana
    ventana.deiconify()  # Mostrar nuevamente la ventana principal

def cerrar_nueva_ventana1(nv,ov):
    nv.destroy()  # Cerrar la nueva ventana
    ov.deiconify()  # Mostrar nuevamente la ventana principal

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.configure()
    whiteL = ttk.Style()
    whiteL.configure("TButton", foreground="white")

    ventana.geometry("500x500")
    ventana.resizable(False, False)
    ventana.title("Agenda de Contactos")

    # Configuración de la fuente del título
    font_style = font.Font(family="Arial", size=16, weight="bold")
    font_p = font.Font(family="Arial", size=9, weight="bold")

    # Crear el título utilizando el widget Label
    titulo = tk.Label(ventana, text="MIS CONTACTOS", font=font_style)
    titulo.pack(pady=(50, 20))

    frame1 = tk.Frame(ventana, borderwidth=0.5,
                      relief="solid", padx=10, pady=10)
    frame1.pack()

    label1 = tk.Button(
        frame1,
        text="Ingresar un contacto",
        width=30,
        relief="groove",
        borderwidth=5,
        command=abrir_nueva_ventana1,
    )
    label1.pack(pady=10)
    label2 = tk.Button(
        frame1,
        text="Modificar un contacto",
        width=30,
        relief="groove",
        borderwidth=5,
        command=quest_des,
    )
    label2.pack(pady=10)
    label3 = tk.Button(
        frame1, text="Eliminar un contacto", width=30, relief="groove", borderwidth=5, command=quest_des1
    )
    label3.pack(pady=10)
    label4 = tk.Button(
        frame1,
        text="Listar todos los contactos de la agenda",
        width=30,
        relief="groove",
        borderwidth=5,
        command=abrir_nueva_ventana4
    )
    label4.pack(pady=10)

    ventana.mainloop()
