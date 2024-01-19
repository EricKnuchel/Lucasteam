from tkinter import ttk, Tk,Button, Toplevel
from app.estructura.catalogo import Juegos
from app.estructura.read_data_csv import leer_datos

class Ventana:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Game Sales")
        self.master.resizable(0, 0)
        self.master.configure(bg='#FF9EA0')
        self.master.geometry("300x400")

        # Datos de ejemplo
        self.data = [
            (1, 'Game1', 'Platform1', 2000, 'Genre1', 'Publisher1', 1.0, 0.5, 0.2, 0.1, 1.8),
            (2, 'Game2', 'Platform2', 2005, 'Genre2', 'Publisher2', 0.8, 0.3, 0.5, 0.2, 1.8),
        ]

        # Configuración de la ventana principal
        self.setup_main_window()

    def setup_main_window(self):
        # Botones en la ventana principal
        insert_button = Button(self.master, text="Insertar Datos", command=self.insert_data)
        insert_button.pack(pady=10)

        show_button = Button(self.master, text="Mostrar Lista de Juegos", command=self.show_list)
        show_button.pack(pady=10)
        
        show_xx = Button(self.master, text="Mostrar Juegos Siglo XX", command=Juegos.show_games_siglo_xx)
        show_xx.pack(pady=10)

    def insert_data(self):
        # Crea una ventana secundaria para mostrar la lista de juegos
        V_add_juego = Toplevel(self.master)
        V_add_juego.title("Añadir Juego")
        V_add_juego.resizable(0, 0)
        V_add_juego.configure(bg='#FF9EA0')
        # lógica para insertar datos
        self.data.append((len(self.data) + 1, f'Game{len(self.data) + 1}', 'Platform', 2200, 'Genre', 'Publisher', 1.0, 0.5, 0.2, 0.1, 1.8))
        print("Datos insertados")

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

    def setup_treeview(self, tree):
        columns = ("Rank", "Name", "Platform", "Year", "Genre", "Publisher")

        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=60) # aqui se ajusta el año de la tabla


def run_gui():
    root = Tk()
    app = Ventana(root)
    root.mainloop()
