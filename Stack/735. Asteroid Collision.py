from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            if not stack:
                stack.append(aster)
                continue
            if aster < 0:
                if stack[-1] < 0:
                    stack.append(aster)
                else:
                    while stack[-1] > 0:
                        if abs(aster) > stack[-1]:
                            stack.pop()
                        elif abs(aster) == stack[-1]:
                            stack.pop()
                            break
                        else:
                            break
                        if not stack:
                            stack.append(aster)
                            break
                    else:
                        stack.append(aster)
            else:
                stack.append(aster)
        return stack


s = Solution()
input = [5, 10, -5]
print(s.asteroidCollision(input))
