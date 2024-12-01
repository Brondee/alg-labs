import utils

def solve_hash(data):
    N, X, A, B = data[0]
    AC, BC, AD, BD = data[1]
    
    hash_table = set()
    
    for _ in range(N):
        if X in hash_table:
            A = (A + AC) % 10**3
            B = (B + BC) % 10**15
        else:
            hash_table.add(X)
            A = (A + AD) % 10**3
            B = (B + BD) % 10**15
        
        X = (X * A + B) % 10**15

    return f'{X} {A} {B}'

if __name__ == '__main__':
  data = utils.read_data('lab6/task8/textf/input.txt')
  res = solve_hash(data)
  utils.print_task_data(6, 8, data, res)
  utils.write_file("lab6/task8/textf/output.txt", [res])