name = input("Enter your name: ")

#put name in lowercase for translation
name = name.lower()

letter_translation = {
    'a': 'ka',
    'b': 'zu',
    'c': 'mi',
    'd': 'te',
    'e': 'ku',
    'f': 'lu',
    'g': 'ji',
    'h': 'ri',
    'i': 'ki',
    'j': 'zu',
    'k': 'me',
    'l': 'ta',
    'm': 'rin',
    'n': 'to',
    'o': 'mo',
    'p': 'no',
    'q': 'ke',
    'r': 'shi',
    's': 'ari',
    't': 'chi',
    'u': 'do',
    'v': 'ru',
    'w': 'me',
    'x': 'na',
    'y': 'fu',
    'z': 'z'
    }

j_name = ''
for letter in name:
    if letter in letter_translation.keys():
        j_name = j_name + letter_translation.get(letter)
    else:
        j_name = j_name + letter

j_name = j_name.title()

print(f"You name in Japanese is {j_name}")
