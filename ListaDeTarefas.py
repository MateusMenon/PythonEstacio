import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        # Centralizar a janela
        self.center_window(250, 400)  # Tamanho da janela
        
        # Desabilitar redimensionamento
        self.root.resizable(False, False)
        
        # Adicionando os elementos da interface
        self.create_widgets()

    def center_window(self, width, height):
        # Obtendo a largura e altura da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculando a posição x e y para centralizar a janela
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        # Definindo a geometria da janela
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        # Configurando a interface gráfica
        self.task_label = tk.Label(self.root, text="Digite uma nova tarefa:")
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, width=35)
        self.task_entry.pack(pady=5)

        self.add_task_button = tk.Button(self.root, text="Adicionar Tarefa", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(self.root, width=35, height=15)
        self.tasks_listbox.pack(pady=10)

        self.remove_task_button = tk.Button(self.root, text="Remover Tarefa", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")

    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para remover.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
