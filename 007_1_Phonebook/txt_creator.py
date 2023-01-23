import imprt as im

def import_to_txt():
    with open('Phonebook.txt', 'a') as file:
        file.write(im.GetUserData())