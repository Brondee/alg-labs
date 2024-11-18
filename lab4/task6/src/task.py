import utils

def queue_func_min(commands):
  queue = []  
  res = []
  for command in commands:
    if command[0] == "+":
      queue.append(int(command[1]))
    elif command[0] == "-":
      queue.pop(0)
    elif command[0] == '?':
      res.append(str(min(queue))  + "\n")
  
  return res
  
if __name__ == '__main__':
  print("task 6")
  data = utils.read_data('lab4/task6/textf/input.txt')
  print(data)
  res = queue_func_min(data[1:])
  print(res)
  utils.write_file("lab4/task6/textf/output.txt", res)
  