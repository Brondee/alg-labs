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