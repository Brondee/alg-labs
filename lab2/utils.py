def write_file(file_path, data):
  f2 = open(file_path, 'w')
  f2.write((" ").join(list(map(str, data))))
  f2.close()

def end_test(time, amount_data):
  print('Время работы: %s секунд' % time)
  print("Память:", amount_data, "МБ")