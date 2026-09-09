class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstPointer, secondPointer = 0, len(numbers)-1
        while firstPointer < secondPointer:
            if numbers[firstPointer] + numbers[secondPointer] == target:
                return [firstPointer+1, secondPointer+1]
            else:
                if numbers[firstPointer] + numbers[secondPointer] > target:
                    secondPointer-=1
                else:
                    firstPointer+=1