import time
# скорость задания 2
t_start = time.perf_counter()
n = int(open('input.txt').readline())
f = open("output.txt", 'w')

if 0 <= n <= 45:
  a,b = 0,1
  for _ in range(n):
    a,b = b, a+b
  f.write(str(a))
f.close()  
print("Время 2 задания %s секунд" % (time.perf_counter() - t_start))

# скорость задания 3
t_start = time.perf_counter()

n = int(open('input1.txt').readline())
f = open("output1.txt", 'w')

if 0 <= n <= 10**7:
  a,b = 0,1
  for _ in range(n):
    a,b = b, (a+b)%10
  f.write(str(a))
f.close()  

print("Время 3 задания %s секунд" % (time.perf_counter() - t_start))
