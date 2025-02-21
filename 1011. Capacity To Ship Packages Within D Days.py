from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def canShipWithinDays(capacity):
            day_count, current_weight = 1, 0
            for weight in weights:
                if current_weight + weight > capacity:
                    day_count += 1
                    current_weight = 0
                current_weight += weight
            return day_count <= days

        while left < right:
            mid = (left + right) // 2
            if canShipWithinDays(mid):  
                right = mid
            else:
                left = mid + 1

        return left
