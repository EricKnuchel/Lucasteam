from tkinter import ttk, Tk, Button, Toplevel, Label, Entry, StringVar, Canvas
from pandasgui import show
from app.estructura.catalogo import Juegos
from app.db.consultas_db import *
from app.crud.operaciones import delete_juego, update_juegos, get_info_for_id, listar_juegos_db
from app.pandas.consultas_pd import listado_pandas
from app.validaciones.validaciones import validar_year_par


class Ventana:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Game Sales")
        self.master.resizable(0, 0)
        self.master.configure(bg='#FF9EA0')
        self.master.geometry("300x600")
        self.master.eval(f'tk::PlaceWindow {str(self.master)} center')
        # Crear un Canvas que ocupe toda la ventana
        canvas = Canvas(self.master, width=300, height=600)
        canvas.pack()

        # Definir los colores para el degradado
        color1 = "#FF9EA0"  # Primer color
        color2 = "#87BAE1"  # Segundo color

        # Dibujar el degradado
        for i in range(600):
            # Calcular el color en cada posición vertical
            r = int((1 - i / 600) * int(color1[1:3], 16) + (i / 600) * int(color2[1:3], 16))
            g = int((1 - i / 600) * int(color1[3:5], 16) + (i / 600) * int(color2[3:5], 16))
            b = int((1 - i / 600) * int(color1[5:7], 16) + (i / 600) * int(color2[5:7], 16))
            color = f"#{r:02X}{g:02X}{b:02X}"

            # Dibujar una línea vertical del color correspondiente
            canvas.create_line(0, i, 600, i, fill=color, width=1)

        canvas.create_text(150, 15, text="Proyecto LucasSteam ©", font=('Arial', 12, 'bold'), fill='black')
        # Configuración de la ventana principal
        self.setup_main_window()

    def setup_main_window(self):
        # Botones en la ventana principal
        insert_button = Button(self.master, text="Datos Manual", width=25, command=self.insert_data)
        insert_button.place(x=60, y=40)

        show_button = Button(self.master, text="Mostrar Lista de Juegos", width=25, command=self.show_list)
        show_button.place(x=60, y=80)

        show_db_button = Button(self.master, text="Mostrar Lista de Juegos (DB)", width=25, command=self.show_list_db)
        show_db_button.place(x=60, y=120)
        
        show_df_button = Button(self.master, text="Mostrar Lista de Juegos (Panda)", width=25, command=self.data_frame)
        show_df_button.place(x=60, y=160)
        
        show_xx = Button(self.master, text="Mostrar Juegos Siglo XX", width=25, command=self.show_list_xx)
        show_xx.place(x=60, y=200)
        

        show_genero_button = Button(self.master, text="Filtrar por género", width=25, command=self.insert_genero)
        show_genero_button.place(x=60, y=240)

        delete = Button(self.master, text="Update Juego", width=25, command=self.update)
        delete.place(x=60, y=280)

        delete = Button(self.master, text="Delete Juego", width=25, command=self.delete)
        delete.place(x=60, y=320)

        show_platform_button = Button(self.master, text="Juegos Nintendo", width=25, command=self.show_platform)
        show_platform_button.place(x=60, y=360)

        show_par_button = Button(self.master, text="Juegos año par", width=25, command=self.show_year_par)
        show_par_button.place(x=60, y=400)

        show_media_button = Button(self.master, text="Juegos superior a la media EU", width=25, command=self.superior_a_media)
        show_media_button.place(x=60, y=440)
        
        show_max_vent_button = Button(self.master, text="Juegos más vendidos Global", width=25, command=self.mas_vendidos)
        show_max_vent_button.place(x=60, y=480)
        
        show_max_vent_button = Button(self.master, text="Juegos más vendidos Regional", width=25, command=self.insert_region)
        show_max_vent_button.place(x=60, y=520)
        
        show_genero_button = Button(self.master, text="Mostrar juegos por editor", width=25, command=self.insert_editor)
        show_genero_button.place(x=60, y=560)

    def update(self):
        window = Tk()
        window.title("Update Juegos")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')
        window.geometry("250x250")

        label_id = Label(window, text="ID:", bg='#FF9EA0')
        label_id.place(x=5, y=20)

        id_entry = Entry(window)
        id_entry.place(x=25, y=20, width=25)

        manual_name_label = Label(window, text="Nombre", bg='#FF9EA0')
        manual_name_label.pack()
        manual_name = Entry(window)
        manual_name.pack()

        manual_plat_l = Label(window, text="Plataforma", bg='#FF9EA0')
        manual_plat_l.pack()
        var_plataforma = StringVar(window)
        var_plataforma.set("Ninguna")
        plataformas = ["Ninguna", "Wii", "NES", "GB", "X360", "PS", "PS2", "PS3", "PS4", "PS5", "SNES", "GBA", "3DS",
                       "N64", "XB", "2600", "DS", "XOne", "GC", "GEN", "PSP", "WiiU", "PC", "DC", ]
        plataforma_combobox = ttk.Combobox(window, textvariable=var_plataforma, values=plataformas, state="readonly")
        plataforma_combobox.pack()

        manual_year_l = Label(window, text="Año", bg='#FF9EA0')
        manual_year_l.pack()
        manual_years = StringVar(window)
        manual_years.set("1952")
        manual_vears_list = [str(manual_vears_list) for manual_vears_list in range(1952, 2024)]
        manual_plataform_year_menu = ttk.Combobox(window, textvariable=manual_years, values=manual_vears_list,
                                                  state="readonly")
        manual_plataform_year_menu.pack()

        manual_genero_l = Label(window, text="Genero", bg='#FF9EA0')
        manual_genero_l.pack()
        manual_genero = StringVar(window)
        manual_genero.set("Ninguna")
        manual_genero_lista = ["Sports", "Racing", "Role-Playing", "Puzzle", "Platform", "Misc", "Shooter",
                               "Simulation", "Action", "Fighting", "Adventure", "Strategy"]
        genero_combobox = ttk.Combobox(window, textvariable=manual_genero, values=manual_genero_lista, state="readonly")
        genero_combobox.pack()

        manual_editor_l = Label(window, text="Editor", bg='#FF9EA0')
        manual_editor_l.pack()
        manual_editor = StringVar(window)
        manual_editor.set("Ninguna")
        manual_editor_lista = ["Nintendo", "Microsoft Game Studios", "Take-Two Interactive",
                               "Sony Computer Entertainment", "Activision", "Ubisoft", "Bethesda Softworks",
                               "Electronic Arts", "Sega", "Square Enix", "Atari", "505 Games", "Capcom",
                               "GT Interactive", "Konami Digital Entertainment", "Namco Bandai Games",
                               "Warner Bros. Interactive Entertainment", "Majesco Entertainment", "Codemasters",
                               "RedOctane", "THQ", "Fox Interactive", "Universal Interactive", "LucasArts",
                               "Virgin Interactive", "Palcom", "Hasbro Interactive", "Vivendi Games", "NCSoft",
                               "Deep Silver", "Arena Entertainment", "Valve Software", "ASCII Entertainment",
                               "Mindscape", "Infogrames"]
        editor_combobox = ttk.Combobox(window, textvariable=manual_editor, values=manual_editor_lista, state="readonly")
        editor_combobox.pack()

        def update_juegos_wrapper():
            try:
                ids = int(id_entry.get())
                update_juegos(ids, manual_name.get(), var_plataforma.get(), manual_years.get(),
                              manual_genero.get(), manual_editor.get())

            except ValueError:
                print("Error: Ingresa un número válido en el campo ID.")

        manual_button = Button(window, text="Update", bg="#00FFFF", command=update_juegos_wrapper)
        manual_button.place(x=100, y=220)

    def delete(self):
        self.confirmacion_dell = False
        self.window_del = Tk()
        self.window_del.title("Delete Juegos")
        self.window_del.resizable(0, 0)
        self.window_del.configure(bg='#FF9EA0')
        self.window_del.geometry("200x150")

        label = Label(self.window_del, text="ID:", bg='#FF9EA0')
        label.place(x=5, y=5)

        self.id_entry = Entry(self.window_del)
        self.id_entry.place(x=25, y=5, width=50)

        self.canvas_comandos = Canvas(self.window_del, bg="white", height=65, width=130)
        self.canvas_comandos.place(x=1, y=30)

        get_id = Button(self.window_del, text="Get info", command=self.get_info_from_entry)
        get_id.place(x=140, y=50)

        delete_id = Button(self.window_del, text="Delete ID", bg="#DC2727", command=self.delete_id)
        delete_id.place(x=70, y=110)

        self.window_del.mainloop()

    def delete_id(self):
        if not self.confirmacion_dell:
            print("Seguro que desea borrar este juego")
            self.confirmacion_dell = True
            return
        delete_juego(self.ident)

    def get_info_from_entry(self):
        try:
            self.ident = int(self.id_entry.get())
            info_text = self.get_info(self.ident)

            self.canvas_comandos.delete("all")

            canvas_comandos = Canvas(self.window_del, bg="white", height=65, width=130)
            canvas_comandos.place(x=1, y=30)
            canvas_comandos.create_text(35, 35, text=info_text, fill="black", font='Arial 7')
        except ValueError:
            print("Error: Ingresa un número válido en el Entry.")

    def get_info(self, ident):
        info = get_info_for_id(ident)

        if info is not None:
            x = f"""
            Nombre: {info[1]}
            Plataforma: {info[2]}
            Año: {info[3]}
            Género: {info[4]}
            Editor: {info[5]}
            """
            return x
        else:
            return "Error: No se pudo obtener la información para el ID especificado."

    def insert_data(self):
        window = Tk()
        window.title("Insert Juegos")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')
        window.geometry("250x350")

        manual_name_label = Label(window, text="Nombre", bg='#FF9EA0')
        manual_name_label.pack()
        manual_name = Entry(window)
        manual_name.pack()
        manual_name.insert(0, "Ej: Mario Bros")
        manual_name.config(fg="grey")
        manual_name.bind("<FocusIn>",
                         lambda event: manual_name.delete(0, 'end') if manual_name.get() == "Ej: Mario Bros" else None)
        manual_name.bind("<FocusOut>",
                         lambda event: manual_name.insert(0, "Ej: Mario Bros") if manual_name.get() == "" else None)

        manual_plat_l = Label(window, text="Plataforma", bg='#FF9EA0')
        manual_plat_l.pack()
        var_plataforma = StringVar(window)
        var_plataforma.set("Ninguna")
        plataformas = ["Ninguna", "Wii", "NES", "GB", "X360", "PS", "PS2", "PS3", "PS4", "PS5", "SNES", "GBA", "3DS",
                       "N64", "XB", "2600", "DS", "XOne", "GC", "GEN", "PSP", "WiiU", "PC", "DC", ]
        plataforma_combobox = ttk.Combobox(window, textvariable=var_plataforma, values=plataformas, state="readonly")
        plataforma_combobox.pack()

        manual_year_l = Label(window, text="Año", bg='#FF9EA0')
        manual_year_l.pack()
        manual_years = StringVar(window)
        manual_years.set("1952")
        manual_vears_list = [str(manual_vears_list) for manual_vears_list in range(1952, 2024)]
        manual_plataform_year_menu = ttk.Combobox(window, textvariable=manual_years, values=manual_vears_list,
                                                  state="readonly")
        manual_plataform_year_menu.pack()

        manual_genero_l = Label(window, text="Genero", bg='#FF9EA0')
        manual_genero_l.pack()
        manual_genero = StringVar(window)
        manual_genero.set("Ninguna")
        manual_genero_lista = ["Sports", "Racing", "Role-Playing", "Puzzle", "Platform", "Misc", "Shooter",
                               "Simulation", "Action", "Fighting", "Adventure", "Strategy"]
        genero_combobox = ttk.Combobox(window, textvariable=manual_genero, values=manual_genero_lista, state="readonly")
        genero_combobox.pack()

        manual_editor_l = Label(window, text="Editor", bg='#FF9EA0')
        manual_editor_l.pack()
        manual_editor = StringVar(window)
        manual_editor.set("Ninguna")
        manual_editor_lista = ["Desconocido", "Nintendo", "Microsoft Game Studios", "Take-Two Interactive",
                               "Sony Computer Entertainment", "Activision", "Ubisoft", "Bethesda Softworks",
                               "Electronic Arts", "Sega", "Square Enix", "Atari", "505 Games", "Capcom",
                               "GT Interactive", "Konami Digital Entertainment", "Namco Bandai Games",
                               "Warner Bros. Interactive Entertainment", "Majesco Entertainment", "Codemasters",
                               "RedOctane", "THQ", "Fox Interactive", "Universal Interactive", "LucasArts",
                               "Virgin Interactive", "Palcom", "Hasbro Interactive", "Vivendi Games", "NCSoft",
                               "Deep Silver", "Arena Entertainment", "Valve Software", "ASCII Entertainment",
                               "Mindscape", "Infogrames"]
        editor_combobox = ttk.Combobox(window, textvariable=manual_editor, values=manual_editor_lista, state="readonly")
        editor_combobox.pack()

        manual_ventas_na_l = Label(window, text="Vents NA", bg='#FF9EA0')
        manual_ventas_na_l.place(x=5, y=220)
        manual_ventas_na_e = Entry(window, width=4)
        manual_ventas_na_e.place(x=15, y=240)

        manual_ventas_eu_l = Label(window, text="Vents EU", bg='#FF9EA0')
        manual_ventas_eu_l.place(x=70, y=220)
        manual_ventas_eu_e = Entry(window, width=4)
        manual_ventas_eu_e.place(x=80, y=240)

        manual_ventas_jp_l = Label(window, text="Vents JP", bg='#FF9EA0')
        manual_ventas_jp_l.place(x=130, y=220)
        manual_ventas_jp_e = Entry(window, width=4)
        manual_ventas_jp_e.place(x=140, y=240)

        manual_ventas_ov_l = Label(window, text="Other Vents", bg='#FF9EA0')
        manual_ventas_ov_l.place(x=180, y=220)
        manual_ventas_ov_e = Entry(window, width=4)
        manual_ventas_ov_e.place(x=200, y=240)

        manual_ventas_vg_l = Label(window, text="Vents Globals", bg='#FF9EA0')
        manual_ventas_vg_l.place(x=85, y=270)
        manual_ventas_vg_e = Entry(window, width=4)
        manual_ventas_vg_e.place(x=110, y=290)

        manual_button = Button(window, text="Insert", command=lambda: Juegos.inser_data(
            [len(Juegos.lista_juegos) + 1, manual_name.get(), var_plataforma.get(), manual_years.get(),
             manual_genero.get(), manual_editor.get(), manual_ventas_na_e.get(), manual_ventas_eu_e.get(),
             manual_ventas_jp_e.get(), manual_ventas_ov_e.get(), manual_ventas_vg_e.get()]))
        manual_button.place(x=105, y=320)

    def insert_genero(self):
        window = Tk()
        window.title("Filtrar Juegos por Género")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')
        window.geometry("200x100")

        genero_l = Label(window, text="Genero", bg='#FF9EA0')
        genero_l.pack()
        genero = StringVar(window)
        genero_lista = ["Sports", "Racing", "Role-Playing", "Puzzle", "Platform", "Misc", "Shooter",
                        "Simulation", "Action", "Fighting", "Adventure", "Strategy"]
        genero.set(genero_lista[0])
        genero_combobox = ttk.Combobox(window, textvariable=genero, values=genero_lista, state="readonly")
        genero_combobox.pack()

        manual_button = Button(window, text="Filtrar", command=lambda: self.show_list_genero(genero.get()))
        manual_button.pack(pady=10)

    def show_list(self):
        # Crea una ventana secundaria para mostrar la lista de juegos
        window = Toplevel(self.master)
        window.title("Lista de Juegos")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview(tree)

        # Inserta los datos en el Treeview
        for juego in Juegos.lista_juegos:
            row = (
                juego.rank, juego.name, juego.plataf, juego.year,
                juego.genero, juego.editor
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")

    def show_list_db(self):
        # Crea una ventana secundaria para mostrar la lista de juegos
        window = Toplevel(self.master)
        window.title("Lista de Juegos (DB)")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview(tree)

        # Inserta los datos en el Treeview
        lista_juegos = listar_juegos_db()
        for juego in lista_juegos:
            row = (
                juego[0], juego[1], juego[2], juego[3],
                juego[4], juego[5]
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")

    def show_list_genero(self, g):

        # Crea una ventana secundaria para mostrar la lista de juegos
        window = Toplevel(self.master)
        window.title(f"Lista de Juegos (Género: {g}")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview(tree)

        # Inserta los datos en el Treeview
        lista_generos = show_genere(g)
        for genero in lista_generos:
            row = (
                genero[0], genero[1], genero[2], genero[3],
                genero[4], genero[5]
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")

    def setup_treeview(self, tree):
        columns = ("Rank", "Name", "Platform", "Year", "Genre", "Publisher")

        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=60)  # aqui se ajusta el año de la tabla
            
    def setup_treeview_ventas(self, tree):
        columns = ("Rank", "Name", "Platform", "Year", "Publisher", "V_EU")

        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=60)  # aqui se ajusta el año de la tabla
            
    def setup_treeview_ventas_regional(self, tree, region):
        columns = ("Rank", "Name", "Platform", "Year", "Publisher", region)

        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=60)

    def show_list_xx(self):
        # Crea una ventana secundaria para mostrar la lista de juegos del siglo XX
        window = Toplevel(self.master)
        window.title("Juegos del Siglo XX")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview(tree)

        # Llama a la función show_siglo_xx para obtener los juegos del siglo XX
        juegos_siglo_xx = show_siglo_xx()

        # Inserta los datos en el Treeview
        for juego in juegos_siglo_xx:
            row = (
                juego[0], juego[1], juego[2], juego[3],
                juego[4], juego[5]
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")


    def data_frame(self):
        data = listado_pandas()
        gui = show(data, title='Tabla de Datos Pandas')
 
 
    def show_platform(self):

        window = Toplevel(self.master)
        window.title("Juegos desarrollados por Nintendo")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview(tree)

        juegos_platform = show_platform()

        # Inserta los datos en el Treeview
        for juego in juegos_platform:
            row = (
                juego[0], juego[1], juego[2], juego[3],
                juego[4], juego[5]
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")

    def show_year_par(self):
        window = Toplevel(self.master)
        window.title("Juegos lanzados en año par")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview(tree)

        juegos_par = validar_year_par(show_year_par())

        # Inserta los datos en el Treeview
        for juego in juegos_par:
            row = (
                juego[0], juego[1], juego[2], juego[3],
                juego[4], juego[5]
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")

    def mas_vendidos(self):       
            window = Toplevel(self.master)
            window.title("Juegos mas vendidos Global")
            window.resizable(0, 0)
            window.configure(bg='#FF9EA0')

            # Creación del Treeview en la ventana secundaria
            tree = ttk.Treeview(window)
            self.setup_treeview_ventas(tree)


            max_vent = show_max_venta()

            # Inserta los datos en el Treeview
            for juego in max_vent:
                row = (
                juego[0], juego[1], juego[2], juego[3],
                juego[4], juego[5] # corregir
                )
                tree.insert("", "end", values=row)

            # Configuración del scrollbar vertical
            scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scrollbar.set)

            # Empaqueta el Treeview en la ventana secundaria
            tree.pack(expand=True, fill="both")
    
    def superior_a_media(self):
            window = Toplevel(self.master)
            window.title("Juegos superior a la media en Europa")
            window.resizable(0, 0)
            window.configure(bg='#FF9EA0')

            # Creación del Treeview en la ventana secundaria
            tree = ttk.Treeview(window)
            self.setup_treeview_ventas(tree)


            max_vent = show_media()

            # Inserta los datos en el Treeview
            for juego in max_vent:
                row = (
                    juego[0], juego[1], juego[2], juego[3],
                    juego[4], juego[5] 
                )
                tree.insert("", "end", values=row)

            # Configuración del scrollbar vertical
            scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scrollbar.set)

            # Empaqueta el Treeview en la ventana secundaria
            tree.pack(expand=True, fill="both")
            
    def insert_region(self):
        window = Tk()
        window.title("Filtrar Juegos por Region")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')
        window.geometry("200x100")

        region_l = Label(window, text="Región", bg='#FF9EA0')
        region_l.pack()
        region = StringVar(window)
        region_lista = ["V_NA", "V_EU", "V_JP", "V_Other"]
        region.set(region_lista[0])
        genero_combobox = ttk.Combobox(window, textvariable=region, values=region_lista, state="readonly")
        genero_combobox.pack()

        manual_button = Button(window, text="Filtrar", command=lambda: self.show_list_region(region.get()))
        manual_button.pack(pady=10)
        
        
    def show_list_region(self, region):

        # Crea una ventana secundaria para mostrar la lista de juegos
        window = Toplevel(self.master)
        window.title(f"Juegos mas vendidos en (Región: {region}")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview_ventas_regional(tree, region)

        # Inserta los datos en el Treeview
        lista_generos = show_max_venta_regional(region)
        for genero in lista_generos:
            row = (
                genero[0], genero[1], genero[2], genero[3],
                genero[4], genero[5]
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")
        
    def insert_editor(self):
        window = Tk()
        window.title("Filtrar Juegos por Editor")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')
        window.geometry("200x100")

        editor_l = Label(window, text="Editor", bg='#FF9EA0')
        editor_l.pack()
        editor = StringVar(window)
        editor_lista = ["Unknown","Nintendo", "Microsoft Game Studios", "Take-Two Interactive",
                        "Sony Computer Entertainment", "Activision", "Ubisoft", "Bethesda Softworks",
                        "Electronic Arts", "Sega", "Square Enix", "Atari", "505 Games", "Capcom",
                        "GT Interactive", "Konami Digital Entertainment", "Namco Bandai Games",
                        "Warner Bros. Interactive Entertainment", "Majesco Entertainment", "Codemasters",
                        "RedOctane", "THQ", "Fox Interactive", "Universal Interactive", "LucasArts",
                        "Virgin Interactive", "Palcom", "Hasbro Interactive", "Vivendi Games", "NCSoft",
                        "Deep Silver", "Arena Entertainment", "Valve Software", "ASCII Entertainment",
                        "Mindscape", "Infogrames"]
        editor.set(editor_lista[0])
        editor_combobox = ttk.Combobox(window, textvariable=editor, values=editor_lista, state="readonly")
        editor_combobox.pack()

        filter_button = Button(window, text="Filtrar", command=lambda: self.show_list_editor(editor.get()))
        filter_button.pack(pady=10)
            
    def show_list_editor(self, e):
        # Crea una ventana secundaria para mostrar la lista de juegos por editor
        window = Toplevel(self.master)
        window.title(f"Lista de Juegos (Editor: {e}")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_editor_treeview(tree)

        # Inserta los datos en el Treeview
        lista_editor = show_editor(e)
        for juego in lista_editor:
            row = (
                juego[0], juego[1], juego[2]
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")

    def setup_editor_treeview(self, tree):
        columns = ("Rank", "Name", "Publisher")

        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=70)
            
        
def run_gui():
    root = Tk()
    app = Ventana(root)
    root.mainloop()
