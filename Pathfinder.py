# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:20:02 2020

@author: franc
"""
from time import sleep 
from os import system
def clear(): 
  system("cls")

printgrid = lambda grid: [print(i) for i in grid]

class Maze:
    def __init__(self, size):
        self.maze = [[1 for i in range(size)] for j in range(size)]
        self.wall = [
            [2,4],
            [3,4],
            [4,4],
            [5,4],
            [6,4],
            [7,4],
            [8,4],
            ]
        
        
    def wallin(self):
        
        for i in range(len(self.wall)):
            self.maze[self.wall[i][1]][self.wall[i][0]] = 2
    def pathfind(self, start, end):
        path = []           
        pos = [matrix(start[0], start[1])]
        a = 1
        start = 0
        while a > 0:
            
            pos = pos[start:]
            start = len(pos)
            for i in pos:
                
                for j in i:
                    try:
                        #print("j = " + str(j))
                        if self.maze[j[0]][j[1]] == 1 and j[0] >= 0 and j[1] >= 0:
                            self.maze[j[0]][j[1]] = 0
                            clear()
                            printgrid(self.maze)
                            sleep(0.1)
                            pos.append(matrix(j[0],j[1]))
                            
                            
                            
                            
                    except:
                         
                         "a"
            a = len(pos)
            
            
            
            
            
            
def matrix(y,x):
    """takes a 2 dimenstional position coordinate and generates a 3x3 matrix 
    around that point
    """
    return [[y-1,x-1],[y-1,x],[y-1,x+1],[y, x-1],[y, x+1],[y+1, x-1],[y+1,x],[y+1, x+1]]


maze = Maze(10)
maze.wallin()
printgrid(maze.maze)
maze.pathfind((1,1), (9,9))