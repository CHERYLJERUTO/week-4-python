# read,write,modify system

# custom exception

class EmptyFileError(Exception):
    pass
# user input

try:

    # user input

    filename = input('enter the filename:')

    # open and read
    with open(filename, "r") as file:
        data = file.read()

    # check if empty
    if not data.strip():
        raise EmptyFileError('The file is empty!')

    # modification
    print('\nChoose a modification')
    print('1 - Convert to UPPERCASE')
    print('2 - Convert to lowercase')
    print('3 - Title case')
    print('4 - replace a word')
    choice = input('Enter choice(1/2/3/4):')

    # backend

    if choice == '1':
        modified = data.upper()
    elif choice == '2':
        modified = data.lower()
    elif choice == '3':
        modified = data.title()
    elif choice == '4':
        word = input('enter the word to replace:')
        new_word = input('enter new word')
        modified = data.replace(word, new_word)
    else:
        print("Invalid choice. No changes made.")
        modified = data

    # count words
    word_count = len(modified.split())

    # modified content to new file

    with open('output.txt', 'w') as outfile:
        outfile.write('Modified file content:\n' )
        outfile.write(modified + '\n\n')
        outfile.write(f"Word count: {word_count}\n")
        
    print('Changes saved to output.txt')

   
    # error handling
except FileNotFoundError:
    print('file not found')
except Exception as e:
    print('unexpected error',e)