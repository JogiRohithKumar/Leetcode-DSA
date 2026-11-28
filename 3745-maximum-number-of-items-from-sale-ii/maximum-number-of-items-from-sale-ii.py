import collections

class Solution(object):
    def maximumSaleItems(self, items, budget):
        max_factor = max(f for f, _ in items)
        
        cnt = [0] * (max_factor + 1)
        min_p = float('inf')
        for f, price in items:
            cnt[f] += 1
            if price < min_p:
                min_p = price
                
        total_multiples = [0] * len(cnt)
        for i in range(1, len(total_multiples)):
            if not cnt[i]:
                continue
            for j in range(i, len(total_multiples), i):
                total_multiples[i] += cnt[j]
        group = collections.defaultdict(int)
        for f, price in items:
            if price >= 2 * min_p:
                continue
            group[price] += (total_multiples[f] - 1)
            
        result = 0
        
        for p in sorted(group):
            if budget < p:
                break
            copies_to_buy = min(group[p], budget // p)
            result += 2 * copies_to_buy
            budget -= copies_to_buy * p
            
        result += budget // min_p
        return result