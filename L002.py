"""Задача заключается в том, чтобы написать функцию,
 которая будет принимать слово и возвращать строку,
 в которой каждую букву этого слова будет представлена с
 помощью соответствующего кода из НАТО-фонетического алфавита.
 https://www.codewars.com/kata/54530f75699b53e558002076  в сщвуцфкы не работает!!!

 """


# NATO фонетический алфавит (словарь)
NATO_ALPHABET = {
    'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
    'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett',
    'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
    'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
    'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray', 'y': 'Yankee', 'z': 'Zulu'
}

def nato(word):
    # Преобразуем все буквы в нижний регистр и находим их НАТО-коды
    return ' '.join(NATO_ALPHABET[char.lower()] for char in word)
