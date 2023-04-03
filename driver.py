import sys
import graph
import search

h, N, w = graph.load(open(sys.argv[1], 'r'))

print()
print('Graph structures, h, N and w:')
print()

print('h = ', h)
print()

print('N = ', N)
print()

print('w = ', w)
print()

print('Search orders:')
print()

start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")
print("Greedy " , search.greedy(N, w, start, goal, heuristic=search.null_heuristic))
print("Ucs " , search.uniform_cost_search(N,w, start, goal))
print("A*", search.a_star(N,w,h, start, goal))


# print('UCS:', search.ucs(N))
order = search.BFS(N)
print('BFS:', order)

order = search.DFS(N)
print('DFS:   ',order)

order = search.DFSrec(N)
print('DFSrec:', *order)
