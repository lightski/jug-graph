# A Problem of Measurement
## Quickstart 
Built for python 3+
Run like this: 
```
	python3 jugs.py 8 5 3 4
```
Where 8 5 3 are jug sizes and 4 is target liters. This implemenation assumes the first jug is full of water and the rest are empty.
Takes any# of input values and the last one is the size

## Background
This is a solution to a homework problem in my algorithms class. I enjoyed writing the solution and thought it may be instructive for others to see so here it is.
The homework problem is: given some jugs of various sizes, for example 8, 5, and 3, how do you get arbitrary quantitites of water? Assume the first jug is full of water and the rest empty. Model the problem as a graph but do not generate an explicit representation.
Solution: generate a graph for the problem by modeling vertices as jug states (amount of water). Edges are generated by the possible pours from one jar into another. Use breadth-first search to traverse the graph and find a solution.
My solution takes any number of jugs and examines the whole graph. It will take a long time to evaluate when given large lists.

## TODO
[]Add support for additional algorithms? Eg depth-first search, djikstra's algorithm, etc.

## Disclaimer
Use this code however you like; I am not responsible for what you do.

