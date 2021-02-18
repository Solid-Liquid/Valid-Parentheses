class Solution:
    matchOp = { '}':'{', ')':'(', ']':'[' }
    
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=='(' or c=='{' or c=='[':
                stack.append(c)
            elif not (len(stack)>0 and stack.pop()==self.matchOp.get(c)):
                    return False
        return len(stack)==0