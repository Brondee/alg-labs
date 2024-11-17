import unittest
from task13.src.stack import Stack 

class AlgorithmsSortTestCase(unittest.TestCase):
    
    def test_should_check_success_of_stack(self):
      stack = Stack()
      self.assertEqual(stack.isEmpty(), True)
      self.assertEqual(stack.display(), None)

      stack.push(10)
      self.assertEqual(stack.isEmpty(), False)
      self.assertEqual(stack.pop(), 10)
      self.assertEqual(stack.isEmpty(), True)


if __name__ == '__main__':
  unittest.main()