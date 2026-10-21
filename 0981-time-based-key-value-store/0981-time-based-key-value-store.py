class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key, value, timestamp):
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.d:
            return ""

        arr = self.d[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1

        return arr[r][1] if r >= 0 else ""