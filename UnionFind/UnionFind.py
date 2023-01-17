# Note: alpha here refers to the Inverse Ackermann function.


class UnionFind:
    def __init__(self, n: int) -> None:
        """
        Time: O(N)
        Space: O(N)
        """
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        """
        Time: O(alpha(N))
        """
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def unite(self, x: int, y: int) -> None:
        """
        Time: O(alpha(N))
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1

    def connected(self, x: int, y: int) -> bool:
        """
        Time: O(alpha(N))
        """
        return self.find(x) == self.find(y)
