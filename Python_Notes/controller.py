from model import Program
import view
import text_ru as msg


def start():
    program = Program()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:  # показать все заметки
                program.list_notes()
            case 2:  # создать заметку
                header = input("Введите заголовок: ")
                text = input("Введите текст заметки: ")
                program.create_note(header, text)
            case 3:  # изменить заметку по ID
                note_id = input("Введите ID заметки для редактирования: ")
                if note_id.isdigit():
                    note_id = int(note_id)
                    header = input("Введите новый заголовок заметки: ")
                    text = input("Введите новый текст заметки: ")
                    program.edit_note(note_id, header, text)
                else:
                    view.print_message(msg.incorrect_format_error)
            case 4:  # удалить заметку
                note_id = input("Введите ID заметки для удаления: ")
                if note_id.isdigit():
                    note_id = int(note_id)
                    program.delete_note_by_id(note_id)
                else:
                    view.print_message(msg.incorrect_format_error)
            case 5:  # сохранить файл
                program.save_file()
                view.print_message(msg.successfully_saved)
            case 6:  # выход из программы
                view.print_message(msg.exit_program)
                break
