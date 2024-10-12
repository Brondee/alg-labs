import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open('./input.txt')
n = int(f.readline())
arr = list(map(int, f.readline().split()))

def swap(i, j, ar):
    ar[i], ar[j] = ar[j], ar[i]

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key > arr[j]:
        swap(j, j+1, arr)
        j -= 1
    
f2 = open("output.txt", 'w')
f2.write((" ").join(list(map(str, arr))))
f2.close()

print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()