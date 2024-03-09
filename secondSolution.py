def is_number(lexeme): return lexeme.isdigit()
def process_lexeme(lexeme):
    if not lexeme: return
    if len(lexeme) > max_buffer_len: return
    if is_number(lexeme):
        number = int(lexeme)
        if str(number).startswith('11'):
            process_number(number)
def process_number(number):
    global max_value; global lexeme; zero = 0
    digits = [int(digit) for digit in str(number)]
    startDigits = "".join(map(str, digits))
    swapped_digits = ''
    for i in range(0, len(digits)-1, 2):
        if digits[i] != digits[i+1]: zero += 1
    for i in range(0, len(digits)-1, 2):
        if digits[i] == digits[i+1]:
            swapped_digits = swapped_digits + str(digits[i]) + str(digits[i+1])
            if len(digits)-1 <= i+1:
                if all(elem == digits[0] for elem in digits):
                    swapped_digits = swapped_digits + str(digits[-1])
        else:
            swapped_digits = swapped_digits + str(digits[i+1]) + '0'*(zero*2) + str(digits[i])
            digits[i],digits[i+1] = digits[i+1], digits[i]
    if len(digits) % 2 == 1:
        swapped_digits = swapped_digits + str(digits[-1])
    swapped_digits = int(swapped_digits)
    if max_value < swapped_digits:
        max_value = swapped_digits
        lexeme = startDigits

def convert_number_to_words(number):
    d_db = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять',}
    words = [d_db[digit] for digit in str(number)]
    result = ' '.join(words)
    return result

max_value = float('-inf')
work_buffer = ''
buffer_len = 1
max_buffer_len = 100
razd = [' ', ',', ';', ':', '?', '!', '&', '*', '.', '\n']
with open('text.txt', 'r', encoding='utf-8') as file:
    buffer = file.read(buffer_len)
    lexeme_found = False
    if not buffer: print('\nФайл text.txt в директории проекта пустой. \nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.')
    while buffer:
        if not buffer: break
        while buffer not in razd:
            work_buffer += buffer
            buffer = file.read(buffer_len)
            if not buffer: break
        process_lexeme(work_buffer)
        lexeme_found = True
        work_buffer = ''
        buffer = file.read(buffer_len)
if lexeme_found:
    if max_value != float('-inf'): print('\nИсходное число:', lexeme, '\nОбработанное число:', max_value,'\nОтвет:', convert_number_to_words(max_value))
    else: print('\nЛексем в файле не осталось или лексемы не удовлетворяют условию (в данном случае проверьте файл и(или) замените text.txt на другой). \nПрограмма завершает работу.')