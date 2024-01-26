from PIL import Image, ImageTk
from pandasgui import show
from tkinter import ttk, Tk, Button, Toplevel, Radiobutton, Label, Entry, StringVar, Canvas

from app.crud.operaciones import *
from app.db.consultas_db import *
from app.estructura.catalogo import Juegos
from app.pandas.consultas_pd import listado_pandas
from app.validaciones.validaciones import validar_year_par


class Ventana:
    def __init__(self, master):
        """_summary_
        Funsion que se encarga de iniciar la interfaz principal
        Args:
            master = la ventana (_type_): _description_
        """
        self.master = master
        self.master.title("Video Game Sales")
        self.master.resizable(0, 0)
        self.master.minsize(0, 0)
        self.master.configure(bg="#26D9D9")
        self.master.geometry("200x200")
        self.var = StringVar()
        self.var.set("0")
        self.master.eval(f'tk::PlaceWindow {str(self.master)} center')

        image = Image.open('imagenes/LucaSteam_icon.png')
        tk_image = ImageTk.PhotoImage(image)
        self.master.tk.call('wm', 'iconphoto', self.master._w, tk_image)
        # Crear un Canvas que ocupe toda la ventana
        self.canvas = Canvas(self.master, width=200, height=200)
        self.canvas.pack()

        # Definir los colores para el degradado
        # color1 = "#FF9EA0"  # Primer color
        # color2 = "#87BAE1"  # Segundo color
        color1 = "#E95985"  # Segundo color
        color2 = "#26D9D9"  # Segundo color

        # Dibujar el degradado
        for i in range(200):
            # Calcular el color en cada posición vertical
            r = int((1 - i / 200) * int(color1[1:3], 16) + (i / 200) * int(color2[1:3], 16))
            g = int((1 - i / 200) * int(color1[3:5], 16) + (i / 200) * int(color2[3:5], 16))
            b = int((1 - i / 200) * int(color1[5:7], 16) + (i / 200) * int(color2[5:7], 16))
            color = f"#{r:02X}{g:02X}{b:02X}"

            # Dibujar una línea vertical del color correspondiente
            self.canvas.create_line(0, i, 200, i, fill=color, width=1)
        # Titulo de la ventana principal
        titulo_init = Label(self.master, text="Proyecto LucasSteam ©", bg="#D2678E", font=('Arial', 12, 'bold'))
        # Texto interrogativo
        radio_button_l = Label(self.master, text="¿De donde quieres ver los datos?", bg="#BA7799")
        # Radio buttons
        radio_button_lista = Radiobutton(self.master, bg="#859AAF", variable=self.var, value="0", highlightthickness=0)
        radio_button_db = Radiobutton(self.master, bg="#859AAF", variable=self.var, value="1", highlightthickness=0)
        radio_button_panda = Radiobutton(self.master, bg="#859AAF", variable=self.var, value="2", highlightthickness=0)
        # Boton para buscar basado en la celeccion
        show_button_buscar = Button(self.master, text="Buscar", width=8, command=lambda: self.setup_main_window(
            self.var.get()))  # Boton que se encarga de enviale un valor basado en la seleccion

        # Texto identificativo de cada radio button
        label_lista = Label(self.master, text="Lista", bg="#998DA7")
        label_db = Label(self.master, text="DB", bg="#998DA7")
        label_panda = Label(self.master, text="Panda", bg="#998DA7")

        # sistema de posiciones del titulo y los radio button 
        titulo_init.place(x=5, y=10)
        radio_button_l.place(x=20, y=40)
        radio_button_lista.place(x=30, y=90)
        radio_button_db.place(x=90, y=90)
        radio_button_panda.place(x=150, y=90)
        show_button_buscar.place(x=70, y=130)

        # sistema de posicionamienton de los textos descriptivos
        label_lista.place(x=26, y=70)
        label_db.place(x=90, y=70)
        label_panda.place(x=143, y=70)

    def setup_main_window(self, var):
        """_summary_

        Args:
            var = variable (_type_): _description_
        """
        # interfaz de esta funsion
        self.root = Tk()
        self.root.title("Video Game Sales")
        self.root.resizable(0, 0)
        self.root.minsize(0, 0)
        self.root.configure(bg="#87BAE1")
        self.root.geometry("300x460")
        self.root.eval(f'tk::PlaceWindow {str(self.root)} center')  # Posiciona la ventana en el centro de la pantalla

        def canvas(ancho, alto):
            # Crear un Canvas que ocupe toda la ventana
            self.canvas = Canvas(self.root, width=ancho, height=alto)
            self.canvas.pack()

            # Definir los colores para el degradado
            # color1 = "#FF9EA0"  # Primer color
            # color2 = "#87BAE1"  # Segundo color
            color1 = "#E95985"
            color2 = "#26D9D9"

            # Dibujar el degradado
            for i in range(alto):
                # Calcular el color en cada posición vertical
                r = int((1 - i / alto) * int(color1[1:3], 16) + (i / alto) * int(color2[1:3], 16))
                g = int((1 - i / alto) * int(color1[3:5], 16) + (i / alto) * int(color2[3:5], 16))
                b = int((1 - i / alto) * int(color1[5:7], 16) + (i / alto) * int(color2[5:7], 16))
                color = f"#{r:02X}{g:02X}{b:02X}"

                # Dibujar una línea vertical del color correspondiente
                self.canvas.create_line(0, i, alto, i, fill=color, width=1)

        # sistema para mostrar los botones segun su seleccion
        if var == "0":
            self.root.geometry(
                "250x200")  # si cumple la condicional , cambiamos las dimenciones de la ventana ajustandoce a la cantyidad de votones que existan dentro la condicion
            canvas(250, 250)  # ajustamos las dimenciones del cambas tambien

            # titulo
            titulo_0 = Label(self.root, text="Proyecto LucasSteam ©", bg="#D2678E", font=('Arial', 12, 'bold'))

            # Botones
            insert_button = Button(self.root, text="Datos Manual", width=25, command=self.insert_data)
            show_button = Button(self.root, text="Mostrar Lista de Juegos", width=25, command=self.show_list)

            # sistema de posiciones de los botones y el titulo
            titulo_0.place(x=30, y=10)
            insert_button.place(x=35, y=70)
            show_button.place(x=35, y=110)

        elif var == "2":
            self.root.geometry(
                "180x180")  # si cumple la condicional , cambiamos las dimenciones de la ventana ajustandoce a la cantyidad de votones que existan dentro la condicion
            canvas(180, 200)  # ajustamos las dimenciones del cambas tambien
            titulo_2 = Label(self.root, text="Proyecto LucasSteam ©", bg="#D2678E", font=('Arial', 10, 'bold'))
            # Boton
            show_df_button = Button(self.root, text="Mostrar Juegos (Panda)", width=18, command=self.data_frame)

            # sistema de posicion de los botones
            titulo_2.place(x=10, y=10)
            show_df_button.place(x=23, y=80)

        elif var == "1":
            self.root.geometry(
                "250x500")  # si cumple la condicional , cambiamos las dimenciones de la ventana ajustandoce a la cantyidad de votones que existan dentro la condicion
            canvas(250, 500)  # ajustamos las dimenciones del cambas tambien
            # titulo de esta ventana 
            titulo_1 = Label(self.root, text="Proyecto LucasSteam ©", bg="#E95985", font=('Arial', 12, 'bold'))
            # Botones de esta ventana
            show_db_button = Button(self.root, text="Mostrar Lista de Juegos (DB)", width=25, command=self.show_list_db)
            show_xx = Button(self.root, text="Mostrar Juegos Siglo XX", width=25, command=self.show_list_xx)
            show_filt_genero_button = Button(self.root, text="Filtrar por género", width=25, command=self.insert_genero)
            update = Button(self.root, text="Update Juego", width=25, command=self.update)
            delete = Button(self.root, text="Delete Juego", width=25, command=self.delete)
            show_platform_button = Button(self.root, text="Juegos Nintendo", width=25, command=self.show_platform)
            show_par_button = Button(self.root, text="Juegos año par", width=25, command=self.show_year_par)
            show_media_button = Button(self.root, text="Juegos superior a la media EU", width=25,
                                       command=self.superior_a_media)
            show_max_vent_button_g = Button(self.root, text="Juegos más vendidos Global", width=25,
                                          command=self.mas_vendidos)
            show_max_vent_button_r = Button(self.root, text="Juegos más vendidos Regional", width=25,
                                          command=self.insert_region)
            show_editor_button = Button(self.root, text="Mostrar juegos por editor", width=25,
                                        command=self.insert_editor)

            # sistema de posiciones de los botones y el titulo
            titulo_1.place(x=30, y=10)
            show_db_button.place(x=35, y=45)
            show_xx.place(x=35, y=85)
            show_filt_genero_button.place(x=35, y=125)
            update.place(x=35, y=165)
            delete.place(x=35, y=205)
            show_platform_button.place(x=35, y=245)
            show_par_button.place(x=35, y=285)
            show_media_button.place(x=35, y=325)
            show_max_vent_button_g.place(x=35, y=365)
            show_max_vent_button_r.place(x=35, y=405)
            show_editor_button.place(x=35, y=445)

    def update(self):
        """_summary_

            interfaz que muetra los campos que pueden hacer la actualizacion de algun juego en la base de datos
        """
        window = Tk()
        window.title("Update Juegos")  # titulo
        window.resizable(0, 0)
        window.minsize(0, 0)
        window.configure(bg='#FF9EA0')
        window.geometry("250x250")

        # texto descriptivo
        label_id = Label(window, text="ID:", bg='#FF9EA0')
        label_id.place(x=5, y=20)

        # Etiquetas e inputs para la actualización de juegos
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
            """Función que envuelve la actualización de juegos."""
            try:
                ids = int(id_entry.get())
                update_juegos(ids, manual_name.get(), var_plataforma.get(), manual_years.get(),
                              manual_genero.get(), manual_editor.get())

            except ValueError:
                print("Error: Ingresa un número válido en el campo ID.")

        manual_button = Button(window, text="Update", bg="#00FFFF", command=update_juegos_wrapper)
        manual_button.place(x=100, y=220)

    def delete(self):
        """Muestra una interfaz para eliminar juegos."""
        self.confirmacion_dell = False
        self.window_del = Tk()
        self.window_del.title("Delete Juegos")
        self.window_del.resizable(0, 0)
        self.window_del.minsize(0, 0)
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
        """Elimina un juego después de la confirmación."""
        if not self.confirmacion_dell:
            print("Seguro que desea borrar este juego")
            self.confirmacion_dell = True
            return
        delete_juego(self.ident)

    def get_info_from_entry(self):
        """Obtiene información de un juego según el ID ingresado."""
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
        """Obtiene información de un juego dado su ID.

        Parameters:
            ident (int): El ID del juego.

        Returns:
            str: Información formateada del juego o un mensaje de error si no se puede obtener la información.
        """
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
        """Muestra una interfaz para insertar información de juegos en la base de datos."""
        window = Tk()
        window.title("Insert Juegos")
        window.resizable(0, 0)
        window.minsize(0, 0)
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
        """Muestra una interfaz para filtrar juegos por género."""
        window = Tk()
        window.title("Filtrar Juegos por Género")
        window.resizable(0, 0)
        window.minsize(0, 0)
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
        window.minsize(0, 0)
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
        window.minsize(0, 0)
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
        window.minsize(False, False)
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
        """Configura el Treeview con columnas y encabezados."""
        columns = ("Rank", "Name", "Platform", "Year", "Genre", "Publisher")

        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=60)  # aqui se ajusta el año de la tabla

    def setup_treeview_ventas(self, tree, region):
        """Configura el Treeview con columnas y encabezados."""
        columns = ("Rank", "Name", "Platform", "Year", "Publisher", region)

        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=60)  # aqui se ajusta el año de la tabla

    def setup_treeview_ventas_regional(self, tree, region):
        """Configura el Treeview con columnas y encabezados."""
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
        window.minsize(0, 0)
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
        """Muestra un DataFrame usando la librería pandas y lo visualiza en una ventana."""
        # Obtén los datos utilizando la función listado_pandas
        data = listado_pandas()

        # Utiliza la función show para visualizar el DataFrame en una ventana
        gui = show(data, title='Tabla de Datos Pandas')

    def show_platform(self):
        """Muestra una ventana secundaria con juegos desarrollados por Nintendo."""
        window = Toplevel(self.master)
        window.title("Juegos desarrollados por Nintendo")
        window.resizable(0, 0)
        window.minsize(0, 0)
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
        """Muestra una ventana secundaria con juegos lanzados en años pares."""
        window = Toplevel(self.master)
        window.title("Juegos lanzados en año par")
        window.resizable(0, 0)
        window.minsize(0, 0)
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
        """Muestra una ventana secundaria con juegos más vendidos a nivel global."""
        window = Toplevel(self.master)
        window.title("Juegos mas vendidos Global")
        window.resizable(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview_ventas(tree, region="V_Global")

        max_vent = show_max_venta()

        # Inserta los datos en el Treeview
        for juego in max_vent:
            row = (
                juego[0], juego[1], juego[2], juego[3],
                juego[4], juego[5]  # corregir
            )
            tree.insert("", "end", values=row)

        # Configuración del scrollbar vertical
        scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")

        tree.configure(yscrollcommand=scrollbar.set)

        # Empaqueta el Treeview en la ventana secundaria
        tree.pack(expand=True, fill="both")

    def superior_a_media(self):
        """Muestra una ventana secundaria con juegos superiores a la media en Europa."""
        window = Toplevel(self.master)
        window.title("Juegos superior a la media en Europa")
        window.resizable(0, 0)
        window.minsize(0, 0)
        window.configure(bg='#FF9EA0')

        # Creación del Treeview en la ventana secundaria
        tree = ttk.Treeview(window)
        self.setup_treeview_ventas(tree, region="V_EU")

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
        """Muestra una ventana para filtrar juegos por región."""
        window = Tk()
        window.title("Filtrar Juegos por Region")
        window.resizable(0, 0)
        window.minsize(0, 0)
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
        window.minsize(0, 0)
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
        """Muestra una ventana para filtrar juegos por editor."""
        window = Tk()
        window.title("Filtrar Juegos por Editor")
        window.resizable(0, 0)
        window.minsize(0, 0)
        window.configure(bg='#FF9EA0')
        window.geometry("200x100")

        editor_l = Label(window, text="Editor", bg='#FF9EA0')
        editor_l.pack()
        editor = StringVar(window)
        editor_lista = ["Unknown", "Nintendo", "Microsoft Game Studios", "Take-Two Interactive",
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
        window.minsize(0, 0)
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
        """Configura el Treeview con columnas y encabezados."""
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
