import networkx as nx
from random_walks import RandomWalk

karate_g = nx.read_edgelist('./graph/karate.edgelist')

random_walk = RandomWalk(karate_g, walk_length=3, num_walks=10, p=1, q=1, workers=6)

walklist = random_walk.walks

for w in walklist:
    print(w)
