#https://leetcode.com/problems/non-decreasing-array/
#nums = [4,2,3]
#nums = [4,2,1]

def checkPossibility(nums):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i+1]:
            count += 1
    if count <= 1:
        return True
    return False

print(str(checkPossibility([4,2,3])))
print(str(checkPossibility([4,2,1])))
print(str(checkPossibility([3,4,2,3])))