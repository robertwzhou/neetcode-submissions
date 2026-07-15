class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed))
        def time(i: int) -> float:
            return (target - ps[i][0]) / ps[i][1]
        fleets = 1
        limiting_time = time(len(ps) - 1)
        for i in range(len(ps) - 2, -1, -1):
            if limiting_time < time(i):
                limiting_time = time(i)
                fleets += 1
        return fleets