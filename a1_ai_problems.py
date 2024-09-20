import math

# Complete your individualized AI problems here
"""
You are in a treasure hunt on a grid represented by a 2D list.
 The grid contains 'T' for treasure, 'X' for obstacles, and '.' for open spaces.
 Write a function to find the shortest path to the treasure from a starting point, moving only up, down, left, or right.
 If the treasure is unreachable, return -1.
"""

def hunt(map, x, y):
    if y >= len(map) or x < 0 or y < 0: return -1
    if x >= len(map[y]): return -1
    if map[y][x] == "T": return 0
    if map[y][x] == "X": return -1
    def miny(x, y): return min(x, y) if x >= 0 and y >= 0 else max(x, y)

    newmap = map
    newmap[y][x] = "X"

    min_length = hunt(newmap, x + 1, y)
    min_length = miny(min_length, hunt(newmap, x, y + 1))
    min_length = miny(min_length, hunt(newmap, x, y - 1))
    min_length = miny(min_length, hunt(newmap, x - 1, y))

    return (min_length + 1) if min_length >= 0 else -1

test = [
    ['.', '.', 'X', 'T'],
    ['X', '.', '.', '.'],
    ['.', '.', '.', '.'],
]

#print(hunt(test, 1, 1))

"""
Given an array of integers nums and an integer target, 
return the indices of the two numbers such that they add up to target.
Assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def prob2(arr, i):
    ans = {arr[num]: num for num in range(len(arr))}

    for num in range(len(arr)):
        if i-arr[num] in ans: return [num, ans[i - arr[num]]]

#print(prob2([2, 0, 5, 4, 0], 6))

"""
Three sum
given an integer array nums find all unique triplets in the array which gives the sum of zero
"""

def prob3(arr):
    def prob2a(arr, i):
        ans = set({num for num in arr})
        ans2 = []
        for num in arr:
            if i-num in ans:  ans2.append([num, i - num])
        return ans2
    ans = []

    for i in arr:
        tempy = arr
        tempy.remove(i)
        result = prob2a(tempy, -i)
        if len(result) > 0:
            for peop in result: 
                meow = peop + [i]
                meow.sort()
                ans.append(meow)
    return [t for n, t in enumerate(ans) if t not in ans[:n]]

print(prob3([-1, 0, 1, 2, -1, -4]))