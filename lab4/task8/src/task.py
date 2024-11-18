import utils

def postfix(expression):
    stack = []
    
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    
    return stack.pop()

if __name__ == '__main__':
  data = utils.read_data('lab4/task8/textf/input.txt')
  res = postfix(data[1])
  utils.print_task_data(8, data, res)
  utils.write_file("lab4/task8/textf/output.txt", res)