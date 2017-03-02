#puzzleBoard.py
#Leina Sha
#2.6.17
"The purpose of this module is to create a virtual representation of the puzzle board of an n x n sliding tile game"

import math

class puzzleBoard(object):
    
    def __init__(self,boardList,parent,move,cost):

        self.boardList=boardList
        self.boardDepth = int(math.sqrt(len(boardList)))
        self.parent = parent
        self.move = move
        self.costofPath = cost
        self.priority = 0
            
    def getBoardList(self):
        return self.boardList
    
    def getcostofPath(self):
        return self.costofPath
    
    def getboardDepth(self):
        return self.boardDepth
                    
    def setPriority(self,priority):
        self.priority = priority
    
    def getPath(self):
        
        path = []
        current = self
        while(current.move is not None):
            path.append(current.move)
            current = current.parent
        path.reverse()
        
        return path
    
    def visualizeBoard(self):
        rowStart=0
        for num in range(0,self.boardDepth):
            print self.boardList[rowStart:rowStart+self.boardDepth]
            rowStart = rowStart+self.boardDepth
    
    def getSuccess(self):
        success = []
        for num in range(0,int(math.pow(self.boardDepth,2))):
            success.append(num)
        return success
    
    def __eq__(self,other):
        return self.boardList == other.boardList
    
    def __hash__(self):
        return hash(str(self.boardList))
    
    def __cmp__(self,other):
        return cmp(self.priority, other.priority)
    
    #shouldn't be used, there is a more efficient way
    def findZeroTile(self):
        position = boardList.index(0)
        row = position/boardDepth+1
        col = position%boardDepth+1
        print [row,col]
        return [row, col]
    
    #shouldn't be used, there is a more efficient way
    def coordinateToInt(position):
        return (position[0]-1)*boardDepth+position[1]-1
    
    def getChildren(self):
        zeroPosition = self.boardList.index(0)
        childrenList=[]
        if zeroPosition/self.boardDepth > 0:
            childrenList.append(self.getUp(zeroPosition))
        if zeroPosition/self.boardDepth < self.boardDepth-1:
            childrenList.append(self.getDown(zeroPosition))
        if zeroPosition%self.boardDepth > 0:
            childrenList.append(self.getLeft(zeroPosition))
        if zeroPosition%self.boardDepth < self.boardDepth-1:
            childrenList.append(self.getRight(zeroPosition))

        return childrenList
            
    def getUp(self,zero):
        newBoardList = list(self.boardList)
        newBoardList[zero], newBoardList[zero-self.boardDepth] = newBoardList[zero-self.boardDepth], newBoardList[zero]
        return puzzleBoard(newBoardList, self,"Up",self.costofPath+1)
            
    def getDown(self,zero):
        newBoardList = list(self.boardList)
        newBoardList[zero], newBoardList[zero+self.boardDepth] = newBoardList[zero+self.boardDepth], newBoardList[zero]
        return puzzleBoard(newBoardList, self, "Down",self.costofPath+1)
    
    def getLeft(self,zero):
        newBoardList = list(self.boardList)
        newBoardList[zero], newBoardList[zero-1] = newBoardList[zero-1], newBoardList[zero]
        return puzzleBoard(newBoardList, self, "Left",self.costofPath+1)
    
    def getRight(self,zero):
        newBoardList = list(self.boardList)
        newBoardList[zero], newBoardList[zero+1] = newBoardList[zero+1], newBoardList[zero]
        return puzzleBoard(newBoardList, self, "Right",self.costofPath+1)
        
    def printBoard(self):
        #what is the function of self in this parentheses?
        print ("Board: ",self.boardList)
        print ("This is a ",self.boardDepth," x ",self.boardDepth,"board.")
        print ("Path to goal is: ",self.pathtoGoal)
        print ("Cost of path is: ", self.costofPath)
