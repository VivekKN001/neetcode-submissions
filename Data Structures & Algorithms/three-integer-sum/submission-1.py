class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
            else:
                # Two Sum Solution with Sorted Array
                leftPointer, rightPointer = index+1, len(nums)-1
                while leftPointer < rightPointer:
                    threeSum = value + nums[leftPointer] + nums[rightPointer]
                    if threeSum > 0:
                        rightPointer -=1
                    elif threeSum < 0:
                        leftPointer +=1
                    else:
                        result.append([value, nums[leftPointer], nums[rightPointer]])
                        leftPointer +=1
                        while (nums[leftPointer] == nums[leftPointer-1]) and leftPointer < rightPointer:
                            leftPointer+=1
        return result
