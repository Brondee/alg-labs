import utils

def add_polynomials(A, B):
  return [A[i] + B[i] for i in range(len(A))]

def subtract_polynomials(A, B):
  n = max(len(A), len(B))
  A += [0] * (n - len(A))
  B += [0] * (n - len(B))
  return [A[i] - B[i] for i in range(len(A))]

def multiply_polynomials(A, B, n):
  if len(A) == 1:
    return [A[0] * b for b in B]
  if len(B) == 1:
    return [B[0] * a for a in A]
  
  if len(A) % 2 != 0:
    A.append(0)
    B.append(0)
  
  n = len(A)
  A1, A2 = A[:n//2], A[n//2:]
  B1, B2 = B[:n//2], B[n//2:]

  P1 = multiply_polynomials(A1, B1, n)
  P2 = multiply_polynomials(A2, B2, n)
  A1_plus_A2 = add_polynomials(A1, A2)
  B1_plus_B2 = add_polynomials(B1, B2)
  P3 = multiply_polynomials(A1_plus_A2, B1_plus_B2, n)

  middle_term = subtract_polynomials(subtract_polynomials(P3, P1), P2)

  result = [0] * (2 * n - 1)
  
  for i in range(len(P1)):
      result[i] += P1[i]
  for i in range(len(middle_term)):
      result[i + n//2] += middle_term[i]
  for i in range(len(P2)):
      result[i + n] += P2[i]

  while len(result) > 1 and result[-1] == 0:
     result.pop()

  return result


if __name__ == '__main__':
  data = utils.read_data('lab2/task8/textf/input.txt')
  res = multiply_polynomials(data[1], data[2], data[0])
  utils.print_task_data(2, 8, data, res)