# Задайте последовательность цифр.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

numbers = str(input("Задайте последовательность чисел: "))
numbers.split()
def list_no_repetitions(line):
    new_list = []
    for item in line:
        if line.count(item) == 1:
            new_list.append(int(item))
    return new_list

print(f"Неповторяющиеся элементы списка: {numbers} => {list_no_repetitions(numbers)}")






