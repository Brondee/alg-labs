import time

# скорость задания 2
t_start = time.perf_counter()

n = int(open('inp_fib.txt').readline())
f = open("out_fib.txt", 'w')

if n <= 1:
  f.write(str(n))
else:
  a,b = 0,1
  for _ in range(2, n+1):
    a,b = b, a+b
  f.write(str(b))

f.close()  

print("Время 2 задания %s секунд" % (time.perf_counter() - t_start))

# скорость задания 3
t_start = time.perf_counter()

n = int(open('inp_fib1.txt').readline())
f = open("out_fib1.txt", 'w')

if n <= 1:
  f.write(str(n))
else:
  a,b = 0,1
  for _ in range(2, n+1):
    a,b = b, (a+b)%10
  f.write(str(b))
f.close()  

print("Время 3 задания %s секунд" % (time.perf_counter() - t_start))