""" 
    Function open_file()
    Should receive the file_name.extension that contains the list of names to be formatted.
"""
def open_file(file_name, file_encoding):
    file = open(file_name, mode = 'r', encoding = file_encoding)
    names_list = file.read().split('\n')
    file.close()
    corrects_names = []
    for name in names_list:
        corrects_names.append(set_capitalize(name.strip()))
    
    return corrects_names
"""
    Finction set_capitalize()
    Should receive the string of original name for capitalize formated
"""
def set_capitalize(original_name):
        exceptions_words   = [' Da ', ' De ', ' Dos ', ' Do ']
        correct_name = [ name.capitalize() for name in original_name.split()]
        correct_name =  ' '.join(correct_name)
        correct_name = set_exceptions_words(correct_name, exceptions_words)
        return correct_name
"""
    Function set_exceptions_words()
    Should receive the string of original name and list of exceptions words that will not be capitalized formatted
"""        
def set_exceptions_words(original_name, exceptions_words):
    correct_name = original_name
    for words in exceptions_words:
        correct_name = correct_name.replace(words, words.lower())
    return correct_name

"""
    Function save_file_names()
    Should receive the name_new_file.extension for to save a list names formatted,
    a list for names formatted and a file encoding
"""
def save_file_names(file_name, list_names, file_encoding):
    new_file = open(file_name, mode = 'w', encoding = file_encoding)
    names = "\n".join(list_names)
    new_file.write(names)
    

save_file_names('nomes_corretos.txt', open_file('names_list.txt', 'utf-8-sig'), 'utf-8-sig')