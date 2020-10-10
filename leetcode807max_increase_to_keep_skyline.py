    # https://leetcode.com/problems/max-increase-to-keep-city-skyline/

#     In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

# What is the maximum total sum that the height of the buildings can be increased?

# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: 
# The grid is:
# [ [3, 0, 8, 4], 
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]

# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]

# The grid after increasing the height of buildings without affecting skylines is:

# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

# Notes:

# 1 < grid.length = grid[0].length <= 50.
# All heights grid[i][j] are in the range [0, 100].
# All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

def maxIncreaseKeepingSkyline(grid):
    #function to return max of grid as viewed from side (max of each sub array)
    def maxSide(grid):
        max = []
        for i in range(len(grid)):
            max.append(0)
        print("maxSide to start is " + str(max))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print(grid[i][j])
                if grid[i][j] > max[j]:
                    max[j] = grid[i][j]
        return max
    print("maxSide = " + str(maxSide(grid)))

    #function to return max of grid as viewed from front
    def maxFront(grid):
        max = []
        for i in range(len(grid)):
            max.append(0)
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] > max[j]:
                        max[j] = grid[i][j]
        return max
    print("maxFront = " + str(maxFront(grid)))

    sideView = maxSide(grid)
    frontView = maxFront(grid)

    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            maxBuildingHeight = sideView[i]
            if grid[i][j] < sideView[i] and grid[i][j] < frontView[i]:
                pass

# The grid is:
#      j  j  j  j
# i [ [3, 0, 8, 4], 
# i   [2, 4, 5, 7],
# i   [9, 2, 6, 3],
# i   [0, 3, 1, 0] ]
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
# maxSide = [9, 
#            4, 
#            8, 
#            7]
# maxFront = [9, 4, 8, 7]

maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])


