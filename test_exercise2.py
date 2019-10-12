"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""

def solution(input):
  output = []
  for i in range(len(input)):
    result = 1
    for j in range(len(input)):
      if i != j:
        result = result * input[j]
    output.append(result)
  return output


def test_solution():
  input = [1, 2, 3, 4, 5]
  expected_output = [120, 60, 40, 30, 24]

  assert expected_output == solution(input)