nums = list(map(int, open('input.txt').readline().split()))
f = open("output.txt", 'w')
f.write(str(nums[0] + nums[1]))
f.close()