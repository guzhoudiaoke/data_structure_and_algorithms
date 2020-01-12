import sys
import random
import string


class Record():
    def __init__(self):
        self.record = {}

    def update(self, index_map, s, index):
        if s not in self.record:
            self.record[s] = {}

        s_map = self.record[s]
        for k, i in index_map.items():
            if k == s:
                continue

            k_map = self.record[k]
            cur_min = index - i
            if k in s_map:
                pre_min = s_map[k]
                if cur_min < pre_min:
                    k_map[s] = cur_min
                    s_map[k] = cur_min
            else:
                k_map[s] = cur_min
                s_map[k] = cur_min

    def setup(self, arr):
        index_map = {}
        for index, s in enumerate(arr):
            self.update(index_map, s, index)
            index_map[s] = index

    def min_distance(self, s1, s2):
        if s1 is None or s2 is None:
            return -1

        if s1 == s2:
            return 0

        if s1 in self.record and s2 in self.record[s1]:
            return self.record[s1][s2]

        return -1


def min_distance(arr, s1, s2):
    if arr is None or len(arr) == 0 or s1 is None or s2 is None:
        return -1
    if s1 == s2:
        return 0

    pos1, pos2 = -1, -1
    ans = sys.maxsize
    for i in range(len(arr)):
        if arr[i] == s1:
            pos1 = i
            if pos2 != -1:
                ans = min(ans, i-pos2)
        elif arr[i] == s2:
            pos2 = i
            if pos1 != -1:
                ans = min(ans, i-pos1)

    return -1 if ans == sys.maxsize else ans


def test_min_distance():
    arr = []
    for _ in range(20):
        size = random.randint(0, 10)
        s = ''.join([random.choice(string.ascii_letters) for _ in range(size)])
        arr.append(s)

    arr *= 5
    random.shuffle(arr)

    record = Record()
    record.setup(arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            s1 = arr[i]
            s2 = arr[j]
            d1 = min_distance(arr, s1, s2)
            d2 = record.min_distance(s1, s2)
            if d1 != d2:
                print(s1, s2, d1, d2)
                raise Exception('Error')

    print('done')


if __name__ == '__main__':
    test_min_distance()
