from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)

        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])
        visited = {"0000"}

        while q:
            lock, moves = q.popleft()

            if lock == target:
                return moves

            for i in range(4):
                for change in [1, -1]:

                    digit = (int(lock[i]) + change) % 10

                    new = lock[:i] + str(digit) + lock[i+1:]

                    if new not in dead and new not in visited:
                        visited.add(new)
                        q.append((new, moves + 1))

        return -1