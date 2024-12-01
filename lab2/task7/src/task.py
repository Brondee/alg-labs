import utils

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
  data = utils.read_data('lab2/task7/textf/input.txt')
  res = max_subarray(data[1])
  utils.print_task_data(2, 7, data, res)