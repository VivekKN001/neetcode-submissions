class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftPointer, rightPointer = 0, len(nums)-1
        while leftPointer < rightPointer:
            mid = leftPointer + (rightPointer-leftPointer)//2
            if nums[mid] > nums[rightPointer]:
                leftPointer = mid+1
            else:
                rightPointer = mid
        return nums[leftPointer]


