import pandas as pd
import numpy as np

correctCols = ['№', 'Фамилия', 'Имя','Индивидуальный номер','Учреждение (организация)','Отдел','Адрес электронной почты','Тест:Тест текущего контроля успеваемости №1 (Значение)','Итого в категории «Тест 1» (Значение)','Тест:Тест текущего контроля успеваемости №2 (Значение)', 'Итого в категории «Тест 2» (Значение)', 'Тест:Тест текущего контроля успеваемости №3 (Значение)', 'Итого в категории «Тест 3» (Значение)', 'Задание:Контрольная работа №1 (Значение)', 'Задание:Контрольная работа №2 (Значение)','Задание:Контрольная работа №3 (Значение)','Итого в категории «Выполнение заданий» (Значение)','Посещаемость:Баллы за посещаемость (Значение)','Итого в категории «Посещаемость» (Значение)','Тест:Тест №1 (Значение)', 'Тест:Тест №2 (Значение)', 'Итого в категории «Тестирование» (Значение)', 'Тест:Тест для лекции №1 (Значение)', 'Тест:Тест для лекции №2 (Значение)', 'Тест:Тест для лекции №3 (Значение)', 'Итоговая оценка за курс (Значение)', 'Последние загруженные из этого курса']

def readEx(file):
    legExTable = pd.read_excel(io=file, engine='odf')
    table = legExTable.values
    #print("Excel file readed:" + str(table))
    return table

def numerateRows(table):
    rowNum = [i + 1 for i in range(0, len(table))]
    table = np.column_stack((rowNum, table))
    #print("Rows numerated:" + str(table))
    return table

def replaceCols(table, col1,col2):
    for i in range(0, len(table)):
        table[i][col1], table[i][col2] = table[i][col2], table[i][col1]
    #print("Cols replaced:" + str(table))
    return table

def genHtmlTable(table):
    htmlTable = pd.DataFrame(table, columns=correctCols)
    result = htmlTable.to_html(index=False)
    html_file = open("./index.html", "w")
    html_file.write(result)
    html_file.close()
    return 0

def main():
    table = readEx("data.ods")
    replaceCols(table, 0,1)
    table = numerateRows(table)
    genHtmlTable(table)


if __name__ == "__main__":
    main()