'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

def validateP(s):
    closedToOpen = {')' : '(' , ']' : '[' , '}' : '{'}
    stack = []

    for c in s:
        if c in closedToOpen:
            
            if stack and stack[-1] == closedToOpen[c]:
                print(stack.pop())
            else:
                return False
        else:
            stack.append(c)
    return True if len(stack) == 0 else False

s = "()[]{}"
print(validateP(s))