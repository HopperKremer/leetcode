#1470 Shuffle the Array
#https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n):
    output = []
    for i in range(n):
        output.append(nums[i])
        output.append(nums[n+i])
    return output

print(shuffle([1,2,3,4,4,3,2,1], 4))
#1,4,2,3,3,2,4,1