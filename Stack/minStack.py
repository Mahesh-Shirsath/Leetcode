# 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val is None or val < min_val:
            min_val = val
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

test_cases = [
    ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
    [[], [0], [1], [0], [], [], [], []],
]

for test_case in test_cases:
    minStack = MinStack()
    for i in range(1, len(test_case)):
        if test_case[i] == "push":
            minStack.push(test_case[i+1])
        elif test_case[i] == "pop":
            minStack.pop()
        elif test_case[i] == "top":
            print(minStack.top())
        elif test_case[i] == "getMin":
            print(minStack.getMin())