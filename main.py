import json
import datetime


# Функция для создания новой заметки
def create_note():
    note_id = input("Введите идентификатор заметки: ")
    note_title = input("Введите заголовок заметки: ")
    note_body = input("Введите текст заметки: ")
    note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": note_id,
        "title": note_title,
        "body": note_body,
        "date": note_date
    }

    return note


# Функция для сохранения заметки в формате JSON
def save_note(note):
    with open('notes.json', 'a') as file:
        json.dump(note, file)
        file.write('\n')


# Функция для чтения всех заметок
def read_notes():
    with open('notes.json', 'r') as file:
        for line in file:
            note = json.loads(line)
            print(f"Идентификатор: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата: {note['date']}")
            print()


# Функция для поиска заметки по идентификатору
def find_note():
    note_id = input("Введите идентификатор заметки: ")

    with open('notes.json', 'r') as file:
        for line in file:
            note = json.loads(line)
            if note['id'] == note_id:
                print(f"Идентификатор: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['body']}")
                print(f"Дата: {note['date']}")
                print()
                return

    print("Заметка не найдена.")


# Функция для удаления заметки по идентификатору
def delete_note():
    note_id = input("Введите идентификатор заметки: ")

    with open('notes.json', 'r') as file:
        notes = []
        for line in file:
            note = json.loads(line)
            if note['id'] != note_id:
                notes.append(note)

    with open('notes.json', 'w') as file:
        for note in notes:
            json.dump(note, file)
            file.write('\n')

    print("Заметка успешно удалена.")


# Функция для редактирования заметки по идентификатору
def edit_note():
    note_id = input("Введите идентификатор заметки: ")

    with open('notes.json', 'r') as file:
        notes = []
        for line in file:
            note = json.loads(line)
            if note['id'] == note_id:
                note_title = input("Введите новый заголовок заметки: ")
                note_body = input("Введите новый текст заметки: ")
                note_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                note['title'] = note_title
                note['body'] = note_body
                note['date'] = note_date

            notes.append(note)

    with open('notes.json', 'w') as file:
        for note in notes:
            json.dump(note, file)
            file.write('\n')

    print("Заметка успешно отредактирована.")


# Пользовательский интерфейс
while True:
    command = input("Введите команду (создать, прочитать, найти, удалить, редактировать), или 'выход' для завершения: ")

    if command == "создать":
        note = create_note()
        save_note(note)
        print("Заметка успешно создана.")
    elif command == "прочитать":
        read_notes()
    elif command == "найти":
        find_note()
    elif command == "удалить":
        delete_note()
    elif command == "редактировать":
        edit_note()
    elif command == "выход":
        break
    else:
        print("Неверная команда. Пожалуйста, попробуйте еще раз.")