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
  hirsh_index()