class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            firstPointer, secondPointer = 0, len(s)-1
            while firstPointer <= secondPointer:
                if s[firstPointer] != s[secondPointer]:
                    return False
                firstPointer+=1
                secondPointer-=1
            return True

        def PalindromePartition(ind, result, final_array, s, n):
            if ind>=n:
                result.append(final_array.copy())
                return 
            
            for i in range(ind, n):
                if isPalindrome(s[ind:i+1]):
                    final_array.append(s[ind:i+1])
                    PalindromePartition(i+1, result, final_array, s, n)
                    final_array.pop()
            return result

        result, final_array = [], []
        result = PalindromePartition(0, result, final_array, s, len(s))
        return result