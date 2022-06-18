from unittest import result


def main_menu():
    print('-'*40)
    print('Выберите команду:\n1-вывести телефонную книгу в терминал\n2-найти контакт\n3-создать новый контакт\nлюбая другая - выход из программы')
    print('-'*40)
    try:
        result_request = int(input())
    except:
        return exit()
    return result_request


def get_find():
    param = input('По какому параметру будем искать? имя, фамилия или номер\n_')
    value = input('Что будем искать? \n_')
    return (value, param)

def action_contact():
    print('1 - изменить контакт\n2 - удалить контакт\n3 - поделиться контактом\n0 - выйти в главное меню\nлюбая другая - выход из программы')
    print('Выберите дальнейшее действие с контактом: ')
    try:
        result_request = int(input())
    except:
        return exit()
    return result_request if 0 <= result_request <= 3 else exit()

def select_contact():
    return int(input('выберите контакт:'))

def print_selected_contact(selected_contact):
    print(f'выбран контакт: {selected_contact[1]}, {selected_contact[2]}, {selected_contact[3]}, {selected_contact[4]}\n'+'-'*40)

def print_report_delete_contact(contact):
    print(f'контакт: {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]} удален\n'+'-'*40)

def print_report_change_contact(contact):
    print(f'контакт изменен на: {contact[1]}, {contact[2]}, {contact[3]}, {contact[4]}\n'+'-'*40)
   

if __name__ == '__main__':
    print(main_menu())
    print(get_find())
    print(action_contact())
