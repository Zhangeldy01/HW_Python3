# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример: *
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random
N = int(input('Введите число: '))
lst = [random.randint(1, N) for _ in range(N)]
print(*lst)
n = int(input())
count = 0
for i in lst:
    if i == n:
        count += 1
print(count)
