import random


class UnionFind1():
    def __init__(self, n):
        self._count = n
        self._id = [i for i in range(n)]

    def count(self):
        return self._count

    def find(self, p):
        self.validate(p)
        return self._id[p]

    def validate(self, p):
        assert(p >= 0 and p < len(self._id))

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self._id[p] == self._id[q]

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        pid = self._id[p]
        qid = self._id[q]

        if pid == qid:
            return

        for i in range(len(self._id)):
            if self._id[i] == pid:
                self._id[i] = qid

        self._count -= 1


class UnionFind2():
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]

    def count(self):
        return self._count

    def find(self, p):
        self.validate(p)
        while p != self._parent[p]:
            p = self._parent[p]

        return p

    def validate(self, p):
        assert(p >= 0 and p < len(self._parent))

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.find(p) == self.find(q)

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        rootp = self.find(p)
        rootq = self.find(q)

        if rootp == rootq:
            return

        self._parent[rootp] = rootq
        self._count -= 1


class UnionFind3():
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]
        self._size = [1 for i in range(n)]

    def count(self):
        return self._count

    def find(self, p):
        self.validate(p)
        while p != self._parent[p]:
            p = self._parent[p]

        return p

    def validate(self, p):
        assert(p >= 0 and p < len(self._parent))

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.find(p) == self.find(q)

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        rootp = self.find(p)
        rootq = self.find(q)

        if rootp == rootq:
            return

        if self._size[rootp] < self._size[rootq]:
            self._parent[rootp] = rootq
            self._size[rootq] += self._size[rootp]
        else:
            self._parent[rootq] = rootp
            self._size[rootp] += self._size[rootq]

        self._count -= 1


class UnionFind4():
    def __init__(self, n):
        if n < 0:
            raise Exception('Illegal Argument')

        self._count = n
        self._parent = [i for i in range(n)]
        self._rank = [0 for i in range(n)]

    def count(self):
        return self._count

    def find(self, p):
        self.validate(p)
        while p != self._parent[p]:
            self._parent[p] = self._parent[self._parent[p]]
            p = self._parent[p]

        return p

    def validate(self, p):
        assert(p >= 0 and p < len(self._parent))

    def connected(self, p, q):
        self.validate(p)
        self.validate(q)
        return self.find(p) == self.find(q)

    def union(self, p, q):
        self.validate(p)
        self.validate(q)
        rootp = self.find(p)
        rootq = self.find(q)

        if rootp == rootq:
            return

        if self._rank[rootp] < self._rank[rootq]:
            self._parent[rootp] = rootq
        elif self._rank[rootp] > self._rank[rootq]:
            self._parent[rootq] = rootp
        else:
            self._parent[rootq] = rootp
            self._rank[rootp] += 1

        self._count -= 1


class UnionFind5():
    """Quick Union Path Compression Union Find
    """
    def __init__(self, n):
        self._count = n
        self._id = [i for i in range(n)]

    def count(self):
        return self._count

    def find(self, p):
        root = p
        while root != self._id[root]:
            root = self._id[root]
        while p != root:
            newp = self._id[p]
            self._id[p] = root
            p = newp

        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return

        self._id[rootp] = rootq
        self._count -= 1


class UnionFind6():
    """Weighted Quick Union Path Compression Union Find
    """
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]
        self._size = [1 for i in range(n)]

    def count(self):
        return self._count

    def find(self, p):
        root = p
        while root != self._parent[root]:
            root = self._parent[root]
        while p != root:
            newp = self._parent[p]
            self._parent[p] = root
            p = newp

        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return

        if self._size[rootp] < self._size[rootq]:
            self._parent[rootp] = rootq
            self._size[rootq] += self._size[rootp]
        else:
            self._parent[rootq] = rootp
            self._size[rootp] += self._size[rootq]
        self._count -= 1


def test_union_find():
    n = 100
    uf1 = UnionFind1(n)
    uf2 = UnionFind2(n)
    uf3 = UnionFind3(n)
    uf4 = UnionFind4(n)
    uf5 = UnionFind5(n)
    uf6 = UnionFind6(n)

    for i in range(n):
        r1 = random.randint(0, n-1)
        r2 = random.randint(0, n-1)
        uf1.union(r1, r2)
        uf2.union(r1, r2)
        uf3.union(r1, r2)
        uf4.union(r1, r2)
        uf5.union(r1, r2)
        uf6.union(r1, r2)
    print(uf1.count(), uf2.count(), uf3.count(),
          uf4.count(), uf5.count(), uf6.count())

    for i in range(n):
        for j in range(n):
            assert(uf1.connected(i, j) == uf2.connected(i, j))
            assert(uf2.connected(i, j) == uf3.connected(i, j))
            assert(uf3.connected(i, j) == uf4.connected(i, j))
            assert(uf4.connected(i, j) == uf5.connected(i, j))
            assert(uf5.connected(i, j) == uf6.connected(i, j))


if __name__ == '__main__':
    test_union_find()
