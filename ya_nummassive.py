
from collections import Counter
import sys
from time import time

def find_most_common_number(arr):
    counter = Counter(arr)
    most_common = counter.most_common(1)
    return most_common[0][0]

# Чтение входных данных
n = int(input("Введите кол-во искомых чисел: "))
ai = list(map(int, input("Перечислите эти числа через пробел: ").split()))
start = time()

# Вызов функции и вывод результата
result = find_most_common_number(ai)
for result in range(0,1000000):
    pass

end_time = time()

print(result)
print("Размер списка в памяти: ", sys.getsizeof(ai), "bytes")

memory = sys.getsizeof(ai)
if memory <= 268435456:
    print("Размер строки не превышает 256 Мб")

elapsed_time = end_time - start
print ("Time to RUN: ", elapsed_time)

if time() -start < 2:
    print("Runtime error.")
else: 
    print("Time= " ,(start))