#driver.py
#Rena Sha
#Feb 6 2017
"The purpose of this module is to solve an n x n sliding board puzzle"

import sys
import Queue
import time
import rsrc
import puzzleBoard
from sets import Set
import math

#Impt statistics that need to be printed out
nodesExpanded =0
fringeSize =0
maxFringeSize=0
searchDepth=0
maxSearchDepth=0
startTime=0.0
maxRAMUsage = 0
successBoardList = []
boardSet = Set()

def bfs(board):
      #Create a queue and pop in the start board and init stats
      q=Queue.Queue()
      q.put(board)
      global maxFringeSize
      maxFringSize=1
      
      #while first thing you pop off queue isn't successful
      current = q.get()
      currentfringeSize = 1
      while(current.getBoardList()!= successBoardList):
            global maxSearchDepth
            global nodesExpanded
            nodesExpanded = nodesExpanded +1
             #add in up down left right to the queue if not in dict already, then add to dict
            childList = current.getChildren()
            for x in childList:
                  if x not in boardSet:
                        boardSet.add(x)
                        q.put(x)
                        if maxSearchDepth < x.getcostofPath():
                              maxSearchDepth = x.getcostofPath()
            currentfringeSize = q.qsize()
            global maxFringeSize            
            if maxFringeSize < currentfringeSize:
                  maxFringeSize = currentfringeSize
            current = q.get()
      
      global fringeSize
      fringeSize = currentfringeSize-1 #one has been popped out and compared and failed the while statement
      printResults(current)
      
def dfs(board):
      #Create a stack and put in the startboard, initialize values
      stack = [board]
      global maxFringeSize
      maxFringeSize =1
      
      current = stack.pop()
      currentFringeSize = 1
      #while the last one popped out is not successful, add in children
      while(current.getBoardList()!=successBoardList):
            global nodesExpanded
            global maxSearchDepth
            nodesExpanded = nodesExpanded+1
            
            childList = current.getChildren()
            childList.reverse()
            for x in childList:
                  if x not in boardSet:
                        boardSet.add(x)
                        stack.append(x)
                        if maxSearchDepth < x.getcostofPath():
                              maxSearchDepth = x.getcostofPath()
            currentFringeSize = len(stack)
            if len(stack)>maxFringeSize:
                  maxFringeSize = len(stack)
            current = stack.pop()
      
      global fringeSize
      fringeSize = currentFringeSize-1
      printResults(current)

def ast(board):
      #Create a priority queue and throw in start board
      priorityQ = Queue.PriorityQueue()
      priorityQ.put(board)
      global maxFringeSize
      maxFringeSize = 1
      
      #while board popped from queue isn't successful
      current = priorityQ.get()
      while(current.getBoardList()!= successBoardList):
            
            global nodesExpanded
            global maxSearchDepth
            nodesExpanded = nodesExpanded +1
            #add in all children to the set and set their priority values
            childList = current.getChildren()
            for x in childList:
                  if x not in boardSet:
                        boardSet.add(x)
                        x.setPriority(getManhattan(x)+x.getcostofPath())
                        priorityQ.put(x)
                        if maxSearchDepth <x.getcostofPath():
                              maxSearchDepth = x.getcostofPath()
            currentFringeSize = priorityQ.qsize()
            if priorityQ.qsize() > maxFringeSize:
                  maxFringeSize = priorityQ.qsize()
                        
            current = priorityQ.get()
      
      global fringeSize
      fringeSize = currentFringeSize -1
      printResults(current)

def ida(board):
      print

def getManhattan(board):
      distance = 0
      for num in range(1,int(math.pow(board.getboardDepth(),2))):
            rowSuccess = num/board.getboardDepth()
            colSuccess = num % board.getboardDepth()
            trueIndex = board.getBoardList().index(num)
            rowTrue = trueIndex/board.getboardDepth()
            colTrue = trueIndex % board.getboardDepth()
            distance = distance + abs(rowSuccess - rowTrue) + abs(colSuccess - colTrue)
                        
      return distance
      
#deprecated, use iterative solution because recursive runs into stack overflow
def dfsRecursiveMain(board):
      #Create a stack and put in the startboard
      stack = [board]
      dfsRecursive(stack)

#deprecated, use iterative solution because recusive runs into stack overflow
def dfsRecursive(stack):
      #take out from stack
      current = stack.pop()
      
      #Case 0 - it is success or no more in stack, so end
      if current.getBoardList() ==successBoardList:
            printResults(current)
      else:
            #Case 1 - it's not success, we add all neighbors into stack, and then recall the stack
            childList = current.getChildren()
            childList.reverse()
            for x in childList:
                  if getKey(x) not in boardDict:
                        boardDict[getKey(x)] = None
                        stack.append(x)
            dfsRecursive(stack)

def printResults(board):
      print "path_to_goal: "+ str(board.getPath())
      print "cost_of_path: "+str(board.getcostofPath())
      print "nodes_expanded: "+str(nodesExpanded)
      print "fringe_size: "+str(fringeSize)
      print "max_fringe_size: "+str(maxFringeSize)
      print "search_depth: "+str(board.getcostofPath())
      print "max_search_depth: "+str(maxSearchDepth)
      print "running_time: "+str(time.time()-startTime)
      print "max_ram_usage: "

#deprecated, should not be used as Set takes up less space
def getKey(board):
    return str(board.getBoardList())

def getDict():
    for x in boardDict:
        print x

def main():
    
    #resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
    #sys.setrecursionlimit(1000000) ------TO DEBUG THIS! 
    global startTime
    startTime = time.time()
    #print rsrc.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
    
    #Create the board and define the success board 
    boardList= sys.argv[2].split(',')
    boardList= map(int, boardList)
    startboard = puzzleBoard.puzzleBoard(boardList,None,None,0)
    global successBoardList
    successBoardList = startboard.getSuccess()
    
    #Deprecated, do not use
    #If the starting board is a successful board no need to go further
    #if boardList == successBoardList:
        #print a bunch of things
        #print "You have found success on your first try!"
        #sys.exit()
    
    #Add starting board to set of boards
    #is an empty dictionary the best way to implement this?
    global boardSet
    boardSet.add(startboard) #get starting board key
        
    #Execute the algorithm according to what was supplied
    if sys.argv[1] == 'bfs':
        print "Executing Breadth First Search"
        bfs(startboard)
        
    elif sys.argv[1] == 'dfs':
        print "Executing Depth First Search"
        dfs(startboard)
        
    elif sys.argv[1] == 'ast':
        print "Executing A Star Search"
        ast(startboard)
        
    elif sys.argv[1] == 'ida':
        print "Executing IDA Star Search"
        
    else:
        print "Wrong input, please try again."
        sys.exit()
    
    #do more user input error checking if we have time
    #if more than 3 args inputted
    #if second arg isnt a matrix as expected
    

if __name__=='__main__': main()

