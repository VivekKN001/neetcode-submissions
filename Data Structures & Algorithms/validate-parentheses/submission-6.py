class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["[", "(", "{"]
        closed_brackets = ["]", "}", ")"]
        stack = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if s[i] in open_brackets:
                stack.append(s[i])
            else:
                if s[i] in closed_brackets and len(stack) == 0:
                    return False
                else:
                    if (s[i] == "]" and stack[-1] == "[") or (s[i] == ")" and stack[-1] == "(") or (s[i] == "}" and stack[-1] == "{"):
                        stack.pop()
                    else:
                        stack.append(s[i])
                    
        
        print(stack)
        if len(stack):
            return False
        
        return True
