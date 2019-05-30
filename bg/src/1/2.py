from collections.abc import Iterable


class PriorityQueue(object):
    def __init__(self, source=None):
        if source is None:
            source = []
        if not isinstance(source, Iterable):
            raise TypeError("'{s_type}' object is not iterable".format(s_type=type(source).__name__))

        self.data = [i for i in source]
        self.build_priority_queue()

    def __str__(self):
        return self.data.__str__()

    def __len__(self):
        return self.data.__len__()

    def build_priority_queue(self):
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self.max_heapify((self.data, len(self.data)), i)

    def maximum(self):
        return self.data[0] if len(self.data) else None

    def extract_max(self):
        if len(self.data) > 0:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            res = self.data.pop()
            self.max_heapify((self.data, len(self.data)), 0)
            return res
        else:
            return None

    def increase_keys(self, x, k):
        if x >= len(self.data):
            raise IndexError('PriorityQueue index out of range')

        if k < 0:
            raise ValueError('PriorityQueue can not increase a negative value')

        self.data[x] += k

        i = x
        while i != 0:
            i = self.parent(i)
            self.max_heapify((self.data, len(self.data)), i)

    def insert(self, x):
        self.data.append(x)

        i = len(self.data) - 1
        while i != 0:
            i = self.parent(i)
            self.max_heapify((self.data, len(self.data)), i)

    @staticmethod
    def max_heapify(source: tuple, index: int) -> None:
        heap_size = source[1]
        source = source[0]

        l = PriorityQueue.left(index)
        r = PriorityQueue.right(index)
        largest = index

        if l < heap_size and source[l] > source[largest]:
            largest = l

        if r < heap_size and source[r] > source[largest]:
            largest = r

        if largest != index:
            source[largest], source[index] = source[index], source[largest]
            PriorityQueue.max_heapify((source, heap_size), largest)

    @staticmethod
    def left(index: int) -> int:
        return index * 2 + 1

    @staticmethod
    def right(index: int) -> int:
        return index * 2 + 2

    @staticmethod
    def parent(index: int) -> int:
        return (index - 1) // 2


if __name__ == '__main__':
    pq_a = PriorityQueue([1, 2, 3, 4, 5, 6, 7, 12, 1, 2, 3])
    print(pq_a)

    print(pq_a.maximum())

    pq_a.increase_keys(6, 10)
    print(pq_a)

    pq_a.insert(24)
    print(pq_a)

    for i in range(len(pq_a)):
        print(pq_a.extract_max())
