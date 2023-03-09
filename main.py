def twoSum(self, nums: List[int], target: int) -> List[int]:
    #yout ANSWER

    j = 0 #second index
    i = 0 #first index
    for i in range (0, len(nums)):
        sub = target - nums[i]
        j = i
        
        while sub > 0:
            j += 1
            if j == len(nums):
                break
            if sub == nums[j]:
                break

        if j == len(nums):
            continue
        if sub == nums[j]:
            break
        
    return i, j
