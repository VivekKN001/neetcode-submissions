class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If length are not equal, then they are already not equal
        if len(s) != len(t):
            return False
        dict1, dict2 = {}, {}
        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        
        for j in t:
            if j not in dict2:
                dict2[j] = 1
            else:
                dict2[j]+=1

        for key, value in dict1.items():
            if key not in dict2.keys():
                return False
            else:
                if dict1[key] != dict2[key]:
                    return False
                else:
                    continue
            
        return True