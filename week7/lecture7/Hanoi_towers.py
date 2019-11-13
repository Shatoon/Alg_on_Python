#!/usr/bin/python3

'''
Рекурентная реализация алгоритма "Ханойские башни"

Даны три стержня, на один из которых нанизаны восемь колец, причём кольца отличаются размером
 и лежат меньшее на большем. Задача состоит в том, чтобы перенести пирамиду из n колец
 за наименьшее число ходов c первого на третий стержень.
 За один раз разрешается переносить только одно кольцо,
 причём нельзя класть большее кольцо на меньшее.

Алгоритм выполнения:

    -Запрашиваем число "n" натуральное, положительное
        n = количество кругов пирамиды

    - Предпроверка:
        assert n > 0 # Число n должно быть больше 0
            в инном случае выводим ошибку - "Количество колец в пирамиде, не может быть меньше 1!"

    Рекурсивная ф-ция:

    - Крайний случай:
        if n == 1: # Если на стартовом столбце 1 кольцо,
            print(n, start, finish) # Переносим его на финишный столбец

    - Рекурсивный случай:
        tmp = 6 - start - finish # Обозначаем временный столбец
                "tmp = сумме номеров всех столбцов(№1 + №2 + №3 = 6) - номер столбца "start"
                    - номер столбца "finish"

        if n > 1: # Если колец 2 и больше, нужно:
            - перенести кольцо n-1 на временный столбец(tmp),
                - запускается крайний случай
            - кольцо n-1 c tmp на финишный столбец



'''
n = int(input("Количество колец в пирамиде:"))

assert  n > 0, "Количество колец в пирамиде, не может быть меньше 1!"

def move(n, start, finish):

    if n == 1:
        print("Кольцо №", n, "переносим со столбца", start, "на столбец", finish)
    else:
        tmp = 6 - start - finish

        move(n - 1, start, tmp)
        print("Кольцо №", n, "переносим со столбца", start, "на столбец", finish)
        move(n-1, tmp, finish)

move(n, 1, 3)