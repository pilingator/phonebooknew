import csv
import from_phonebook 
from interface import print_report_change_contact as report

def change_contact(befo_id, after_id):
    phonebook = from_phonebook.phonebook()
    with open("phonebook.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        for element in phonebook:
            writer.writerow(after_id if element == befo_id else element)
    report(after_id)



if __name__ == '__main__':
    change_contact(['3', 'Иван', 'Петров', '891234567877', ''], ['3', 'Иванушка', 'Петров', '891234567877', ''])
    print(from_phonebook.phonebook())
