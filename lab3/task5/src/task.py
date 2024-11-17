import utils

def hirsh_index(arr):
    arr.sort(reverse=True) 
    h = 0
    for i, n in enumerate(arr):
        if n >= i + 1:
            h = i + 1
        else:
            break
    return h

if __name__ == '__main__':
  data = utils.read_data('task5/textf/input.txt')
  hirsh_index(data[0])