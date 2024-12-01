import utils

def is_heap(n, array):
    for i in range(n):
        if 2 * i + 1 < n and array[i] > array[2 * i + 1]:
            return "NO"
        if 2 * i + 2 < n and array[i] > array[2 * i + 2]:
            return "NO"
    return "YES"


if __name__ == '__main__':
  data = utils.read_data('lab5/task1/textf/input.txt')
  res = is_heap(data[0], data[1])
  utils.print_task_data(5, 1, data, res)
  utils.write_file("lab5/task1/textf/output.txt", [res])
