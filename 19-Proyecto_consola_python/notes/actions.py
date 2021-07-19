import notes.note as noteModel

class Actions:

    def create(self, user):
        print(f'\nCreating note...')
        title = input('Write a title for the note ')
        content = input('Write the content for the note ')

        # user[0] is the index where id is saved in our database's table called notes
        note = noteModel.Note(user[0], title, content)
        save = note.saveOnDB()

        if save[0] >= 1:
            print(f'Note with title {note.title} successfully saved!')
        else:    
            print(f'Something went wrong. Note could not been saved!')

    def show(self, user):
        print(f'\nOkay! This are your notes, {user[1]}')   

        note = noteModel.Note(user[0])   
        notes = note.getNotes()

        for note in notes:
            print('\n**********************************************')
            print(f'|{note[2]}')
            print(f'|{note[3]}')
            print('**********************************************')

    def delete(self, user):
        title = input('Write the title of the note you want to delete: ')     
        note = noteModel.Note(user[0], title)
        delete = note.deleteNote()  
        
        if delete[0] >= 1:
            print(f'Note with title: {note.title} has been successfully deleted!')
        else:
            print(f'Something went wrong. Could not delete the note')    



            