def pugalo_sort(A, n, k):
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for i in range(0, n - k):
            if A[i] > A[i + k]:
                A[i], A[i + k] = A[i + k], A[i]
                sorted_flag = False 
    return "ДА" if A == sorted(A) else "НЕТ"

if __name__ == '__main__':
  pugalo_sort()