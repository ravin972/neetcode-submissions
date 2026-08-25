class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p = [(position[i], speed[i]) for i in range(len(position))]
        p.sort()
        stack = []
        for param in p:
            time_to_target = (target-param[0])/param[1]
            while stack and time_to_target >= stack[-1]:
                stack.pop()
            stack.append(time_to_target)
        return len(stack)