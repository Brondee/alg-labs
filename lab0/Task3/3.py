n = int(open('input.txt').readline())
f = open("output.txt", 'w')

if 0 <= n <= 10**7:
  a,b = 0,1
  for _ in range(n):
    a,b = b, (a+b)%10
  f.write(str(a))
f.close()  

