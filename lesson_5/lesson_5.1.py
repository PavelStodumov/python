# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
def odd_num(num):
    for i in range(1, num + 1, 2):
        yield i


odd_to_15 = odd_num(15)
print(odd_to_15)
print(next(odd_to_15), next(odd_to_15), next(odd_to_15))
print(*odd_to_15)


# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
def odd_num_2(num):
    return (i for i in range(1, num + 1, 2))


odd_to_9 = odd_num_2(9)
print(type(odd_to_9))
print(next(odd_to_9), next(odd_to_9), next(odd_to_9), next(odd_to_9))
