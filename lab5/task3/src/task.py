import utils


def network_packets(buffer_size, packets):
    buffer = []
    start_times = []

    for arrival_time, processing_time in packets:
        while buffer and buffer[0] <= arrival_time:
            buffer.pop(0)

        if len(buffer) >= buffer_size:
            start_times.append(-1)
        else:
            if not buffer:
                start_time = arrival_time
            else:
                start_time = buffer[-1]

            start_times.append(str(start_time))

            buffer.append(start_time + processing_time)

    return start_times

if __name__ == '__main__':
  data = utils.read_data('lab5/task3/textf/input.txt')
  res = network_packets(data[0][0], data[1:])
  utils.print_task_data(5, 3, data, res)
  utils.write_file("lab5/task3/textf/output.txt", res)
