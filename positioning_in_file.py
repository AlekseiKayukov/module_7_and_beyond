def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    number_row = 0

    for string in strings:
        number_row += 1
        file_tell = file.tell()
        file.write(string + "\n")
        strings_positions[number_row, file_tell] = string

    return  strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)