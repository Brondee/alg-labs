import utils

def queue_func(commands):
  queue = []  
  front_index = 0 
  res = []
  for command in commands:
    if command[0] == "+":
      queue.append(int(command[1]))
    elif command[0] == "-":
      res.append(str(queue[front_index])  + "\n")
      front_index += 1
  
  return res
  
if __name__ == '__main__':
  data = utils.read_data('task2/textf/input.txt')
  res = queue_func(data[1:])
  utils.write_file("task2/textf/output.txt", res)
  