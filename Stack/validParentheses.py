# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    stack = []
    match = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char in [")", "]", "}"]:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    return len(stack) == 0
        
test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "({})",
    "({})"
]

for test_case in test_cases:
    print(isValid(test_case))