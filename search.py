
'''

  for performing various search strategies on graphs G = (V,E) of
  vertices V and edges E, input as the set N(v) of neighbours for each
  v in V

'''

# for a graph input as neighbourhood set N, perform breadth-first
# search (BFS) for a goal vertex starting from some start vertex



import heapq
import math
from queue import PriorityQueue


def BFS(N, start = 's', goal = 'g') :

    order = [] # the order in which vertices are visited

    queue = [start]
    while queue :

        v = queue.pop(0)
        order.append(v)

        if v == goal :
            return order
        
        queue += N[v]


# for a graph input as neighbourhood set N, perform depth-first
# search (DFS) for a goal vertex starting from some start vertex
def DFS(N, start = 's', goal = 'g', giveup = 100) :

    order = [] # the order in which vertices are visted

    stack = [[start]]
    i = 0
    while stack :

        i += 1
        if i > giveup :
            return order, '<- gave up after {} iterations'.format(giveup)

        # should the list at the top of the stack be empty
        if not stack[-1] :
            stack.pop()
            continue

        v = stack[-1].pop()
        order.append(v)

        if v == goal :
            return order, ''

        stack.append(list(reversed(N[v])))


# for a graph input as neighbourhood set N, perform depth-first search
# (DFS) for a goal vertex starting from some start vertex, using
# recursion to do so
def DFSrec(N, start = 's', goal = 'g', giveup = 100) :

    order = [] # the order in which vertices are visted

    DFSaux(order, start, N, goal, 0, giveup)

    log = ''
    if len(order) > giveup :
        log = '<- gave up after recursion depth {}'.format(giveup)

    return order, log


# auxiliary function for DFSrec which does the actual recursion,
# inspired by:
# https://stackoverflow.com/questions/70550888/how-i-can-stop-depth-first-search-at-specific-node
def DFSaux(order, v, N, goal, i, giveup) :

    order.append(v)

    if v == goal :
        return True

    if i > giveup :
        return True

    for u in N[v] :
        if DFSaux(order, u, N, goal, i+1, giveup) :
            return True

    return False

def null_heuristic(h, v, goal):
    return 0

def greedy(N, h, start, goal, heuristic=null_heuristic):
    beg = PriorityQueue()
    beg.put((0, start))
    visited = set()
    route = {start: [start]}
    while not beg.empty():
        current_cost, current_node = beg.get()
        if current_node not in visited:
            visited.add(current_node)
            if current_node == goal:
                return route[current_node]
            neighbors = [neighbor for neighbor in N[current_node] if neighbor not in visited]
            for neighbor in neighbors:
                priority = heuristic(h, neighbor, goal)
                beg.put((priority, neighbor))
                route[neighbor] = route[current_node] + [neighbor]
    return []

def uniform_cost_search(N,w, start, goal):
    beg = PriorityQueue()
    searched = set()
    searched_list = list()
    route = {}
    dist = {}
    order = []
    for node in N.keys():
        dist[node] = math.inf
    dist[start] = 0
    beg.put((0, start))
    while not beg.empty():
        curr_cost, curr_node = beg.get()
        if curr_node == goal:
            break
        if curr_node not in searched:
            searched_list.append(curr_node)
            searched.add(curr_node)
            order.append(curr_node)
            for neighbor in N[curr_node]:
                edge_cost = w.get((curr_node, neighbor), w.get((neighbor, curr_node), None))
                if edge_cost is None:
                    continue
                new_cost = curr_cost + edge_cost
                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    route[neighbor] = curr_node
                    beg.put((new_cost, neighbor))
    res = []
    cur = goal
    while cur != start:
        res.append(cur)
        cur = route.get(cur)
        if cur is None:
            return [], 0, []
    res.append(start)
    total_cost = dist[goal]
    order.append(goal)
    return searched_list, total_cost, order

def a_star(N ,w, h,  start, goal):
    queue = [(h[start], start)]
    location = {}
    cost = {start: 0}

    while queue:
        _, current = heapq.heappop(queue) 
        if current == goal: 
            order = []
            while current != start:
                order.append(current)
                current = location[current]
            order.append(start)
            order.reverse()
            return order
        for neighbor in N[current]:
            new_cost = cost[current] + w[(current, neighbor)]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + h[neighbor]
                heapq.heappush(queue, (priority, neighbor))
                location[neighbor] = current
    return None



