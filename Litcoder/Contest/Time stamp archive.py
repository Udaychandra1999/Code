import sys

class TimeTravelersArchive:
    def _init_(self):
        # Dictionary to store key-value pairs and their timestamps
        self.data = defaultdict(list)

    def Store(self, key, value, timestamp):
        self.data[key].append((timestamp, value))

    def Retrieve(self, key, timestamp):
        # Check if the key exists in the data
        if key not in self.data:
            return "empty"

        # Retrieve the values associated with the key
        values = self.data[key]

        # Binary search to find the latest value with a timestamp less than or equal to the given timestamp
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        # If no matching timestamp is found, return the latest value with a timestamp less than the given timestamp
        if right >= 0:
            return values[right][1]
        else:
            return "empty"
archive1 = TimeTravelersArchive()

for in_str in sys.stdin:
    in_val = in_str.split(' ')
    if in_val[0] == 'Store':
        archive1.Store(in_val[1], in_val[2], int(in_val[3]))
    elif in_val[0] == 'Retrieve':
        res = archive1.Retrieve(in_val[1], int(in_val[2]))
        print(res)