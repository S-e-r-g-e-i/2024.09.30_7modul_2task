# Позиционирование в файле


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for i in range(0, len(strings)):
        strings_positions.update({(i + 1, file.tell()): strings[i]})
        file.write(f'{strings[i]}\n')
    file.close()
    return (strings_positions)


# Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)