class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        firstPointer, secondPointer = 0, len(s)-1
        while firstPointer <= secondPointer:
            if s[firstPointer] != s[secondPointer]:
                return False
            firstPointer+=1
            secondPointer-=1
        return True
        