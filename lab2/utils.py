def write_file(file_path, data):
  f2 = open(file_path, 'w')
  f2.write((" ").join(list(map(str, data))))
  f2.close()

def read_data(file_path: str):
    file = open(file_path, 'r')
    lines = file.readlines()
    data = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if len(line.split()) == 1:
            data.append(int(line))
        else:
            data.append(list(map(int, line.split())))
        i += 1
    file.close()
    return data

def end_test(time, amount_data):
  print('Время работы: %s секунд' % time)
  print("Память:", amount_data, "МБ")