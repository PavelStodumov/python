# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
numbers = [number ** 3 for number in range(1, 1000, 2)]

# a.Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
total = 0
for number in numbers:
    is_total = number
    get_sum = number % 10  # Вычисляем сумму цыфр
    while number > 0:
        number //= 10
        get_sum += number % 10
    if get_sum % 7 == 0:
        total += is_total
print(numbers)
print(total)

# b.К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
numbers2 = [number + 17 for number in numbers]
total2 = 0
for number in numbers2:
    is_total2 = number
    get_sum = number % 10       # Вычисляем сумму цыфр
    while number > 0:
        number //= 10
        get_sum += number % 10
    if get_sum % 7 == 0:
        total2 += is_total2
print(numbers2)
print(total2)

# c.* Решить задачу под пунктом b, не создавая новый список.
total3 = 0
for number in numbers:
    number += 17
    is_total3 = number
    get_sum = number % 10  # Вычисляем сумму цыфр
    while number > 0:
        number //= 10
        get_sum += number % 10
    if get_sum % 7 == 0:
        total3 += is_total3
print(numbers)
print(total3)

# Как то так себе представляю
