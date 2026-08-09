class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        # If length is not equal
        if len(dict1) != len(dict2):
            return False
            
        for key, value in dict1.items():
            if key not in dict2.keys():
                return False
            else:
                if dict1[key] != dict2[key]:
                    return False
                else:
                    continue
            
        return True