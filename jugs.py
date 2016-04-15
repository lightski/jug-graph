'''
    jugs.py
    solves the jug problem for 2+ jugs
    accepts commandline input for jugs/capacities and targer
    use: python jugs.py 8 5 3 4
    where 8,5, and 3 are jugs and 4 is target volume
    more info: readme.txt
'''

import sys
from collections import deque

def calc_neighbors(amt, capacity):
#    print(capacity, amt)
    neighbors = list()
    for i in range(len(amt)):
        for j in range(len(capacity)):
            if (i != j) and (amt[i] != 0) and (amt[j] != capacity[j]):
                # pouring i into j
                new_amt = list(amt)
                if amt[j]+amt[i] > capacity[j]: 
                    new_amt[i] = (amt[i] + amt[j]) - capacity[j]
                    new_amt[j] = capacity[j]
                else:
                    new_amt[i] = 0
                    new_amt[j] = amt[j] + amt[i]
                neighbors.append(tuple(new_amt))
#    print("neighbors for ",amt,"are as follows:",neighbors)
    return neighbors


def calc_parent(v, visited, outstr):
    if visited[v][1] == 0:
        outstr += str(v)
        return outstr
    else:
        outstr = outstr + str(v) + "<-" + str(calc_parent(visited[v][1], visited, outstr))
        return outstr


def BFS(capacity, target):
    start = list(0 for i in capacity)
    start[0] = capacity[0]
    first = tuple(start)
    # check for solution in initial state
    if capacity[0] == target or 0 == target: return first
    visited = {first:[0, 0]}
    theq = deque()
    theq.appendleft(first)
    while len(theq) != 0:
        curr = theq.pop()
        for v in calc_neighbors(curr, capacity):
            if v not in visited:
                dist = visited[curr][0] + 1
                par = curr
                visited[v] = [dist, par]
                for val in v:
                    if val == target:
                        # return solution if any number in tuple v is target
                        return calc_parent(v, visited, "")
                theq.appendleft(v)
    return 0


if __name__ == "__main__":
    if not len(sys.argv) > 4:
        print("error: needs more arguments")
        quit()
    else:
        invals = sys.argv[1:len(sys.argv)-1]
        list(map(int, invals))
        capacity = [int(i) for i in invals]
        t = int(sys.argv[len(sys.argv) - 1])
        print("Using jugs",capacity,"to reach",t,"liters")
        res = BFS(capacity,t)
        if res:
            print("Success! Here is the solution (follow arrows <-):\n",res)
        else:
            print("Sorry,",t,"could not be reached\nTry some other values")


