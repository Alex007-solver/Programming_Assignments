# Comparision Of All Varients Of Uninformed Search

## 1. BFS

BFS explores search space level by level.

Observation:
* it gurantees finf=ding a solution if on exists.
* The solution obtained is **"always the shortest path in terms of numbers of steps."**
* Requires **Large memory** because all nodes at each level must be stored.
* Works well when the goal state is near the initial state.

**In the problem we had observed that BFS has given the solution is minimum number of moves**

## 2. DFS

DFS explores nodes along one branch as deep as possible before backtracking.

Observations:
* Uses less memory compared to BFS.
* May reach te solution quickly if it lies deep in the search tree.
* Does not always give the optimal solution.
* Requires tracking of visited states to avoid revisting the same states repeatedly.

**In the problem we had observed that DFS has solution but, it took more number of setps to reach the goal state**

## 3. DBDFS(Depth bounded Depth First Search)
   
DBDFS is a variation of DFS where the search is restricted to a fixed deoth limit.

Condition:
`depth <= limit`

Observations:
* Prevents DFS form going infinitely deep.
* Helps control the serach depth and computation time.
* if the depth limit is too small, the algorithem cannot reach the goal state.

**In the problem we weren't reached the solution because of small depth limit**

## 4. DFID(Depth First Iteration Deepening)
DFID repeatedly applies depth-limited DFS with gradually increasing limits.

Ovservations:

* Combines the advantages of BFS and DFS.
* Uses much less memory than BFS.
Ensures that the solution found is optimal.
* Avoids the problem of choosing an incorrect depth limit.

**In the probelem we successfully reached the goal state. the solution is same as BFS but used lower memory.**






