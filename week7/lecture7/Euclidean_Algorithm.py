'''
Алгори́тм Евкли́да

    — эффективный алгоритм для нахождения наибольшего общего делителя двух целых чисел
    (или общей меры двух отрезков). ...

    Процесс повторяется, пока числа не станут равными.
    Найденное число и есть наибольший общий делитель исходной пары.

    lcf - Largest common factor(Наибольший общий делитель)
'''
a = int(input("Введите значение для а: "))
b = int(input("Введите значение для b: "))

'''
Более сложный вариант
Жрет много памяти, если разница между a и b очень большая.

    Крайний случай:
        lcf(a, b) = a, если a = b

    Рекурентные случаи(их 2, так как, непонятно a или b больше):
        lcf(a, b) = lcf(a - b, b), если a > b
        lcf(a, b) = lcf(b - a, a), если a < b
'''
'''
def lcf(a, b):
    if a == b:
        return a
    elif a > b:
        return lcf(a - b, b)
    else:
        return lcf(b - a, a)
'''

'''
Более простой вариант

Если a % b = 0,
    то b и есть "Наибольший общий делитель"

Крайний случай:
        lcf(a, b) = a, если b = 0

    Рекурентный случай():
        lcf(a, b) = lcf(b, a % b)


def lcf(a, b):
    if b == 0:
        return a
    return lcf(b, a % b)
'''

# Более краткая запись

def lcf(a, b):
    return a if b == 0 else lcf(b, a % b)

print("Наибольший общий делитель = ", lcf(a, b))

