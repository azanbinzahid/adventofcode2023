import networkx as nx
import itertools


def read(filename='in.txt'):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())

    return data

if __name__ == '__main__':
    data = read()
    g = nx.Graph()
    for line in data:
        nodes = line.replace(':', ' ').split()
        for dest in nodes[1:]:
            g.add_edge(nodes[0],dest,capacity=1)
    for a,b in itertools.combinations(g.nodes(),2):
        cut_size, partition = nx.minimum_cut(g,a,b)
        if cut_size == 3:
            print(len(partition[0])*len(partition[1]))
            break