# -*- coding: utf-8 -*-
"""
Created on Sun May 18 02:20:16 2014

@author: ankur
"""

COLUMN = 20
ROW = 20

import math
import networkx as nx
import matplotlib.pyplot as plt
import sys

class CPathfinding:
    def __init__(self):

        self.pos = None

    def read_file_draw_graph(self):
	global pos
	with open('sample.txt') as file:
		array2d = [[int(digit) for digit in line.split()] for line in file]
	    
	count = 1 
	G = nx.Graph()    
	for j in range(COLUMN):
		for i in range(ROW):
	            if array2d[ROW-1-i][j] == 0:
	                G.add_node(count,pos=(j,i))
	            count +=1 
	     
	    
	   
	    
	self.pos=nx.get_node_attributes(G,'pos')
	    
	    
	for index in self.pos.keys():
		for index2 in self.pos.keys():
	        	if self.pos[index][0] == self.pos[index2][0] and self.pos[index][1] == self.pos[index2][1] -1 :
	                	G.add_edge(index,index2,weight=1)
	            	if self.pos[index][1] == self.pos[index2][1] and self.pos[index][0] == self.pos[index2][0] -1 :
	                	G.add_edge(index,index2,weight=1)
	    
    	return G
    
    
    def dist(self,a,b):
    	(x1,y1) = self.pos[a]
    	(x2,y2) = self.pos[b]    
    	return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
    
  
    def dijkstra(self,G,source,destination):
    
	    ##Done Dijkstra
	    print nx.dijkstra_path(G,source,destination) 
	    #return G
   
    
if __name__ == "__main__":
    objPathfinding = CPathfinding()
    G = objPathfinding.read_file_draw_graph()
    #nx.draw(G,pos)
    inp = 1
    while (inp != 0):
        inp = raw_input()
        inp2 = raw_input()
        path = nx.astar_path(G,int(inp),int(inp2),objPathfinding.dist)
        print path
    #nx.draw(G,pos,nodelist=path,node_color = 'g') 
    #plt.show()
