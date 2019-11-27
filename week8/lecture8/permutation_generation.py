#!/usr/bin/env python3

"""
    Генерация всех перестановок

Элементы комбинаторики
При n чисел, количество перестановок всех чисел = n! (n - факториал)

Задача стоит в том, чтобы вывести на экран все возможные варианты перестановки чисел.

Решаем с помощью рекурсии

Упрощение: от 0 до n-1
"""

""" Вариант с применением рекурсии"""
def generate_numbers(n:int, m:int, prefix=None):

    """Генерирует все числа (с лидирующими нулями
        в n-ричной системе счисления (n <= 10))
        длинной m.
        n - основание для систем исчисления,
        m - длинна числа,
        prefix - список
    """
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


""" Вариант с применением цикла"""
def gen_byn(m, prefix=""):
    if m == 0:
        print(prefix)
    else:
        for digit in "0", "1":
            gen_byn(m - 1, prefix + digit)

# Только для двоичной системы исчисления
gen_byn(4)

# Для произвольной системы исчисления
generate_numbers(4, 3)