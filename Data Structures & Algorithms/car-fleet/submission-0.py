class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position
        cars = sorted([(position[i], speed[i]) for i in range(len(position))])
        print(cars)
        # calculate travel times
        times = deque()
        for i in range(len(cars)):
            times.append((target - cars[i][0]) / cars[i][1])
        print(times)

        fleets = 1
        current_fleet = times.pop()
        while times:
            car = times.pop()
            if current_fleet < car:
                current_fleet = car
                fleets += 1
        return fleets