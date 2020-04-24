import random
import string


class TrieNode():
    def __init__(self):
        self._end = 0
        self._path = 0
        self._map = [None for _ in range(26)]


class Trie():
    def __init__(self):
        self._root = TrieNode()

    def insert(self, s):
        if s is None:
            return

        node = self._root
        for c in s:
            index = ord(c) - ord('a')
            assert(0 <= index < 26)
            if node._map[index] is None:
                node._map[index] = TrieNode()
            node = node._map[index]
            node._path += 1

        node._end += 1

    def delete(self, s):
        if s is None:
            return

        if self.search(s) is False:
            return

        node = self._root
        for c in s:
            index = ord(c) - ord('a')
            assert(0 <= index < 26)
            assert(node._map[index] is not None)
            node = node._map[index]
            node._path -= 1

        node._end -= 1

    def search(self, s):
        if s is None:
            return False

        node = self._root
        for c in s:
            index = ord(c) - ord('a')
            assert(0 <= index < 26)
            if node._map[index] is None:
                return False
            node = node._map[index]

        return node._end != 0

    def prefix_number(self, prefix):
        if prefix is None:
            return 0

        node = self._root
        for c in prefix:
            index = ord(c) - ord('a')
            assert(0 <= index < 26)
            if node._map[index] is None:
                return 0
            node = node._map[index]

        return node._path


def test_trie():
    trie = Trie()

    words = {}
    for _ in range(10000):
        length = random.randint(1, 5)
        s = ''.join([random.choice(string.ascii_lowercase)
                     for __ in range(length)])
        words[s] = 1 if s not in words else words[s]+1
        trie.insert(s)

    for _ in range(1000):
        length = random.randint(1, 3)
        s = ''.join([random.choice(string.ascii_lowercase)
                     for __ in range(length)])
        count = 0
        for w in words:
            if w.startswith(s):
                count += words.get(w, 0)
        assert(count == trie.prefix_number(s))

    for s in list(words):
        assert(trie.search(s) is True)
        trie.delete(s)
        words[s] -= 1

    for s in words:
        if words[s] == 0:
            assert(trie.search(s) is False)
        else:
            assert(trie.search(s) is True)

    print('done')


if __name__ == '__main__':
    test_trie()
