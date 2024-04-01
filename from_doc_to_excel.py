from docx import Document
import pandas as pd
import os

#Функция открывает док, извлекает из него таблицы, если флаг тру, то берет оба столбца (нужно в первой итерации), возвращает датафрейм
def process_docx_file(file_path, flag=True):
    doc = Document(file_path)
    data = []
    for table in doc.tables:
        for row in table.rows:
            col1, col2 = row.cells
            if flag:
                data.append([col1.text, col2.text])  
            else:
                data.append([col2.text])  
    return pd.DataFrame(data)

input_folder = 'Data'
output_folder = 'Excel' #Сюда делаем копию каждого ДФ, мало ли

flag = True
dfs = []

#Проходим по всем докам в папке, забираем таблицу, пушим транспонированный столбец в ДФ и в список.
for file_name in os.listdir(input_folder):
    if file_name.endswith(".docx"):
        df = process_docx_file(os.path.join(input_folder, file_name), flag)
        df.T.to_excel(os.path.join(output_folder, file_name.replace(".docx", ".xlsx")), index=False) #По сути эта строка не нужна, мы на всякий случай сохраняем копию эксельки каждой отдельной таблицы
        flag = False  
        dfs.append(df.T)  

#Конкатинируем все Датафреймы и сохраняем в эксельку
result = pd.concat(dfs, ignore_index=True)
result.to_excel('итоговая_таблица.xlsx', index=False)
