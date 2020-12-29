from datetime import datetime
from typing import List, Dict, DefaultDict, Tuple, Set
from collections import defaultdict

import numpy as np

class Node:
    def __init__(self, jolts:int):
        self.children:Dict[int,Node] = {}
        self.parents:Dict[int,Node] = {}
        self.jolts = jolts

    def is_exp(self, exp:int):
        return self.jolts + 3 == exp

    def __repr__(self):
        return 'J-{} [{}]'.format(self.jolts, ', '.join(str(x) for x in self.children.values()))

def breadth(adapters, exp):
    graph:Node = Node(0)
    q:List[Node] = [graph]
    d:Dict[int,Node] = {}
    ps:DefaultDict[int, int] = defaultdict(lambda : 0)

    d[0] = graph

    count:int = 0
    while len(q) > 0:
        c = q.pop()
        if c.is_exp(exp):
            #print('reached end', c)
            continue
        for i in range(1, 4):
            if c.jolts + i in adapters:
                if c.jolts + i not in d.keys():
                    new_node = Node(c.jolts + i)
                    c.children[new_node.jolts] = new_node
                    new_node.parents[c.jolts] = c
                    ps[new_node.jolts] += 1
                    d[new_node.jolts] = new_node
                    q.append(new_node)
                else:
                    existing_node = d[c.jolts + i]
                    c.children[existing_node.jolts] = existing_node
                    existing_node.parents[c.jolts] = c
                    ps[existing_node.jolts] += 1

    matrix = np.zeros((max(d.keys())+1, max(d.keys())+1))
    for n in d.values():
        for nc in n.children.values():
            #print('edge {} to {}'.format(n.jolts, nc.jolts))
            matrix[n.jolts][nc.jolts] += 1

    """
    for row in matrix:
        print(row)
    """

    npaths = [0] * (len(matrix) + 1)
    npaths[0] = 1 # len(graph.children)

    for i in range(0, len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[i][j] == 1:
                npaths[j] += npaths[i]
            
    #print('x', npaths)
    #print('answer', npaths[exp - 3])

    return npaths[exp - 3]

    """
    print("^2")
    matrix_2 = matrix ** 8
    for row in matrix_2:
        print(row)
    """

def search_graph(g:Node, visited:Set[int], exp:int):
    count = 0
    for c in g.children.values():
        if c.jolts in visited:
            continue
        if c.is_exp(exp):
            visited.add(c.jolts)
            count += 1

def print_g(g:Node):
    for n in g.children.values():
        print('{}: pc = {}'.format(n.jolts, len(n.parents)))
        print_g(n)

with open("10.txt") as f:
    adapters = set(int(x) for x in f)

#print(adapters)

exp = max(adapters) + 3
#print(exp)
g = breadth(adapters, exp)
print('part2', g)
