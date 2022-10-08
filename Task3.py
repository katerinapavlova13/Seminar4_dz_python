# Задайте последовательность цифр.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


from random import randint

my_list = "".join(list(map(str, [randint(0, 9) for i in range(15)])))
def list_no_repetitions(line):
    new_list = []
    for item in line:
        if line.count(item) == 1:
            new_list.append(int(item))
    return new_list

print(f"Неповторяющиеся элементы списка: {my_list} => {list_no_repetitions(my_list)}")









# from random import randint as rI
# unique = {}
# my_list = "".join(list(map(str, [rI(0, 9) for i in range(20)])))
# print(my_list)
#
# for c in my_list:
#     if unique.get(c):
#         unique[c] = unique.get(c) + 1
#     else:
#         unique[c] = 1
#
# ulist = []
#
# for i in unique.items():
#     if i[1] == 1:
#         ulist.append(i[0])
# print(ulist)









