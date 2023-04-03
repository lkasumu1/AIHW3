
import sys
import graph

fname, start, goal = sys.argv[1:]
graph.visualize(open('{}.csv'.format(fname),'r'), start=start, goal=goal, filename=fname)
