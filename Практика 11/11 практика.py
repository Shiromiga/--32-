import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

# Создание вкладок
root = tk.Tk()
root.geometry("1000x500")
root.title("Игнатьев Дмитрий Сергеевич")

tab_control = ttk.Notebook(root) # Виджет с несколькими вкладками
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='1 вкладка')#Добавление вкладок
tab_control.add(tab2, text='2 вкладка')
tab_control.add(tab3, text='3 вкладка')

tab_control.pack(expand=True, fill='both') # Расщирене на полную длинну родительского контейнера  и заполнение всего объёма



def calculate():
    num1 = float(entry1.get())#Переменная, принимающая в себя число
    num2 = float(entry2.get())
    operation = operation_var.get()
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    result_label.config(text="Ответ: " + str(result))
# Вкладка с калькулятором
entry1 = tk.Entry(tab1)# Принятие одного числа
entry1.pack()
entry2 = tk.Entry(tab1)# Принятие вторго числа
entry2.pack()
operation_var = tk.StringVar(tab1) #Отслеживание операций
operation_var.set('+')
operation_menu = tk.OptionMenu(tab1, operation_var, '+', '-', '*', '/') #Выпадающее меню с операциями
operation_menu.pack()
calculate_button = tk.Button(tab1, text="Подсчёт", command=calculate)
calculate_button.pack()
result_label = tk.Label(tab1, text="Результат: ")
result_label.pack()

def show_selected_checkbox():
    if checkbox1_var.get() == 1:
        messagebox.showinfo("Выбор", "Вы выбрали первый вариант")
    elif checkbox2_var.get() == 1:
        messagebox.showinfo("Выбор", "Вы выбрали второй вариант ")
    else checkbox3_var.get() == 1:
        messagebox.showinfo("Выбор", "Вы выбрали третий вариант ")
# Вкладка с чекбоксами
checkbox1_var = tk.IntVar()
checkbox2_var = tk.IntVar()
checkbox3_var = tk.IntVar()
checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=checkbox1_var) #Флвжок с выбором чекбокса
checkbox1.pack()
checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=checkbox2_var) #аналогично
checkbox2.pack()
checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=checkbox3_var) #аналогично
checkbox3.pack()
show_selected_button = tk.Button(tab2, text="Показать выбор", command=show_selected_checkbox) #Кнопка показывающая выбор
show_selected_button.pack()
def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text = file.read()
        text_box.delete(1.0, tk.END) #Удаляет все, с начала до конца
        text_box.insert(tk.END, text) #Вставляет текст из файла


# Вкладка с текстом
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

text_box = tk.Text(tab3)
text_box.pack()

root.mainloop()

