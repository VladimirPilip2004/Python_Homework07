from models import (view_info as vi, save_info1 as si1)

def input_info():
    Last_name = input("Введите Фамилию: ")    
    First_name = input("Введите Имя: ")
    Phone = input("введите номер: ")
    Info = input("Введите описание: ")
    return (Last_name, First_name, Phone, Info)

def choice_active():
    choice = int(input("Если вы хотите записать информацию в справочник введите - 1\nЕсли вы хотите считать информацию из справочника введите - 2\n"))
    if choice == 1:  
        
        si1()

    elif choice == 2:  vi()
    else: 
        print("Ошибка: Некорректный ввод! ")
      
