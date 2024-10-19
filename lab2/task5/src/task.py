def count_majority(A, target, l, r):
  count = 0
  for i in range(l, r+1):
    if A[i] == target:
      count += 1

  return count

def majority(A, l, r):
  mid = (l + r) // 2

  if l == r:
    return A[l]
  
  al = majority(A, l, mid)
  ar = majority(A, mid+1, r)

  if al == ar:
    return al

  al_count = count_majority(A, al, l, r)
  ar_count = count_majority(A, ar, l, r)

  if al_count > (r - l) // 2:
    return al
  elif ar_count > (r - l) // 2:
    return ar

  return None

def has_majority(A, n):
  res = majority(A, 0, n-1)
  if res is not None:
    count = count_majority(A, res, 0, n-1)
    if count > n // 2:
      return 1
  return 0