N = int(input()) # Вводится количество студентов

student_list = [[] for i in range(N)] # Создаем список студентов с пустыми списками их оценок, где N - Количество вложенных списков

def grades_list(N, student_list): # Ф-ция формирует список успеваемости "grades list"
    while True:
        x = input()
        
        if x == '#':
            break
    
        student_grade = list(map(int, x.split())) # создаем список натуральных чисел из полученных в перменной "х" значений (2 числа)
    
        student_id = student_grade[0] # Первый элемент присваивем переменной "student_id"
    
        value = student_grade[1] # Второй элемент присваивем переменной "value"
        
        student_list[student_id].append(value) # Добавляем "value" во вложенный в "student_list" список №"student_id" по счету
    
    return student_list #Возвращаем список "student_list"

def revers_sort(l): # Ф-ция возвращает сумму чисел из вложенного списка
    if isinstance(l, list): # Если елемент списка является списком
        return sum(revers_sort(x) for x in l) # Вернуть сумму всех элементов данного вложенного списка
    else: # Иначе
        return l # Вернуть значениеединого элемента

grades_list(N, student_list)
student_list.sort(key=revers_sort, reverse=True)

print(student_list)