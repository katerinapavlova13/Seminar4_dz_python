# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

numbers = int(input("Введите  число: "))

def factors(numbers):
    factors = list()
    i = 2
    while i <= numbers:
        if numbers % i == 0:
            factors.append(i)
            numbers //= i
        else:
            i += 1
    return factors

print(factors(numbers))


