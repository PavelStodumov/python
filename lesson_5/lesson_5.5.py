from time import perf_counter
import random

# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# result = [23, 1, 3, 10, 4, 11]

src = [random.randint(1, 200) for num in range(10 ** 3)]
print(len(src), '- длинна списка')
#
start = perf_counter()
tmp = set()
uniq_elem = set()
for elem in src:
    if elem not in tmp:
        uniq_elem.add(elem)
    else:
        uniq_elem.discard(elem)
    tmp.add(elem)
result = [elem for elem in src if elem in uniq_elem]
print(result, perf_counter() - start, "- через множества")
#
start = perf_counter()
result = []
for elem in src:
    if src.count(elem) < 2:
        result.append(elem)
print(result, perf_counter() - start, "- через перебор списка")
#
start = perf_counter()
result = list(filter(lambda x: src.count(x) < 2, src))
print(result, perf_counter() - start, "- еще один способ перебора списка")
#
start = perf_counter()
result = (num for num in src if src.count(num) < 2)
print(*result, perf_counter() - start, '- через итератор')
#
print("на практике более громоздкое решение через множества работает гораздо быстрее")

