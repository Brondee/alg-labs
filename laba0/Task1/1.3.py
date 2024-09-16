nums = list(map(int, open('input.txt').readline().split()))
f = open("output.txt", 'w')
if (-10**9 <= nums[0] <= 10**9) and (-10**9 <= nums[1] <= 10**9):
  f.write(str(nums[0] + nums[1]))
  f.close()
else:
  print("Введите числа правильно")
  f.close()

