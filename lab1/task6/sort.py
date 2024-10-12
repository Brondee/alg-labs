import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open('./input.txt')
n = int(f.readline())
arr = list(map(int, f.readline().split()))

for i in range(n):
  for j in range(0, n-i-1):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j]

f2 = open("output.txt", 'w')
f2.write((" ").join(list(map(str, arr))))
f2.close()

print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()