from from_phonebook import phonebook as data

def find_contact(contact, area):
    result = []
    for i in data():
        if i[area] == contact:
            result.append(i)
    if not result: return -1
    return result




if __name__ == '__main__':
    print(find_contact('Иванов'))
    print(find_contact('Иван', 'имя'))