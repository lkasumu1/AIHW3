
from collections import defaultdict

'''

  for loading and visualizing graphs G = (V,E) stored in a CSV format.
  Graphs have vertices V with integer heuristic values h(v), for each
  v in V, and edges E with integer weights w(e), for each e in E

'''

# load a graph as a triple h, N, w: the heuristic h(v) and the set
# N(v) of neighbours, for each vertex v in V, and the weight w(e), for
# each edge e in E
def load(lines) :

    v, *heur, es, orientation = (x.strip() for x in lines.readline().split(','))
    assert v == 'v'
    assert es == 'es'
    assert orientation in ['dir', 'undir']
    undir = True if orientation == 'undir' else False

    if heur :
        assert len(heur) == 1
        heur = heur[0]
        assert heur == 'h'

    h = {} # heuristic value h(v), for each v in V
    N_ = defaultdict(set) # set N(v) of neighbours, for each v in V
    w = {} # weight w(e), for each e in E
    for line in lines :
        v, *es = (x.strip() for x in line.split(','))

        h[v] = 0 # h(v) 0 by default
        if heur :
            h[v] = int(es[0])
            es = es[1:]

        for e in es :
            u, *W = (x.strip() for x in e.split(':'))

            N_[v].add(u)
            if undir :
                N_[u].add(v)

            w[(v,u)] = 1 # w(e) 1 by default
            if W :
                assert len(W) == 1
                W = int(W[0])
                w[(v,u)] = W

                if undir :

                    if (u,v) in w :
                        s = 'undirected graph with w({},{}) = {} yet w({},{}) = {}'
                        assert w[(u,v)] == W, s.format(v,u,W,u,v,w[(u,v)])

                    w[(u,v)] = W

    N = {}
    for v in h :
        N[v] = sorted(N_[v]) if v in N_ else []

    return h, N, w


# given a graph, load it, then color the start vertex green and the
# goal vertex red, and dump pdf to filename (.pdf)
def visualize(lines, start = None, goal = None, filename = 'G') :

    import graphviz

    h, N, w = load(lines)

    undir = True
    for e in w :
        v, u = e

        if (u,v) not in w :
            undir = False

        else :
            if w[(u,v)] != w[(v,u)] :
                undir = False

    dot = None
    if undir :
        dot = graphviz.Graph(comment = 'graph {}'.format(filename))
    else :
        dot = graphviz.Digraph(comment = 'digraph {}'.format(filename))

    # vertices

    heur = False
    for v in h :
        if h[v] :
            heur = True

    for v in h :
        dot.node(v, xlabel = '<<font color="magenta">h({}) = {}</font>>'.format(v,h[v]) if heur else '')
        
        if v == start :
            dot.node(v, style = 'filled', fillcolor = 'green')

        if v == goal :
            dot.node(v, style = 'filled', fillcolor = 'red')

    # edges (with weights)

    weights = False
    for e in w :
        if w[e] > 1 :
            weights = True

    drawn = set([])
    for e in w :
        v, u = e

        if undir :
            if (v,u) in drawn or (u,v) in drawn :
                continue

        dot.edge(v, u, label = str(w[e]) if weights else '', fontcolor = 'blue')
        drawn.add((v,u))

    dot.format = 'png'
    dot.render(filename, view=True).replace('\\', '/')
