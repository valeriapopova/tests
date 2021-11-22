documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people():
    d_number = input('Введите номер документа:')
    for document in documents:
        if document['number'] == d_number:
            return document['name']
    else:
        return 'Неверный номер'
    # people()


def shelf():
    doc_number = input('Введите номер документа:')
    for dir, directory in directories.items():
        if doc_number in directory:
            return dir
    else:
        return 'Неверный номер'
    # shelf()


def doc_list():
    docs = [f"{doc['type']}, {doc['number']}, {doc['name']}" for doc in documents]
    return docs
    # doc_list()


def add_doc():
    add1 = input('Введите тип документа:')
    add2 = input('Введите номер документа:')
    add3 = input('Введите имя владельца:')
    add4 = input('Введите номер полки:')
    documents.append({'type': add1, 'number': add2, 'name': add3})

    if add4 in directories.keys():
        directories[add4].append(add2)
        return documents, directories
    else:
        return 'Такой полки не существует!'


# add_command()

def delete_doc():
    x = input('Введите номер документа:')
    for doc in documents:
        if doc['number'] == x:
            doc['number'] = 'удалён'
    for dic, dic1 in directories.items():
        if x in dic1:
            dic1.remove(x)
            break
    else:
        return 'Несуществующий документ!'
    return documents, directories


def add_new_shelf():
    add_shelf = input('Введите номер полки:')
    for dir,dir2 in directories.items():
        if add_shelf in dir:
            return 'Такая полка уже существует'
    else:
        directories[add_shelf] = []
        return directories


def move(moving_doc, new_shelf):
    if new_shelf not in directories.keys():
        return 'Ошибка: неверный номер полки'
    for dic2, dic3 in directories.items():
        if moving_doc in dic3:
            dic3.remove(moving_doc)
            directories[new_shelf].append(moving_doc)
            return directories
    else:
        return 'Ошибка: неверный номер документа'


def secretary():
    while True:
        command = input('Введите команду:')
        if command == 'p':
            print(people())
        elif command == 's':
            print(shelf())
        elif command == 'l':
            print(doc_list())
        elif command == 'a':
            print(add_doc())
        elif command == 'd':
            print(delete_doc())
        elif command == 'as':
            print(add_new_shelf())
        elif command == 'm':
            m = input('Введите номер документа:')
            s = input('Введите номер полки:')
            print(move(m, s))
        else:
            print('Программа завершена')


# secretary()