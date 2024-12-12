import utils

def min_coins(money, coins):
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money] if dp[money] != float('inf') else -1

if __name__ == '__main__':
  data = utils.read_data('lab7/task1/textf/input.txt')
  res = min_coins(data[0][0], data[1])
  utils.print_task_data(7, 1, data, res)
  utils.write_file("lab7/task1/textf/output.txt", res)