import tkinter as tk
from tkinter import messagebox

class Stopwatch:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Cronômetro")

        # Desabilitar redimensionamento
        self.window.resizable(False, False)

        # Configurar posição da janela no centro da tela
        window_width = 350
        window_height = 250
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.time_label = tk.Label(self.window, text="00:00:00", font=("Arial", 50))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(self.window, text="Iniciar", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.window, text="Parar", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(self.window, text="Resetar", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(pady=5)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        if not self.running:  # Redefinir apenas se o cronômetro não estiver em execução
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.update_time_display()  # Atualizar o rótulo de tempo com os valores redefinidos
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Aviso", "O cronômetro deve estar parado para ser resetado.")

    def update_time_display(self):
        formatted_time = f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        self.time_label.config(text=formatted_time)

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1

            self.update_time_display()
            self.window.after(1000, self.update_time)

if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.window.mainloop()
