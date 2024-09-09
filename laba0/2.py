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