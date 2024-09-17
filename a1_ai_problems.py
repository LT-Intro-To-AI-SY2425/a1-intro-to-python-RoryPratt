# Complete your individualized AI problems here
"""
You are in a treasure hunt on a grid represented by a 2D list.
 The grid contains 'T' for treasure, 'X' for obstacles, and '.' for open spaces.
 Write a function to find the shortest path to the treasure from a starting point, moving only up, down, left, or right.
 If the treasure is unreachable, return -1.
"""

def hunt(map, x, y):
    if y >= len(map): return -1
    if x >= len(map[y]): return -1
    if map[y][x] == "T": return 1
    if map[y][x] == "X": return -1
    def miny(x, y): return min(x, y) if x >= 0 and y >= 0 else -1

    newmap = map
    newmap[y][x] = "X"

    min_length = hunt(newmap, x + 1, y)
    min_length = miny(min_length, hunt(newmap, x, y + 1))
    min_length = miny(min_length, hunt(newmap, x, y - 1))
    min_length = miny(min_length, hunt(newmap, x - 1, y))

    return (min_length + 1) if min_length >= 0 else max(x, y)

test = [
    ['.', '.', 'X', 'T'],
    ['X', '.', 'X', '.'],
    ['.', '.', '.', '.'],
]

print(hunt(test, 0, 0))