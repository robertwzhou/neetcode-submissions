class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars by position, but include speeds
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        
        stack = deque()
        # if a new car takes more time to reach target, add to stack
        for pos, spe in cars:
            time = (target - pos) / spe
            if len(stack) == 0 or stack[-1] < time:
                stack.append(time)
        # else, discard it
        return len(stack)