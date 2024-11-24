import utils

def build_pyramid(n, data):
    swaps = []

    def move_down(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[min_index]:
            min_index = left

        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append(f'{i} {min_index}\n')
            data[i], data[min_index] = data[min_index], data[i]
            move_down(min_index)

    for i in range(n // 2 - 1, -1, -1):
        move_down(i)

    swaps.insert(0, str(len(swaps)) + '\n')
    return swaps

if __name__ == '__main__':
  data = utils.read_data('lab5/task4/textf/input.txt')
  res = build_pyramid(data[0], data[1])
  utils.print_task_data(4, data, res)
  utils.write_file("lab5/task4/textf/output.txt", res)

