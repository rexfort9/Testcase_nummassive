
from collections import Counter
import sys
from time import time

def find_most_common_number(arr):
    counter = Counter(arr)
    most_common = counter.most_common(1)
    return most_common[0][0]

# Reading input data
n = int(input("Enter number's qty: "))
ai = list(map(int, input("List numbers, separate via 'space': ").split()))
start = time()

# Call func. & call result
result = find_most_common_number(ai)
for result in range(0,1000000):
    pass

end_time = time()

print(result)
print("List size in memory: ", sys.getsizeof(ai), "bytes")

memory = sys.getsizeof(ai)
if memory <= 268435456:
    print("String sise less than 256 Мб")

elapsed_time = end_time - start
print ("Time to RUN: ", elapsed_time)

if time() -start < 2:
    print("Runtime error.")
else: 
    print("Time= " ,(start))
