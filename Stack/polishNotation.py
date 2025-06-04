# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(int(left / right))
        else:
            stack.append(int(token))
    return stack[0]

test_cases = [
    ["2", "1", "+", "3", "*"],
    ["4", "13", "5", "/", "+"],
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
]

for test_case in test_cases:
    print(evalRPN(test_case))