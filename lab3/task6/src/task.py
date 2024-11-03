from task1.src.task2 import randomized_quicksort 

def sum_of_tenth(A, B):
    C = []
    for b in B:
        for a in A:
            C.append(a * b)
    randomized_quicksort(C, 0, len(C) - 1)
    sum_of_tenth = sum(C[i] for i in range(0, len(C), 10))

    return sum_of_tenth

if __name__ == '__main__':
  sum_of_tenth()