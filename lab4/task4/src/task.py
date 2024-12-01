import utils

def check_brackets(data):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    for i, char in enumerate(data, start=1):
        if char in "([{":
            stack.append((char, i))
        elif char in ")]}":
            if not stack or stack[-1][0] != bracket_pairs[char]:
                return i
            stack.pop()
    
    if stack:  
        return stack[0][1]
    
    return "Success" 

if __name__ == '__main__':
  data = utils.read_data('lab4/task4/textf/input.txt')
  res = check_brackets(data[0])
  utils.print_task_data(4, 4, data, res)
  utils.write_file("lab4/task4/textf/output.txt", res)