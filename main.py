from pprint import pprint
import re
# Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# 1. Выполните пункты 1-3 задания.
def name_format(contacts_list):
    for person in contacts_list:
        if len(person[0].split()) == 3:
            surname_splitted = person[0].split()
            person[0], person[1], person[2] = person[0].split()[0], surname_splitted[1], surname_splitted[2]
        if len(person[1].split()) == 2:
            name_splitted = person[1].split()
            person[1], person[2] = name_splitted[0], name_splitted[1]
        if len(person[0].split()) == 2:
            surname_splitted = person[0].split()
            person[0], person[1] = person[0].split()[0], surname_splitted[1]

    return contacts_list


def get_phone_numbers_format(contacts_list):
    pattern = r"(\+7|8)?\s?\(?(\d{3}?)\)?[-\s]?(\d{3})[-\s]?(\d{2})-?(\d{2})(\s?)\(?([доб.]{4})?\s?(\d{4})?\)?"
    substitution = r"+7(\2)\3-\4-\5\6\7\8"
    for person in contacts_list:
        person[5] = re.sub(pattern, substitution, person[5])

    return contacts_list


def Merge_duplicate_records(contacts_list):
    formatted_contacts_list = contacts_list.copy()
    for num, row in enumerate(contacts_list):
        for i in range(num + 1, len(contacts_list)):
            if row[0] == contacts_list[i][0]:
                formatted_contacts_list.remove(row)
                formatted_contacts_list.remove(contacts_list[i])
                zipped = zip(row, contacts_list[i])
                uniq = []
                for j in zipped:
                    if j[0] == j[1]:
                        uniq.append(j[0])
                    elif j[0] == '':
                        uniq.append(j[1])
                    elif j[1] == '':
                        uniq.append(j[0])
                formatted_contacts_list.append(uniq)
    return formatted_contacts_list


if __name__ == "__main__":
    name_format(contacts_list)
    get_phone_numbers_format(contacts_list)
    formatted_contacts_list = Merge_duplicate_records(contacts_list)

    # 2. Сохраните получившиеся данные в другой файл.
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(formatted_contacts_list)
