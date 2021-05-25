from time import perf_counter
import sys

# Представлен список чисел.
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# result = [12, 44, 4, 10, 78, 123]

start = perf_counter()
result = (num for num in src[1:] if num > src[src.index(num) - 1])
print(*result, perf_counter() - start, '- время итератора')
print(sys.getsizeof(result), '-занимаемая память')
print('для итератора(как я понял) память не изменится в зависимости от длинны списка')

start = perf_counter()
result = []
for num in src[1:]:
    if num > src[src.index(num) - 1]:
        result.append(num)
print(result, perf_counter() - start, '- время цикла for')
print(sys.getsizeof(result), '-занимаемая память')

start = perf_counter()
result = list(filter(lambda num: num > src[src.index(num) - 1], src[1:]))
print(result, perf_counter() - start, '- время filter()')
print(sys.getsizeof(result), '-занимаемая память')

# время настолько разное с каждым запуском, не понимаю как сравнивать
