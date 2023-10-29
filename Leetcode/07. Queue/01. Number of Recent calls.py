from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)

        # Remove requests that fall outside the time frame (3000 milliseconds)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)


obj = RecentCounter()
result = [None, obj.ping(1), obj.ping(100), obj.ping(3001), obj.ping(3002)]
print(result)
