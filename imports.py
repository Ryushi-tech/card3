from collections import Counter
from collections import deque
from itertools import permutations
from itertools import combinations
from itertools import product
from functools import reduce
import bisect
import heapq
import math
from math import hypot
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall, shortest_path
import sys
sys.setrecursionlimit(10 ** 7)

import os, io
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

from stop_watch import stop_watch
@stop_watch