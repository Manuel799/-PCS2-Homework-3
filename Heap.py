import heapq

class Heap(object):
    def __init__(self):
        self.contentmin=[]
        self.contentmax=[]

    def add(self, value):
       heapq.heappush(self.contentmin, value)
       heapq.heappush(self.contentmax, -value)
    def finding_max(self):
        return -self.contentmax[0]
    def finding_min(self):
        return self.contentmin[0]


b = Heap()

import random
import matplotlib.pyplot as plt
for r in range(100):
    num = random.randint(0,1000)
    b.add(num)
    my_min = b.finding_min()
    my_max = b.finding_max()

import time


def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.finding_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.finding_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max


if __name__ == '__main__':
    a = Heap()
    a.add(5)
    print(a.contentmin, a.contentmax, a.finding_min(), a.finding_max())
    a.add(7)
    print(a.contentmin, a.contentmax, a.finding_min(), a.finding_max())
    a.add(3)
    print(a.contentmin, a.contentmax, a.finding_min(), a.finding_max())
    a.add(9)
    print(a.contentmin, a.contentmax, a.finding_min(), a.finding_max())

    repetitions = 5
    max_operations = 20000
    step = 5000

    values_heap_add, values_heap_min, values_heap_max = [], [], []
    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 20000))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0

        for repetition in range(5):
           a = Heap()
           myadd, mymin, mymax = measure_time(a, this_list)
           tot_time_add += myadd
           tot_time_min += mymin
           tot_time_max += mymax

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        values_heap_add.append(tot_time_add * 1000)
        values_heap_min.append(tot_time_min * 1000)
        values_heap_max.append(tot_time_max * 1000)



    xlabels = range(step, max_operations, step)
    plt.plot(xlabels, values_heap_add, label='Adding')
    plt.plot(xlabels, values_heap_min, label='FindingMin')
    plt.plot(xlabels, values_heap_max, label='FindingMax')
    plt.legend()
    plt.xlabel("# Operations")
    plt.ylabel("T(execution) (msec)")
    plt.title("Performance of Heap")
    plt.show()
