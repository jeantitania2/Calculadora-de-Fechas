import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import pytz

class DateCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Fechas")

        # Frame para la calculadora de fechas
        self.date_frame = ttk.Frame(self.root, padding="10")
        self.date_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        self.label_date1 = ttk.Label(self.date_frame, text="Fecha 1 (YYYY-MM-DD):")
        self.label_date1.grid(row=0, column=0)
        self.entry_date1 = ttk.Entry(self.date_frame)
        self.entry_date1.grid(row=0, column=1)

        self.label_date2 = ttk.Label(self.date_frame, text="Fecha 2 (YYYY-MM-DD):")
        self.label_date2.grid(row=1, column=0)
        self.entry_date2 = ttk.Entry(self.date_frame)
        self.entry_date2.grid(row=1, column=1)

        self.button_calculate = ttk.Button(self.date_frame, text="Calcular Diferencia", command=self.calculate_difference)
        self.button_calculate.grid(row=2, columnspan=2)

        self.label_result = ttk.Label(self.date_frame, text="")
        self.label_result.grid(row=3, columnspan=2)

        # Frame para la hora mundial
        self.time_frame = ttk.Frame(self.root, padding="10")
        self.time_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.label_timezone = ttk.Label(self.time_frame, text="Selecciona Zona Horaria:")
        self.label_timezone.grid(row=0, column=0)

        self.timezones = pytz.all_timezones
        self.selected_timezone = tk.StringVar(value='UTC')
        self.combobox_timezone = ttk.Combobox(self.time_frame, textvariable=self.selected_timezone, values=self.timezones)
        self.combobox_timezone.grid(row=0, column=1)
        self.combobox_timezone.bind("<<ComboboxSelected>>", self.update_time)

        self.label_world_time = ttk.Label(self.time_frame, text="")
        self.label_world_time.grid(row=1, columnspan=2)

        self.update_time()

    def calculate_difference(self):
        date1_str = self.entry_date1.get()
        date2_str = self.entry_date2.get()
        try:
            date1 = datetime.strptime(date1_str, "%Y-%m-%d")
            date2 = datetime.strptime(date2_str, "%Y-%m-%d")
            difference = abs((date2 - date1).days)
            self.label_result.config(text=f"Diferencia: {difference} días")
        except ValueError:
            self.label_result.config(text="Formato de fecha incorrecto. Usa YYYY-MM-DD.")

    def update_time(self, event=None):
        timezone = pytz.timezone(self.selected_timezone.get())
        world_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        self.label_world_time.config(text=f"Hora Mundial: {world_time}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DateCalculatorApp(root)
    root.mainloop()
