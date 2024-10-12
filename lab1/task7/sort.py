import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open('./input.txt')
n = int(f.readline())
M = list(map(float, f.readline().split()))

arr_ind = [[M[x], x + 1] for x in range(len(M))]
arr_ind.sort()

res = [arr_ind[0][1], arr_ind[len(M) // 2][1] ,arr_ind[-1][1]]

f2 = open("output.txt", 'w')
f2.write((" ").join(list(map(str, res))))
f2.close()

print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()