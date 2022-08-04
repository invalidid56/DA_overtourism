import math
import random
import sys


class Spot:
    def __init__(self, lat, lon, score, connected=[]):
        self.lat = lat
        self.lon = lon
        self.score = score
        self.connected = connected

    def connect(self, other):
        self.connected.append(other)
        other.connected.append(self)


def make_spots():
    datas = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(5)]
    spots = []
    for data in datas:
        s = Spot(
            lat = data[0],
            lon = data[1],
            score = data[2]
        )
        spots.append(s)

    for s in spots:
        for i in spots:
            if not i == s:
                s.connect(i)

    return spots
    # connect spots


def recommend(start, end, n_to_visit=5, max_distance=1000):
    current_node = start

    def get_value(a: Spot, b: Spot):
        dist = math.sqrt(
            (a.lon-b.lon)**2 + (a.lat-b.lat)**2
        ) + 0.001
        return (a.score+b.score)/dist

    def search(node, i):
        print(i)
        if i < n_to_visit:
            values = []
            history = []

            for child in node.connected:
                c_val, c_nodes = search(node, i+1)
                values.append(
                    get_value(node, child) + c_val
                )
                history.append(c_nodes)

            max_index = values.index(max(values))
            return get_value(node, node.connected[max_index]), history[max_index] + [node.connected[max_index]]

        else:
            return get_value(node, end), [node]

    return search(start, 0)[1].reversed()


spots = make_spots()

print(recommend(start=spots[0],
          end=spots[-1]))