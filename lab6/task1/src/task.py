import utils

def process_operations(n, data):
  result = []
  s = set()

  for i in range(n):
      line = data[i]
      operation = line[0]
      x = int(line[1])

      if operation == 'A':
          s.add(x)
      elif operation == 'D':
          s.discard(x)
      elif operation == '?':  
          if x in s:
              result.append('Y\n')
          else:
              result.append('N\n')

  return result

if __name__ == '__main__':
  data = utils.read_data('lab6/task1/textf/input.txt')
  res = process_operations(data[0], data[1:])
  utils.print_task_data(6, 1, data, res)
  utils.write_file("lab6/task1/textf/output.txt", res)