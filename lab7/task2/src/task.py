import utils


def min_operations(n):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    path = []
    current = n
    while current > 1:
        path.append(str(current))
        if current % 3 == 0 and dp[current] == dp[current // 3] + 1:
            current //= 3
        elif current % 2 == 0 and dp[current] == dp[current // 2] + 1:
            current //= 2
        else:
            current -= 1
    path.append(str(1))

    return [str(dp[n]) + "\n", (" ").join(path[::-1])]

if __name__ == "__main__":
  data = utils.read_data('lab7/task2/textf/input.txt')
  res = min_operations(data[0])
  utils.print_task_data(7, 2, data, res)
  utils.write_file("lab7/task2/textf/output.txt", res)

