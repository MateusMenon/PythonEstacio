import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora de IMC")
        
        # Centralizar a janela
        self.center_window(250, 150)  # Tamanho da janela 
        
        # Desabilitar redimensionamento
        self.window.resizable(False, False)
        
        # Adicionando os elementos da interface
        self.create_widgets()
        
    def create_widgets(self):
        # Rótulos para altura e peso
        self.height_label = tk.Label(self.window, text="Altura (m):")
        self.height_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.weight_label = tk.Label(self.window, text="Peso (kg):")
        self.weight_label.grid(row=1, column=0, padx=10, pady=5)
        
        # Entradas para altura e peso
        self.height_entry = tk.Entry(self.window)
        self.height_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.weight_entry = tk.Entry(self.window)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Botão para calcular IMC
        self.calculate_button = tk.Button(self.window, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Rótulo para exibir o resultado do IMC
        self.result_label = tk.Label(self.window, text="Seu IMC: ")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"Seu IMC: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")
        
    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        
        self.result_label.config(text=f"Seu IMC: {bmi:.2f} ({category})")
    
    def center_window(self, width, height):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.window.geometry(f'{width}x{height}+{x}+{y}')

if __name__ == "__main__":
    app = BMICalculator()
    app.window.mainloop()
