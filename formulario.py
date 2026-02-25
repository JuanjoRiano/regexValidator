import tkinter as tk
from tkinter import messagebox
from validacion import Validacion

BG_VENTANA    = "#f0f4f8"
BG_HEADER     = "#1a3c5e"
BG_PANEL      = "#ffffff"
BG_CAMPO      = "#f7f9fc"
BG_ERROR      = "#fff0f0"
BG_OK         = "#f0fff4"
BD_ERROR      = "#e05252"
BD_OK         = "#2ecc71"
COLOR_TITULO  = "#ffffff"
COLOR_LABEL   = "#2d3748"
COLOR_HINT    = "#a0aec0"
COLOR_ERROR   = "#c0392b"
COLOR_OK      = "#27ae60"
BTN_REG       = "#1a3c5e"
BTN_LIMP      = "#718096"


class FormularioVehiculo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de Vehículo")
        self.configure(bg=BG_VENTANA)
        self.resizable(True, True)
        self.minsize(600, 700)
        ancho, alto = 700, 790
        x = (self.winfo_screenwidth()  - ancho) // 2
        y = (self.winfo_screenheight() - alto)  // 2
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
        self._construir_ui()

    def _construir_ui(self):
        # Encabezado
        header = tk.Frame(self, bg=BG_HEADER, pady=18)
        header.pack(fill="x")
        tk.Label(header, text="Registro de Vehículo",
                 bg=BG_HEADER, fg=COLOR_TITULO,
                 font=("Segoe UI", 18, "bold")).pack()
        tk.Label(header,
                 text="Complete el formulario — todos los campos son obligatorios",
                 bg=BG_HEADER, fg="#90aec8",
                 font=("Segoe UI", 9)).pack(pady=(2, 0))

        # Contenedor
        cont = tk.Frame(self, bg=BG_VENTANA, padx=30, pady=20)
        cont.pack(fill="both", expand=True)

        panel = tk.Frame(cont, bg=BG_PANEL, relief="solid", bd=1)
        panel.pack(fill="both", expand=True)
        panel.columnconfigure(0, weight=1)
        panel.columnconfigure(1, weight=1)
        for r in range(1, 7):
            panel.rowconfigure(r, weight=1)

        self.vars    = {}
        self.entries = {}
        self.err_lbl = {}

        self._seccion(panel, "Datos del Vehículo", row=0)

        vehiculo = [
            ("Placa",        "placa",   "ABC123 o ABC12D",            1, 0),
            ("Marca",        "marca",   "Ej: Chevrolet",               1, 1),
            ("Modelo (año)", "modelo",  "Entre 1900 y 2026",           2, 0),
            ("Color",        "color",   "Ej: Rojo",                    2, 1),
            ("N° de Chasis", "chasis",  "17 caracteres alfanuméricos", 3, 0),
            ("N° de Motor",  "noMotor", "Alfanumérico",                3, 1),
        ]
        for args in vehiculo:
            self._campo(panel, *args)

        self._seccion(panel, "Datos del Propietario", row=4)

        propietario = [
            ("Cédula",             "cedula",   "7–10 dígitos",          5, 0),
            ("Nombre completo",    "nombre",   "Solo letras y espacios",5, 1),
            ("Correo electrónico", "correo",   "usuario@dominio.com",   6, 0),
            ("Teléfono",           "telefono", "10 dígitos",            6, 1),
        ]
        for args in propietario:
            self._campo(panel, *args)

        bf = tk.Frame(panel, bg=BG_PANEL, pady=16)
        bf.grid(row=7, column=0, columnspan=2, sticky="ew", padx=20)

        tk.Button(bf, text="✔  Registrar Vehículo",
                  command=self._registrar,
                  bg=BTN_REG, fg="white", activebackground="#0f2a45",
                  font=("Segoe UI", 10, "bold"),
                  relief="flat", cursor="hand2",
                  padx=20, pady=9).pack(side="left", padx=(0, 10))

        tk.Button(bf, text="↺  Limpiar",
                  command=self._limpiar,
                  bg=BTN_LIMP, fg="white", activebackground="#4a5568",
                  font=("Segoe UI", 10),
                  relief="flat", cursor="hand2",
                  padx=20, pady=9).pack(side="left")

        tk.Label(self,
                 text="Validación con Expresiones Regulares · Python + Tkinter",
                 bg=BG_VENTANA, fg=COLOR_HINT,
                 font=("Segoe UI", 8)).pack(pady=(0, 8))

    def _seccion(self, parent, texto, row):
        f = tk.Frame(parent, bg="#e8f0f7", pady=6)
        f.grid(row=row, column=0, columnspan=2, sticky="ew")
        tk.Label(f, text=texto, bg="#e8f0f7", fg=BG_HEADER,
                 font=("Segoe UI", 9, "bold"), padx=14).pack(anchor="w")

    def _campo(self, parent, etiqueta, clave, hint, fila, col):
        cell = tk.Frame(parent, bg=BG_PANEL, padx=14, pady=6)
        cell.grid(row=fila, column=col, sticky="nsew")

        tk.Label(cell, text=etiqueta, bg=BG_PANEL, fg=COLOR_LABEL,
                 font=("Segoe UI", 9, "bold"), anchor="w").pack(fill="x")

        var = tk.StringVar()
        self.vars[clave] = var

        entry = tk.Entry(cell, textvariable=var,
                         bg=BG_CAMPO, fg="#2d3748",
                         insertbackground=BG_HEADER,
                         font=("Segoe UI", 10),
                         relief="solid", bd=1)
        entry.pack(fill="x", ipady=6)
        self.entries[clave] = entry

        tk.Label(cell, text=hint, bg=BG_PANEL, fg=COLOR_HINT,
                 font=("Segoe UI", 7), anchor="w").pack(fill="x")

        err = tk.Label(cell, text="", bg=BG_PANEL, fg=COLOR_ERROR,
                       font=("Segoe UI", 7, "italic"), anchor="w")
        err.pack(fill="x")
        self.err_lbl[clave] = err

    _REGLAS = {
        "placa":    (Validacion.validar_placa,    "Formato inválido. Use ABC123 o ABC12D"),
        "marca":    (Validacion.validar_marca,    "Solo letras y espacios"),
        "modelo":   (Validacion.validar_modelo,   "Año válido entre 1900 y 2026"),
        "color":    (Validacion.validar_color,    "Solo letras y espacios"),
        "chasis":   (Validacion.validar_chasis,   "Exactamente 17 caracteres alfanuméricos"),
        "noMotor":  (Validacion.validar_noMotor,  "Solo caracteres alfanuméricos"),
        "cedula":   (Validacion.validar_cedula,   "Entre 7 y 10 dígitos numéricos"),
        "nombre":   (Validacion.validar_nombre,   "Solo letras y espacios"),
        "correo":   (Validacion.validar_correo,   "Formato: usuario@dominio.com"),
        "telefono": (Validacion.validar_telefono, "Exactamente 10 dígitos"),
    }

    def _registrar(self):
        todo_valido = True

        for clave, (fn, msg) in self._REGLAS.items():
            valor = self.vars[clave].get()
            entry = self.entries[clave]
            err   = self.err_lbl[clave]

            if fn(valor):
                entry.config(bg=BG_OK)
                err.config(text="✔ Correcto", fg=COLOR_OK)
            else:
                entry.config(bg=BG_ERROR)
                err.config(text=f"⚠ {msg}", fg=COLOR_ERROR)
                todo_valido = False

        if todo_valido:
            messagebox.showinfo(
                "Registro exitoso",
                "¡El vehículo fue registrado correctamente!\n"
                "Todos los campos son válidos."
            )
            self._limpiar()

    def _limpiar(self):
        for clave in self.vars:
            self.vars[clave].set("")
            self.entries[clave].config(bg=BG_CAMPO)
            self.err_lbl[clave].config(text="")


# ══════════════════════════════════════════
if __name__ == "__main__":
    app = FormularioVehiculo()
    app.mainloop()