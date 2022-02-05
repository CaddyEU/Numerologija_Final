# -*- coding: cp1251 -*-

# dict в котором ключи это числовой вес букв, а значения эти списки букв с этим весом
letters_value_dict = {
    'а': 1, 'и': 1, 'с': 1, 'ъ': 1, 'a': 1, 'j': 1, 's': 1,
    'б': 2, 'й': 2, 'т': 2, 'ы': 2, 'b': 2, 'k': 2, 't': 2,
    'в': 3, 'к': 3, 'у': 3, 'ь': 3, 'c': 3, 'l': 3, 'u': 3,
    'г': 4, 'л': 4, 'ф': 4, 'э': 4, 'd': 4, 'm': 4, 'v': 4,
    'д': 5, 'м': 5, 'х': 5, 'ю': 5, 'e': 5, 'n': 5, 'w': 5,
    'е': 6, 'н': 6, 'ц': 6, 'я': 6, 'f': 6, 'o': 6, 'x': 6,
    'ё': 7, 'о': 7, 'ч': 7, 'g': 7, 'p': 7, 'y': 7,
    'ж': 8, 'п': 8, 'ш': 8, 'h': 8, 'q': 8, 'z': 8,
    'з': 9, 'р': 9, 'щ': 9, 'i': 9, 'r': 9
}


# функция которая складывает цифры числа пока число не будет состоять из одной цифры
def sum_digits(final_number):
    digits_list = [int(digits) for digits in str(final_number)]
    while len(digits_list) > 1:
        digits_list = sum([int(digits) for digits in digits_list])
        digits_list = [int(digits) for digits in str(digits_list)]
        if len(digits_list) == 1:
            return digits_list[0]


# ввод имени
name = input('Введите ваше имя: ')

# определение промежуточного числа
final_number = 0

# идем по буквам имени делая их маленьким, что бы не
# путался регистр и ищем их в словаре, если нашли прибавляем число к сумме


for letters in name:
    try:
        final_number += letters_value_dict[letters.lower()]
    except KeyError as e:
        print(e)

# выводим на печать результат передавая промежуточный результат в функцию для пересчета
final_digit = sum_digits(final_number)
print(f"Ваше число: {final_digit}")

def bonus():
    if final_digit == 1:
        f = open("list_1.txt", "r", encoding="utf-8")
        print(f.read())
    if final_digit == 2:
        f = open("list_2.txt", "r", encoding="utf-8")
        print(f.read())
    if final_digit == 3:
        f = open("list_3.txt", "r", encoding="utf-8")
        print(f.read())
    if final_digit == 4:
        f = open("list_4.txt", "r", encoding="utf-8")
        print(f.read())
    if final_digit == 5:
        f = open("list_5.txt", "r", encoding="utf-8")
        print(f.read())
    if final_digit == 6:
        f = open("list_6.txt", "r", encoding="utf-8")
        print(f.read())
    if final_digit == 7:
        f = open("list_7.txt", "r", encoding="utf-8")
        print(f.read())
    if final_digit == 8:
        f = open("list_8.txt", "r", encoding="utf-8")
        print(f.read())
    if final_digit == 9:
        f = open("list_9.txt", "r", encoding="utf-8")
        print(f.read())
pass

bonus()
