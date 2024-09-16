n = int(open('inp_fib.txt').readline())
f = open("out_fib.txt", 'w')

if 0 <= n <= 45:
  a,b = 0,1
  for _ in range(n):
    a,b = b, a+b
  f.write(str(a))

f.close()  

