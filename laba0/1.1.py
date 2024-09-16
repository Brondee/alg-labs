nums = list(map(int, input().split()))
while not ((-10**9 <= nums[0] <= 10**9) and (-10**9 <= nums[1] <= 10**9)):
  print("Введите числа правильно")
  nums = list(map(int, input().split()))
print(sum(nums))
  

