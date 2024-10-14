import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open('task2/textf/input.txt')
n = int(f.readline())
arr = list(map(int, f.readline().split()))

indxs = []

for i in range(n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    indxs.append(j+2)
    arr[j + 1] = key

f2 = open("task2/textf/output.txt", 'w')
f2.write((" ").join(list(map(str, indxs))) + "\n")
f2.write((" ").join(list(map(str, arr))))
f2.close()

print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()