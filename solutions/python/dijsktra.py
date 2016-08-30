import unittest
from priodict import priorityDictionary # for Two


class Graph_One:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra_one(graph, initial):
    """ from https://gist.github.com/econchick/4666413 """
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
    min_node = None
    for node in nodes:
        if node in visited:
            if min_node is None:
                min_node = node
            elif visited[node] < visited[min_node]:
                min_node = node

    if min_node is None:
        break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
        weight = current_weight + graph.distance[(min_node, edge)]
        if edge not in visited or weight < visited[edge]:
            visited[edge] = weight
            path[edge] = min_node

    return visited, path


def dijsktra_two(G,start,end=None):
	"""
	Find shortest paths from the  start vertex to all vertices nearer than or equal to the end.

	The input graph G is assumed to have the following representation:
	A vertex can be any object that can be used as an index into a dictionary.
	G is a dictionary, indexed by vertices.  For any vertex v, G[v] is itself a dictionary,
	indexed by the neighbors of v.  For any edge v->w, G[v][w] is the length of the edge.
	This is related to the representation in <http://www.python.org/doc/essays/graphs.html>
	where Guido van Rossum suggests representing graphs as dictionaries mapping vertices
	to lists of outgoing edges, however dictionaries of edges have many advantages over lists:
	they can store extra information (here, the lengths), they support fast existence tests,
	and they allow easy modification of the graph structure by edge insertion and removal.
	Such modifications are not needed here but are important in many other graph algorithms.
	Since dictionaries obey iterator protocol, a graph represented as described here could
	be handed without modification to an algorithm expecting Guido's graph representation.

	Of course, G and G[v] need not be actual Python dict objects, they can be any other
	type of object that obeys dict protocol, for instance one could use a wrapper in which vertices
	are URLs of web pages and a call to G[v] loads the web page and finds its outgoing links.

	The output is a pair (D,P) where D[v] is the distance from start to v and P[v] is the
	predecessor of v along the shortest path from s to v.

	Dijkstra's algorithm is only guaranteed to work correctly when all edge lengths are positive.
	This code does not verify this property for all edges (only the edges examined until the end
	vertex is reached), but will correctly compute shortest paths even for some graphs with negative
	edges, and will raise an exception if it discovers that a negative edge has caused it to make a mistake.
	"""

	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()	# estimated distances of non-final vertices
	Q[start] = 0

	for v in Q:
		D[v] = Q[v]
		if v == end: break

		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError, "Dijkstra: found better path to already-final vertex"
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v

	return (D,P)

def shortestPath(G,start,end):
	"""
	Find a single shortest path from the given start vertex to the given end vertex.
	The input has the same conventions as Dijkstra().
	The output is a list of the vertices in order along the shortest path.
	"""

	D,P = Dijkstra(G,start,end)
	Path = []
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path
