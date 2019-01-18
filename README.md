# Random-Walk

Implementation of the biased random walk from node2vec.
Python 3 implementation of the Implementation of the biased random walk from node2vec Aditya Grover, Jure Leskovec and Vid Kocijan. node2vec: Scalable Feature Learning for Networks. A. Grover, J. Leskovec. ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 2016.

Most of the codes are from [eliorc/node2vec](https://github.com/eliorc/node2vec).

# Changes

Change the type of walks attribute from list of **str** to list of **int**.
Delete unused class methods, and **merge parallel_generate_walks** into the code.

# Usage

```python
import networkx as nx
from random_walks import RandomWalk

karate_g = nx.read_edgelist('./graph/karate.edgelist')

random_walk = RandomWalk(karate_g, walk_length=3, num_walks=10, p=1, q=1, workers=6)

walklist = random_walk.walks

for w in walklist:
    print(w)

```

# Parameters

1. graph: Input graph `int`
2. walk_length: Number of nodes in each walk (default: 80) `int`
3. num_walks: Number of walks per node (default: 10) `int`
4. p: Return hyper parameter (default: 1) `float`
5. q: Inout parameter (default: 1) `float`
6. weight_key: On weighted graphs, this is the key for the weight attribute (default: 'weight') `str`
7. workers: Number of workers for parallel execution (default: 1) `int`
8. sampling_strategy: Node specific sampling strategies, supports setting node specific 'q', 'p', 'num_walks' and 'walk_length'. Use these keys exactly. If not set, will use the global ones which were passed on the object initialization
9. temp_folder: Path to folder with enough space to hold the memory map of self.d_graph (for big graphs); to be passed joblib.Parallel.temp_folder `str`
