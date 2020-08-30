# python3

class MinHeap:
    def __init__(self, num_workers):
        # each worker contains (rank(index), next_free_time)
        self._data = []
        self.n = num_workers
        for i in range(num_workers):
            self._data.append((i, 0))

    def change_priority(self, index, priority):
        old_p = self._data[index][1]
        self._data[index] = (self._data[index][0], priority)
        if priority < old_p:
            self.shift_up(index)
        else:
            self.shift_down(index)

        self.shift_down(index)

    def repair_heap(self):
        for i in range(int(self.n / 2), -1, -1):
            self.shift_down(i)

    def parent(self, i):
        return self._data[int((i-1)/2)]

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def compare_worker(self, worker1, worker2):
        if worker1[1] != worker2[1]:
            return worker1[1] < worker2[1]
        else:
            return worker1[0] < worker2[0]

    def shift_up(self, i):
        while i > 0 and self.compare_worker(self._data[i], self._data[self.parent(i)]):
            self._data[i], self._data[self.parent(i)] = self._data[self.parent(i)], self._data[i]
            i = self.parent(i)


    def shift_down(self, i):
        min_index = i
        left = self.left_child(i)
        if left < self.n and self.compare_worker(self._data[left], self._data[min_index]):
            min_index = left

        right = self.right_child(i)
        if right < self.n and self.compare_worker(self._data[right], self._data[min_index]):
            min_index = right
        if i != min_index:
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.shift_down(min_index)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_workers = [0] * n_jobs
    start_times = [0] * n_jobs
    min_heap = MinHeap(n_workers)
    for i in range(n_jobs):
        assigned_workers[i] = min_heap._data[0][0]
        start_times[i] = min_heap._data[0][1]
        min_heap.change_priority(0, min_heap._data[0][1] + jobs[i])

    for i in range(n_jobs):
        print(assigned_workers[i], start_times[i])

if __name__ == "__main__":
    main()