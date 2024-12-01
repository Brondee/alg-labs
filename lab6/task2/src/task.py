import utils

def manage_phonebook(data):
    phonebook = {}
    result = []

    for query in data:
        command = query[0]
        
        if command == 'add':
            number = query[1]
            name = query[2]
            phonebook[number] = name

        elif command == 'del':
            number = query[1]
            if number in phonebook:
                del phonebook[number]

        elif command == 'find':
            number = query[1]
            if number in phonebook:
                result.append(phonebook[number] + '\n')
            else:
                result.append('not found\n') 

    return result

if __name__ == '__main__':
  data = utils.read_data('lab6/task2/textf/input.txt')
  res = manage_phonebook(data[1:])
  utils.print_task_data(6, 2, data, res)
  utils.write_file("lab6/task2/textf/output.txt", res)