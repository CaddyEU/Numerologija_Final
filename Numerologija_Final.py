# -*- coding: cp1251 -*-

# dict � ������� ����� ��� �������� ��� ����, � �������� ��� ������ ���� � ���� �����
letters_value_dict = {
    '�': 1, '�': 1, '�': 1, '�': 1, 'a': 1, 'j': 1, 's': 1,
    '�': 2, '�': 2, '�': 2, '�': 2, 'b': 2, 'k': 2, 't': 2,
    '�': 3, '�': 3, '�': 3, '�': 3, 'c': 3, 'l': 3, 'u': 3,
    '�': 4, '�': 4, '�': 4, '�': 4, 'd': 4, 'm': 4, 'v': 4,
    '�': 5, '�': 5, '�': 5, '�': 5, 'e': 5, 'n': 5, 'w': 5,
    '�': 6, '�': 6, '�': 6, '�': 6, 'f': 6, 'o': 6, 'x': 6,
    '�': 7, '�': 7, '�': 7, 'g': 7, 'p': 7, 'y': 7,
    '�': 8, '�': 8, '�': 8, 'h': 8, 'q': 8, 'z': 8,
    '�': 9, '�': 9, '�': 9, 'i': 9, 'r': 9
}


# ������� ������� ���������� ����� ����� ���� ����� �� ����� �������� �� ����� �����
def sum_digits(final_number):
    digits_list = [int(digits) for digits in str(final_number)]
    while len(digits_list) > 1:
        digits_list = sum([int(digits) for digits in digits_list])
        digits_list = [int(digits) for digits in str(digits_list)]
        if len(digits_list) == 1:
            return digits_list[0]


# ���� �����
name = input('������� ���� ���: ')

# ����������� �������������� �����
final_number = 0

# ���� �� ������ ����� ����� �� ���������, ��� �� ��
# ������� ������� � ���� �� � �������, ���� ����� ���������� ����� � �����


for letters in name:
    try:
        final_number += letters_value_dict[letters.lower()]
    except KeyError as e:
        print(e)

# ������� �� ������ ��������� ��������� ������������� ��������� � ������� ��� ���������
final_digit = sum_digits(final_number)
print(f"���� �����: {final_digit}")

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
