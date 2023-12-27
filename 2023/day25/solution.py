import re
import networkx as nx

with open('./input', 'r') as f:
  data = f.read().strip()

def solve(lines):
  g = nx.Graph()
  for l in lines:
    c, *ns = re.split(r':* ', l)
    g.add_edges_from((c, n) for n in ns)

  g.remove_edges_from(nx.minimum_edge_cut(g))
  a, b = nx.connected_components(g)
  print(len(a) * len(b))


lines = data.split('\n')
solve(lines)