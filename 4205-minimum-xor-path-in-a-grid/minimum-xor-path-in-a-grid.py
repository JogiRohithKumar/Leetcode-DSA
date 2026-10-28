sm = (1 << (512))-1
swapmasks = [0]*9 + [sm]
for i in range(8, -1, -1):
    sm ^= sm << (1 << i)
    swapmasks[i] = sm

def swap_for(path, cell):
    for i in range(10):
        if cell & (1 << i):
            path = ((path & swapmasks[i]) << (1 << i)) | ((path & (swapmasks[i] << (1 << i))) >> (1 << i))
    return path

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        paths = [0]*n
        xor = grid[0][0]
        paths[0] = 1 << xor
        for c in range(1, n):
            xor ^= grid[0][c]
            paths[c] = 1 << xor
        xor = grid[0][0]
        for r in range(1, m):
            xor ^= grid[r][0]
            paths[0] = 1 << xor
            for c in range(1, n):
                paths[c] = swap_for(paths[c-1] | paths[c], grid[r][c])

        return (paths[n-1] & -paths[n-1]).bit_length() - 1