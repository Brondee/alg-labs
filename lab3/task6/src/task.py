from lab3.task1.src.task2 import randomized_quicksort 
import utils

def sum_of_tenth(A, B):
    C = []
    for b in B:
        for a in A:
            C.append(a * b)
    randomized_quicksort(C, 0, len(C) - 1)
    sum_of_tenth = sum(C[i] for i in range(0, len(C), 10))

    return sum_of_tenth

if __name__ == '__main__':
    data = utils.read_data('lab3/task6/textf/input.txt')
    res = sum_of_tenth(data[1], data[2])
    utils.print_task_data(6, data, res)
