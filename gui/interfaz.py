from tkinter import ttk, Tk, Button, Toplevel, Label, Entry, StringVar
from app.estructura.catalogo import Juegos
from app.crud.operaciones_db import listar_juegos_db
from app.estructura.consultas_db import show_genere


class Ventana:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Game Sales")
        self.master.resizable(0, 0)
        self.master.configure(bg='#FF9EA0')
        self.master.geometry("300x250")
        self.master.eval(f'tk::PlaceWindow {str(self.master)} center')

        # Configuración de la ventana principal
        self.setup_main_window()

    def setup_main_window(self):
        # Botones en la ventana principal
        insert_button = Button(self.master, text="Datos Manual", command=self.insert_data)
        insert_button.pack(pady=10)

        show_button = Button(self.master, text="Mostrar Lista de Juegos", command=self.show_list)
        show_button.pack(pady=10)

        # show_xx = Button(self.master, text="Mostrar Juegos Siglo XX", command=Juegos.show_games_siglo_xx)
        # show_xx.pack(pady=10)

        show_db_button = Button(self.master, text="Mostrar Lista de Juegos (DB)", command=self.show_list_db)
        show_db_button.pack(pady=10)

        show_genero_button = Button(self.master, text="Mostrar Lista filtrada por género", command=self.insert_genero)
        show_genero_button.pack(pady=10)

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
        manual_button.place(x=10, y=50)

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


def run_gui():
    root = Tk()
    app = Ventana(root)
    root.mainloop()
