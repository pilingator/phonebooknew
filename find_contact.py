from from_phonebook import phonebook as data

def find_contact(contact, area = 'фамилия'):
    result = []
    
    if area == 'имя':
        ind = 1
    elif area == 'фамилия':
        ind = 2
    elif area == 'номер':
        ind = 3
    else:
        ind = 2
    for i in data:
        if i[ind] == contact:
            result.append(i)
    else:
        ind = -1
    if not result: return -1
    return result




if __name__ == '__main__':
    print(find_contact('Иванов'))
    print(find_contact('Иван', 'имя'))