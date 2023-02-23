import os
from data_create import name_data, surname_data, phone_data, adress_data

file_name = "data.txt"

def print_data():
    if os.path.exists(file_name):
        print("Вывод данных из файла: ")
        with open(file_name, "r", encoding= "utf - 8") as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print("Файла не существует!!!")


def input_data():
    print("Введите данные для записи в файл: ")
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    with open(file_name, "a", encoding= "utf - 8") as file:
        file.write(f"{name}; {surname}; {phone}; {adress}; \n")
        
def filter_data(filter_string):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf - 8")as file:
            list_data = file.readlines()
            if ";" in filter_string:
                list_filter = filter_string.split("; ")
            else:
                list_filter = [filter_string]
            is_found = False
            for element in list_data:
                temp_record = element.split("; ")
                count = 0
                for record in temp_record:
                    for element_filter in list_filter:
                        if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
                            count += 1        
                if count == len(list_filter):
                    print(element)
                    is_found = True
        if not is_found:
            print("Таких записей не найдено!")
    else:
        print("Файла не существует!!!")


def change_data(filter_string):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf - 8") as file:
            lines = file.readlines()
        with open(file_name, "w", encoding="utf - 8") as file:
            for line in lines:
                element = line.split("; ")
                for record in element:
                    if record == element[0]:
                        count = 0
                    if filter_string.lower() in record.lower() and len(filter_string.lower()) == len(record.lower()):
                        print(f"Изменить контактные данные:  {line}")
                        print("""Введите:
        1 - Для изменения данных
        2 - Для удаления данных
        3 - Для пропуска""")
                        choice = int(input("Введите номер команды: "))
                        while choice < 1 or choice > 3:
                            print("Введён некорректный номер команды: ")
                            choice = int(input("Введите номер команды: "))
                        if choice == 1:
                            input_data()
                            break
                        elif choice == 2:
                            break
                    count += 1
                    if count == len(line.split()):
                        with open(file_name, "a", encoding="utf - 8") as file:
                            file.write(line)
    else:
        print("Файла не существует!!!")
