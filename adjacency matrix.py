# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:21:15 2019

@author: Teenu
"""

import networkx as nx
from scipy.linalg import block_diag
list1 = list()
G_asymmetric=nx.DiGraph()
#G_asymmetric.add_edge('A','B')
G_asymmetric.add_edge('A','C')
G_asymmetric.add_edge('A','D')
G_asymmetric.add_edge('A','E')
G_asymmetric.add_edge('B','C')
G_asymmetric.add_edge('B','A')
G_asymmetric.add_edge('B','E')
G_asymmetric.add_edge('E','A')

p=nx.degree(G_asymmetric,'A')
print(p)
nx.spring_layout(G_asymmetric)
nx.draw_networkx(G_asymmetric)
#s=nx.clustering(G_asymmetric,'A')
#print(s)
A = nx.adjacency_matrix(G_asymmetric)
adj = A.toarray()
list1=adj.tolist()
a = list1[0]
b = list1[1]
c = list1[2]
d = list1[3]
e = list1[4]
print(a,b,c,d,e)
s= block_diag(a,b,c,d,e)
#A.setdiag(A.diagonal()*2)
print(s)
