from datetime import datetime
import json
import os


class Note:
    def __init__(self, header: str, text: str):
        self.id = None
        self.header = header
        self.text = text
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.note_dict = self.to_dict()

    def to_dict(self):
        return {
            "id": self.id,
            "header": self.header,
            "text": self.text,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M')
        }

    def update_text(self, new_text):
        self.text = new_text
        self.updated_at = datetime.now()


class Program:
    def __init__(self, path: str = 'Notes.json'):
        self.path = path
        self.notes = {}
        self.open_file()

    def open_file(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, 'r', encoding='UTF-8') as file:
                    data = json.load(file)
                    self.notes = data
            except json.JSONDecodeError:
                self.notes = {}

    def save_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            json.dump(self.notes, file, indent=4, ensure_ascii=False)

    def create_note(self, header, text):
        next_id = max(map(int, self.notes.keys()), default=0) + 1
        note = Note(header, text)
        note.id = next_id
        self.notes[next_id] = note.to_dict()
        self.save_file()
        print(f"Заметка с ID {note.id} создана.")

    def get_note_by_id(self, note_id):
        if str(note_id) in self.notes:
            note_data = self.notes[str(note_id)]
            return Note(note_data["header"], note_data["text"])
        else:
            return None

    def edit_note(self, note_id, header, text):
        if str(note_id) in self.notes:
            note_data = self.notes[str(note_id)]
            note_data["header"] = header
            note_data["text"] = text
            note_data["updated_at"] = datetime.now().strftime('%Y-%m-%d %H:%M')
            # self.save_file()
            print(f"Заметка с ID {note_id} отредактирована.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def delete_note_by_id(self, note_id):
        if str(note_id) in self.notes:
            del self.notes[str(note_id)]
            self.save_file()
            print(f"Заметка с ID {note_id} удалена.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def list_notes(self):
        for note_id, note_data in self.notes.items():
            print(f"ID: {note_id}; Заголовок: {note_data['header']}; Заметка: {note_data['text']}")
