# check for valid / complete sets of brackets
validChars = ['(', '[', '{']
stack = []
def isBalanced(chars: str):
    for char in chars:
        print('checking char: ', char)
        # 1 if char is valid OPEN brace then push to stack
        if char in validChars:
            stack.append(char)
            print('step 1: appending ', char, ' to stack')
            print('stack: ', stack)
        else:
        # 2 if stack is empty (nothing was pushed bc CLOSING brace)
            if not stack:
                print('step 2: string NOT balanced')
                return False
        # 3 if stack NOT empty (there exists a valid OPEN brace) get top char
            top = stack.pop()
            print('step 3: top = ', top)
        # 4 if step 2 passed = valid OPEN brace then check if top has a matching CLOSE brace
            print('checking if ', top, ' matches ', char)
            if top == '[' and char != ']' or top == '(' and char != ')' or top == '{' and char != '}':
                print('step 4: string NOT balanced')
                return False
    # 5 stack is empty string balanced if not string NOT balanced
    print('step 5: check stack length\n', len(stack))
    print('string balanced') if not stack else print('string NOT balanced')
    return True if not stack else False

isBalanced('[()]')
# SUMMARY if an opening brace is followed by a closing brace which is NOT a valid mate the string is imbalanced
# if the char is a closing brace check it against top of stack
# if there is a match then the top element (opening brace) gets popped off
# the new top is the next opening brace in the stack which gets checked against the next char
# if the chars all have an open and closing brace uninterrupted by a singular closing or open brace then all elements will be popped until stack len is 0
# if one closing or open brace is left it indicates there was no match and was left in the stack
# if there is any elements left in the stack the string was not balanced
# if empty it was balanced

# todo refactor with clean code principles