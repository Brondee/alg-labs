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
