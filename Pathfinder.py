# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:20:02 2020

@author: franc
"""
import math
from time import sleep 
from os import system
from sys import exit
def clear(): 
  system("cls")
  
maze1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 2, 1, 2, 2, 2, 2, 2],
    [1, 2, 1, 2, 1, 2, 1, 1, 1, 1],
    [1, 2, 1, 2, 1, 2, 1, 2, 2, 1],
    [1, 2, 2, 2, 1, 2, 1, 2, 1, 1],
    [1, 2, 1, 2, 1, 1, 1, 2, 2, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 2, 1, 1]
    ]

def printgame(board):
    dic = {1:"   ", 2:"███", 3:" P ", 0:"   ", "W":"^", "^":"O", "v":"O", "<":"O",">":"O", "a":"A"}
    out = ""
    for i in board:
        out += "]"
        for j in i:
            out += dic[j]
        out += "[\n"
    print(out)

printgrid = lambda grid: [print(i) for i in grid]

class Maze:
    def __init__(self, size):
        self.maze = [[1 for i in range(size)] for j in range(size)]
        
        self.wall = [
            [2,3],
            [2,4],
            [3,4],
            [4,3],
            [4,4],
            [5,4],
            [6,4],
            [7,4],
            [8,4],
            ]
        self.path = []
        
    def wallin(self):        
        for i in range(len(self.wall)):
            self.maze[self.wall[i][0]][self.wall[i][1]] = 2
            
    def pathin(self):        
        for i in range(len(self.path)):
            
            self.maze[self.path[i][0]][self.path[i][1]] = 3
            
    def clear_tiles(self, y, x, end): 
        self.maze[y][x] = 0               
        for j in matrix(y,x, end):
            
            if j == end:
                #print(self.path)
                self.pathin()
                self.maze[j[0]][j[1]] == 3
                printgame(maze.maze)
                #printgrid(maze.maze)
                input("Enter To Exit")
                exit()        
                
                
            if j[0] >= 0 and j[1] >= 0 and j[0] < len(self.maze) and j[1] < len(self.maze):
                if self.maze[j[0]][j[1]] == 1 and j[0] >= 0 and j[1] >= 0 and j[0] < len(self.maze) and j[1] < len(self.maze):
                    self.maze[j[0]][j[1]] = 0
                    
                    #clear()
                    #printgame(self.maze)
                    if [y,x] == self.path[-1]:
                        #print(str((y,x)) + " A " + str(self.path[-1]))
                        self.path.append(j)
                        #print(self.path)
                        
                    else:
                        count = 0
                        u = True
                        while u:
                            #print(count)
                            if self.path[count] == [y,x]:
                                #print("X,Y " + str((x,y))
                                self.path = self.path[:count + 1]
                                u = False
                            count += 1
                        self.path.append(j)    
                            
                            
                    
                    #print("coords " + str(j))
                    self.clear_tiles(j[0],j[1], end)
            # except RecursionError:
            #     print("RecursionError")
            # except:
            #     "a"
        
                            
                           
            
    # def pathfind(self, start, end):
    
    #     paths = []           
    #     pos = [matrix(start[0], start[1])]
    #     a = 1
    #     start = 0
    #     while a > 0:
                       
    #         for path in paths:
                
    #             for j in matrix(y,x):
    #                 try:
                        
    #                     if self.maze[j[0]][j[1]] == 1 and j[0] >= 0 and j[1] >= 0:
    #                         self.maze[j[0]][j[1]] = 0
    #                         clear()
    #                         printgrid(self.maze)
    #                         sleep(0.1)
    #                         #input("Enter")
    #                         pos.append(matrix(j[0],j[1]))
    #                     elif j == end:
    #                         return
    #                 except:
                         
    #                      "a"
            
            
            
            
"""
Always have one path, append to path if at the end, otherwise find position in path and append from that position.
"""            
            
            
def matrix(y,x, end):
    """takes a 2 dimenstional position coordinate and generates a 3x3 matrix 
    around that point, with the first element pointing towards the end coords.
    """
    
    angle = math.degrees(math.atan2(end[1] - x,end[0] - y)) % 360
    #print(angle)
    if angle <=22.5 or 337.5< angle:
        return [[y+1,x],[y+1, x-1],[y+1, x+1],[y, x-1],[y, x+1],[y-1,x-1],[y-1,x+1],[y-1,x]]
    elif 22.5< angle <=67.5:
        return [[y+1, x+1],[y+1,x],[y, x+1],[y+1, x-1],[y-1,x+1],[y, x-1],[y-1,x],[y-1,x-1]]
    elif 67.5< angle <=112.5:
        return [[y, x+1],[y+1, x+1],[y-1,x+1],[y+1,x],[y-1,x],[y+1, x-1],[y-1,x-1],[y, x-1]]
    elif 112.5< angle <=157.5:
        return [[y-1,x+1],[y, x+1],[y-1,x],[y+1, x+1],[y-1,x-1],[y, x-1],[y+1,x],[y+1, x-1]]
    elif 157.5< angle <=202.5:
        return [[y-1,x],[y-1,x-1],[y-1,x+1],[y, x-1],[y, x+1],[y+1, x-1],[y+1, x+1],[y+1,x]]
    elif 202.5< angle <=247.5:
        return [[y-1,x-1],[y-1,x],[y, x-1],[y-1,x+1],[y+1, x-1],[y, x+1],[y+1,x],[y+1, x+1]]
    elif 247.5< angle <=292.5:
        return [[y, x-1],[y-1,x-1],[y+1, x-1],[y-1,x],[y+1,x],[y-1,x+1],[y+1, x+1],[y, x+1]]
    elif 292.5< angle <=337.5:
        return [[y+1, x-1],[y+1,x],[y, x-1],[y+1, x+1],[y-1,x-1],[y, x+1],[y-1,x],[y-1,x+1]]
    # else:
    #     return [[y+1, x-1],[y+1,x],[y, x-1],[y+1, x+1],[y-1,x-1],[y, x+1],[y-1,x],[y-1,x+1]]
    


maze = Maze(10)
maze.maze = [
    [1, 1, 2, 1, 2, 1, 1, 1, 1, 1],
    [1, 1, 2, 1, 2, 1, 1, 1, 1, 1],
    [1, 2, 2, 1, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 2, 2, 2, 2],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
    ]
printgame(maze.maze)
input("Enter To Pathfind")
maze.path.append([9,0])
maze.clear_tiles(9,0, [9,9])





