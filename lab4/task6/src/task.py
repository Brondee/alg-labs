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
  data = utils.read_data('task6/textf/input.txt')
  res = queue_func_min(data[1:])
  utils.write_file("task6/textf/output.txt", res)
  