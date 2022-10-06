# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import math

d = float(input("Введите число от 0.1 до 0.0000000001: "))
def get_count(d):
    str_d = str(d)
    if "." in str_d:
        return len(str_d.split(".")[1].rstrip("0"))
    else:
        return 0


res = get_count(d)
print(res)

print(round(math.pi, res))






