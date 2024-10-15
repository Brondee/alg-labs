import time
import tracemalloc
tracemalloc.start()
t_start = time.perf_counter()

f = open('task10/textf/input.txt')
n = int(f.readline())
chars = f.readline()

chars_count = {}
for c in chars:
  if c not in chars_count:
    chars_count[c] = 1
  else:
    chars_count[c] += 1

chars_count_sort = sorted(chars_count.items(), key=lambda x: (-x[1], x[0]), reverse=True)

res = ""
for key, value in chars_count_sort:
  if value % 2 != 0 and res == "":
    res += key * value
  elif value % 2 == 0:
    res = key * (value // 2) + res + key * (value // 2)
  
f2 = open("task10/textf/output.txt", 'w')
f2.write(res)
f2.close()

print('Время работы: %s секунд' % (time.perf_counter() - t_start))
print("Память:", tracemalloc.get_traced_memory()[1] / (1024 ** 2), "МБ")
tracemalloc.stop()