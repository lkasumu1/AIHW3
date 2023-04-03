#!/bin/bash

# package needed for visualization
pip install graphviz

# visualize example graph --- it will be found in "example.png"
python3 visualize.py example s g

# run BFS and DFS on example graph
python3 driver.py example.csv
