class Solution:
    def solve1(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        def isValid(n):
            l, r = 0, len(arr2)-1
            while l <= r:
                m = (l+r)//2
                if abs(n - arr2[m]) <= d:
                    return False
                elif arr2[m] < n:
                    l = m + 1
                else:
                    r = m - 1
            return True
        return sum(isValid(n) for n in arr1)
    def solve2(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for n in arr1:
            l = bisect_left(arr2, n - d)
            r = bisect_right(arr2, n + d)
            ans += 1 if l == r else 0
        return ans
    def solve3(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for n in arr1:
            mn = inf
            idx = bisect_left(arr2, n)
            if idx < len(arr2):
                mn = min(mn, arr2[idx] - n)
            if idx > 0:
                mn = min(mn, n - arr2[idx-1])
            res += 1 if mn > d else 0
        return res
    def mock(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        arr2.sort()
        for n in arr1:
            idx = bisect_left(arr2, n)
            dist = inf
            if idx < len(arr2):
                dist = arr2[idx] - n
            if idx > 0:
                dist = min(dist, n - arr2[idx-1])
            res += 1 if dist > d else 0
        return res
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return self.mock(arr1, arr2, d)