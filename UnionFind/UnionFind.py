# Note: `a` refers to the inverse Ackermann function.


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
        Time: O(a(N))
        """
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        """
        Time: O(1)
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.root[x_root] = y_root
            elif self.rank[y_root] < self.rank[x_root]:
                self.root[y_root] = x_root
            else:
                self.root[x_root] = y_root
                self.rank[y_root] += 1

    def connected(self, x: int, y: int) -> bool:
        """
        Time: O(a(N))
        """
        return self.find(x) == self.find(y)
