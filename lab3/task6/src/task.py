from task1.src.task2 import randomized_quicksort 

def sum_of_tenth(A, B):
    C = []
    for b in B:
        for a in A:
            C.append(a * b)
    randomized_quicksort(C, 0, len(C) - 1)
    sum_of_tenth = sum(C[i] for i in range(0, len(C), 10))

    return sum_of_tenth

r1 = [7,1, 4, 9]
r2 = [2, 7, 8, 11]
print(sum_of_tenth(r1, r2))