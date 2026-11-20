
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pq:
            time, r, c = heapq.heappop(pq)

            if r == n - 1 and c == m - 1:
                return time

            if time > dist[r][c]:
                continue

            cost = 1 if (r + c) % 2 == 0 else 2

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    newTime = max(time, moveTime[nr][nc]) + cost

                    if newTime < dist[nr][nc]:
                        dist[nr][nc] = newTime
                        heapq.heappush(pq, (newTime, nr, nc))

        return -1
