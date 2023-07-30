import random
import sys

from app import Mass, Spring
from preprocess import read_file

import networkx as nx

import matplotlib.pyplot as plt

network = read_file()

nodes = set()
edges = dict()

masses = dict()
log = dict()
springs = list()

for entry in network:
    nodes.update([entry[0]])
    edges[frozenset(entry[:2])] = entry[2]

for index in nodes:
    masses[index] = Mass()
    masses[index].position = complex(random.random(), random.random())

for key in masses.keys():
    masses[key].fixed = True
    masses[key].position = 1 + 1j
    break

for key in masses.keys():
    log[key] = []

for item in edges:
    x, y = item

    springs.append(Spring(masses[x], masses[y], relaxed_length=1/edges[item]))

# Simulate
for gen in range(4000):
    # print(f"Generation: {gen}")

    for key in masses.keys():
        masses[key].force = complex(0)

    for s in springs:
        s.update()

    for key in masses.keys():
        m = masses[key]

        m.update(dt=0.1)

        log[key].append(m.position)

last_state = dict()

for key in log.keys():
    x = []
    y = []

    for item in log[key]:
        x.append(item.real)
        y.append(item.imag)

    last_state[key] = [x[-1], y[-1]]

    plt.plot(x, y)

plt.savefig("vis/trajectory.png")
plt.show()

for connection in edges.keys():
    m1, m2 = connection

    x1, y1 = last_state[m1]
    x2, y2 = last_state[m2]

    plt.plot([x1, x2], [y1, y2])

for key in last_state.keys():
    plt.plot(*last_state[key], "ro")

plt.savefig("vis/sim_network.png")
plt.show()

plotting = False

if plotting:
    g = nx.Graph()

    for item in edges:
        x, y = item

        g.add_edge(x, y)

    nx.draw_spring(g)

    plt.savefig("vis/network.png")
