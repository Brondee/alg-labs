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
  print("task 8")
  data = utils.read_data('lab4/task8/textf/input.txt')
  print(data)
  res = postfix(data[1])
  print(res)
  utils.write_file("lab4/task8/textf/output.txt", res)