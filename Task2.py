# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

numbers = int(input("Введите натуральное число: "))

def factors(numbers):
    factor = list()
    i = 2
    while (i <= numbers):
        if (numbers % i) == 0:
            factor.append(i)
            numbers //= i
        else:
            i += 1
    return factor

print(factors(numbers))


