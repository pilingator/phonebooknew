import csv

phonebook = []
with open("phonebook.csv", encoding = 'utf-8') as file:
    reader = csv.reader(file, delimiter = "|")
    for id in reader:
        phonebook.append(id)