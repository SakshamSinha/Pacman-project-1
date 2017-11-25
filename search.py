# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    start_state= problem.getStartState()

    stack=util.Stack()                      #using stack as a fringe
    stack.push([start_state,None,0])
    visited=[]                              #list to keep track of visited nodes
    path=[]                                 #List to store the path directions
    parentSeq={}                            #Dictionary to store child parent relationships. Child is the key and Parent is the value
    while stack.isEmpty()==False:
        current_fullstate=stack.pop()
        if(problem.isGoalState(current_fullstate[0])):
            break
        else:
            current_state=current_fullstate[0]
            if current_state not in visited:
                visited.append(current_state)
            else:
                continue
            successors=problem.getSuccessors(current_state)
            for state in successors:
                #if state[0] not in visited:
                stack.push(state)
                parentSeq[state] = current_fullstate

    child=current_fullstate
    while (child!=None):                        #Loop to form the path from the expanded nodes. Start from the last expanded node and look for the parent.
        path.append(child[1])                   #Repeat until the parent of the current state is None.
        if child[0]!=start_state:               #keep storing the actions in the path as the loop iterates
            child=parentSeq[child]
        else:
            child=None
    path.reverse()                       #since the actions starts from child to parent. So reversed the list.
    return path[1:]         #Since action to reach the first node i.e. the root node is None. Hence remove the first element
                            #and return the path.

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()

    queue = util.Queue()                        #same as DFS. Only Difference is the fringe which now is the queue.
    queue.push([start_state, None, 0])
    visited = []
    path = []
    parentSeq = {}
    while queue.isEmpty() == False:
        current_fullstate = queue.pop()
        if (problem.isGoalState(current_fullstate[0])):
            break
        else:
            current_state = current_fullstate[0]
            if current_state not in visited:
                visited.append(current_state)
            else:
                continue
            successors = problem.getSuccessors(current_state)
            for state in successors:
                if state[0] not in visited:
                    queue.push(state)
                    parentSeq[state] = current_fullstate

    child = current_fullstate
    while (child != None):
        path.append(child[1])
        if child[0] != start_state:
            child = parentSeq[child]
        else:
            child = None
    path.reverse()
    return path[1:]

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    pqueue = util.PriorityQueueWithFunction(lambda x: x[2])         #same as DFS. Only Difference is the fringe which
    pqueue.push((start_state,None,0))                               #now is the priority queue with function. Used Lambda function to extract the cost from the state.
    cost=0                                                          #if x is the state, then x[2] is the cost.
    visited = []
    path = []
    parentSeq = {}
    parentSeq[(start_state,None,0)]=None
    while pqueue.isEmpty() == False:
        current_fullstate = pqueue.pop()
        # print current_fullstate
        if (problem.isGoalState(current_fullstate[0])):
            break
        else:
            current_state = current_fullstate[0]
            if current_state not in visited:
                visited.append(current_state)
            else:
                continue
            successors = problem.getSuccessors(current_state)
            for state in successors:
                cost= current_fullstate[2] + state[2];
                #print state,cost
                if state[0] not in visited:
                    pqueue.push((state[0],state[1],cost))
                    #parentSeq[state] = current_fullstate
                    parentSeq[(state[0],state[1])] = current_fullstate

    child = current_fullstate

    while (child != None):
        path.append(child[1])
        if child[0] != start_state:
            child = parentSeq[(child[0],child[1])]
        else:
            child = None
    path.reverse()
    return path[1:]

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    pqueue = util.PriorityQueueWithFunction(lambda x: x[2]+heuristic(x[0],problem)) #same as UCS. Just added heuristic to
    pqueue.push((start_state, None, 0))                                             #cost to reach the state. So if x is that state
    cost = 0                                                                    #then x[2] is the cost to reach that state, and heuristic(state,problem) is the heuristic.
    visited = []                                                                #Hint to Heuristic function parameters got from nullHeuristic function definition above
    path = []
    parentSeq = {}
    parentSeq[(start_state, None, 0)] = None
    while pqueue.isEmpty() == False:
        current_fullstate = pqueue.pop()
        # print current_fullstate
        if (problem.isGoalState(current_fullstate[0])):
            break
        else:
            current_state = current_fullstate[0]
            if current_state not in visited:
                visited.append(current_state)
            else:
                continue
            successors = problem.getSuccessors(current_state)
            for state in successors:
                cost = current_fullstate[2] + state[2];
                # print state,cost
                if state[0] not in visited:
                    pqueue.push((state[0], state[1],cost))
                    # parentSeq[state] = current_fullstate
                    parentSeq[(state[0], state[1])] = current_fullstate

    child = current_fullstate

    while (child != None):
        path.append(child[1])
        if child[0] != start_state:
            child = parentSeq[(child[0], child[1])]
        else:
            child = None
    path.reverse()
    return path[1:]


    return []

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
