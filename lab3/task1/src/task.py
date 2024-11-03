import random

def partition(A, l, r):
  x = A[l]
  j = l
  for i in range(l+1, r+1):
    if A[i] <= x:
      j += 1
      A[j], A[i] = A[i], A[j]
  A[l], A[j] = A[j], A[l]
  return j

def randomized_quicksort(A,l,r):
  if l < r:
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]
    m = partition(A, l, r)
    randomized_quicksort(A, l, m-1)
    randomized_quicksort(A, m+1, r)
  return A