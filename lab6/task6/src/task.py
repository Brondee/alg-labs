import utils

def is_fibonacci(num):
    x1 = 5 * num ** 2 + 4
    x2 = 5 * num ** 2 - 4
    
    return is_perfect_square(x1) or is_perfect_square(x2)

def is_perfect_square(x):
    if x < 0:
        return False
    
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return True
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


def process_fibonacci(data):
    results = []
    
    for num in data:
        if is_fibonacci(num):
            results.append("Yes\n")
        else:
            results.append("No\n")

    return results

if __name__ == '__main__':
  data = utils.read_data('lab6/task6/textf/input.txt')
  res = process_fibonacci(data[1:])
  utils.print_task_data(6, 6, data, res)
  utils.write_file("lab6/task6/textf/output.txt", res)