#!/bin/bash

for f in cycles example example-weighted 26th
do
    echo "converting: $f.csv (start=s, goal=g) -> $f.png"
    python3 visualize.py $f s g
done

echo "converting: romania.csv (start=Arad, goal=Bucharest) -> romania.png"
python3 visualize.py romania Arad Bucharest
