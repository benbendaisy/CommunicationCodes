from fractions import Fraction
class Solution:
    def maxPoints1(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        n = len(points)
        max_count = 1  # At least one point is always present
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 0
            cur_max = 0
            
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:  # Duplicate point
                    duplicate += 1
                    continue
                
                # Use a fraction to avoid floating-point precision errors
                # slope = float('inf') if dx == 0 else Fraction(dy, dx)
                slope = float('inf') if dx == 0 else dy/dx # can use Ffraction to avoid precision error
                
                slopes[slope] += 1
                cur_max = max(cur_max, slopes[slope])
            
            max_count = max(max_count, cur_max + duplicate + 1)  # +1 for the reference point
        
        return max_count
    
    def maxPoints2(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n, max_cnt = len(points), 1
        for i in range(n):
            slopes, duplicate = defaultdict(int), 0
            cur_cnt = 0
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                
                slope = float('inf') if dx == 0 else Fraction(dy, dx)
                slopes[slope] += 1
                cur_cnt = max(cur_cnt, slopes[slope])
            max_cnt = max(max_cnt, cur_cnt + duplicate + 1)
        return max_cnt