# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
#
# The following rules define a valid string:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

class Solution:
    def checkValidString(self, s: str) -> bool:
        if s == '*':
            return True
        if len(s) < 2:
            return False
        
        stack = []
        
        for ch in s:
            if ch in ['(', '*']:
                stack.append(ch)
            elif not stack.pop() in ['(', '*']:
                return False
        
        return not bool(len(stack))
        
        


if __name__ == '__main__':
    s = Solution()
    # assert s.checkValidString('*')
    # assert not s.checkValidString('(')
    assert s.checkValidString('()')
    assert s.checkValidString('(*)')
    assert s.checkValidString('(*))')
    assert s.checkValidString('(**((()')
