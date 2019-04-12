def set_capitalize(original_name):
    if original_name:
        exceptions_words   = [' Da ', ' De ', ' Dos ', ' Do ']
        correct_name = [ name.capitalize() for name in original_name.split()]
        correct_name =  ' '.join(correct_name)
        correct_name = set_exceptions_words(correct_name, exceptions_words)
        return correct_name
    else:
        return '**informe um nome**'

def set_exceptions_words(original_name, exceptions_words):
    correct_name = original_name
    for words in exceptions_words:
        correct_name = correct_name.replace(words, words.lower())
    return correct_name

def init():
    while True:
        name = set_capitalize(input('Informe o nome: \n'))
        print(3 * '|', name, 3 * '|')
        print(35 * '-')

init()