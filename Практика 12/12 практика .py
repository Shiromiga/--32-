import tkinter as tk
import requests
import json

def get_repository_info():
    repo_name = entry.get() #Название репозитоориря , получаемое от человека
    url = f'https://api.github.com/repos/{repo_name}' #Полная урл ссылка на репозиторий , форматированная строка Ф
    response = requests.get(url) #Получение данных по урл
    data = response.json() #Преобразование в json

    # Создание словаря ключ зачение, содержащий в себе данные из data
    info = {
        'company': data.get('company', 'N/A'),
        'created_at': data.get('created_at', 'N/A'),#Извлечение определённой информации из data
        'email': data.get('email', 'N/A'),
        'id': data.get('id', 'N/A'),
        'name': data.get('name', 'N/A'),
        'url': data.get('url', 'N/A')
    }

    with open('repository_info.json', 'w') as file:
        json.dump(info, file, indent=4)


# Создание графического интерфейса
root = tk.Tk()
root.title('Игнатьев_Дмитрий_Сергеевич')

label = tk.Label(root, text='Введите название репозитория:')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Получить данныЕ', command=get_repository_info)
button.pack()

label_info = tk.Label(root, text='')
label_info.pack()

root.mainloop()
