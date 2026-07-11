class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map and len(self.time_map[key]) and self.time_map[key][0][1] <= timestamp:
            time_map_key = self.time_map[key]
            l, r = 0, len(time_map_key)
            while l < r:
                m = l + (r - l) // 2
                if timestamp < time_map_key[m][1]:
                    r = m
                elif m + 1 < len(time_map_key) and time_map_key[m+1][1] <= timestamp:
                    l = m + 1
                else:
                    return time_map_key[m][0]
        return ""
