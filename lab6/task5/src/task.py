import utils

def process_elections(data):
    votes = {}
    
    for line in data:
        candidate, vote_count = line

        if candidate in votes:
            votes[candidate] += int(vote_count)
        else:
            votes[candidate] = int(vote_count)
    
    sorted_candidates = sorted(votes.items())

    res = []
    for candidate, votes in sorted_candidates:
        res.append(f'{candidate} {votes}\n')

    return res

if __name__ == '__main__':
  data = utils.read_data('lab6/task5/textf/input.txt')
  res = process_elections(data)
  utils.print_task_data(6, 5, data, res)
  utils.write_file("lab6/task5/textf/output.txt", res)