"""
Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), 
распознает, преобразует и выводит на экран лексемы по определенному правилу. Лексемы разделены пробелами. Преобразование делать по возможности через словарь. 
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.

Вариант 26
Натуральные числа, начинающиеся с не менее чем 2 единиц. Вывести числа, меняя местами каждые две соседние цифры, разделяя их количеством нулей, 
равным количеству обработанных цифр в числе. Одинаковые цифры нулями не разделяются. Цифры максимального числа после преобразования вывести прописью.

ИСТбд-13 Фокин Даниил
"""

def is_number(lexeme):
    return lexeme.isdigit()

def convert_number_to_words(number):
    d_db = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять',}
    words = [d_db[digit] for digit in str(number)]
    result = ' '.join(words)
    return result

def process_number(number):
    global max_value
    e = 100
    digits = [int(digit) for digit in str(number)]
    swapped_digits = ''

    for i in range(0, len(digits)-1):
        if digits[i] == digits[i+1]:
            swapped_digits = swapped_digits + str(digits[i])
            print(digits, swapped_digits)
        else:
            swapped_digits = swapped_digits + str(int(digits[i+1])*e + int(digits[i]))
            e = e * 10
            digits[i],digits[i+1] = digits[i+1],digits[i]
            if len(digits) > i+2:
                if digits[i+1] != digits[i+2]:
                    swapped_digits = swapped_digits[:-1]
            print(digits, swapped_digits)
    swapped_digits = int(swapped_digits)
    if max_value < swapped_digits:
        max_value = swapped_digits

def process_lexeme(lexeme):
    if len(lexeme) > max_buffer_len:
        print('Лексема имеет длину больше 100 символов!','\nЛексема:',work_buffer,'\nПропускаем\n')
        return
    
    if is_number(lexeme):
        number = int(lexeme)
        if str(number).startswith('11'):
            process_number(number)

def tokenize_line(line):
    buffer = ''
    for char in line:
        if char not in razd:
            buffer += char
        elif buffer:
            yield buffer
            buffer = ''
    if buffer:
        yield buffer

max_buffer_len = 100 # максимальная длинна буфера
buffer_len = 1 # размер буфера чтения
work_buffer = '' # рабочий буфер
work_buffer_len = buffer_len # длина рабочего буфера
razd = [' ', ',', '.', ';', ':', '?', '!', '"']

max_value = float('-inf')

with open('text.txt', encoding='utf-8') as file:
    lexeme_found = False
    for line in file:
        tokens = tokenize_line(line)
        for token in tokens:
            process_lexeme(token)
        work_buffer = ''
        lexeme_found = True

if lexeme_found:
    if max_value != float('-inf'):
        print('\nОтвет:', convert_number_to_words(max_value))
    else:    
        print('\nЛексем в файле не осталось или лексемы не удовлетворяют условию (в данном случае проверьте файл и(или) замените *.txt на другой). \nПрограмма завершает работу.')



# with open('text.txt', encoding='utf-8') as file:
#     buffer = file.read(buffer_len)
#     lexeme_found = False
#     if not buffer:
#         print('\nФайл text.txt в директории проекта пустой. \nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.')
#     while buffer:
#         if not buffer:
#             break
#         while buffer not in razd:
#             work_buffer += buffer
#             buffer = file.read(buffer_len)
#             if not buffer:
#                 break
#         process_lexeme(work_buffer)
#         work_buffer = ''
#         buffer = file.read(buffer_len)
#         lexeme_found = True