import utils

def bin_search(A, target, l, r):
  if l > r:
    return -1

  mid =(l+r)//2 
  if A[mid] == target:
    return mid

  if target > A[mid]:
    return bin_search(A, target, mid+1, r)
  if target < A[mid]:
    return bin_search(A, target, l, mid-1)

def find_ind(A, B, n):
  res = []
  for num in B:
    res.append(bin_search(A, num, 0, n - 1))
  
  return res

if __name__ == '__main__':
  data = utils.read_data('lab2/task4/textf/input.txt')
  res = find_ind(data[1], data[3], data[0])
  utils.print_task_data(4, data, res)