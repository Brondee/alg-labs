def max_subarray(arr):
  max_sum = arr[0]
  current_sum = arr[0]
  
  st = end = 0
  temp_st = 0

  for i in range(1, len(arr)):
      if arr[i] > current_sum + arr[i]:
          current_sum = arr[i]
          temp_st = i  
      else:
          current_sum += arr[i]

      if current_sum > max_sum:
          max_sum = current_sum
          st = temp_st
          end = i
  return arr[st:end + 1]

if __name__ == '__main__':
  max_subarray()