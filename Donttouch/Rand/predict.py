import pandas as pd
import numpy as np
import random
import networkx as nx
from tqdm import tqdm
import re
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# # load nodes details
# with open("fb-pages-food.nodes") as f:
#     fb_nodes = f.read().splitlines() 

# load edges (or links)
with open("Output.edges") as f:
    output_edges = f.read().splitlines() 

with open("Initial.edges") as f:
    initial_edges = f.read().splitlines() 


# captture nodes in 2 separate lists
node_list_1 = []
node_list_2 = []

for i in tqdm(output_edges):
  node_list_1.append(i.split(' ')[0])
  node_list_2.append(i.split(' ')[1])

import networkx as nx
  
G = nx.Graph()
O = [(node_list_1[i],node_list_2[i])for i in range(len(node_list_1))]
G.add_edges_from(O)
e = list(G.edges())

# captture nodes in 2 separate lists
node_list_1 = []
node_list_2 = []

for i in tqdm(initial_edges):
  node_list_1.append(i.split(' ')[0])
  node_list_2.append(i.split(' ')[1])

I =  [(node_list_1[i],node_list_2[i])for i in range(len(node_list_1))]
def triadic(e):
  new_edges = []
  
  for i in e:
    a, b = i
  
    for j in e:
      x, y = j
  
      if i != j:
        if a == x and (b, y) not in e and (y, b) not in e:
          new_edges.append((b, y))
        if a == y and (b, x) not in e and (x, b) not in e:
          new_edges.append((b, x))
        if b == x and (a, y) not in e and (y, a) not in e:
          new_edges.append((a, y))
        if b == y and (a, x) not in e and (x, a) not in e:
          new_edges.append((a, x))
  
  return new_edges
  
# print("The possible new edges according to Triadic closure are :")
Pred = triadic(e)
# Pred = [(int(Pred[i][0]),int(Pred[i][1])) for i in range(len(Pred))]
sum=0.0
for i in Pred:
    if(i in I):
        sum= sum +1.0
print('\n\nAccording to Triadic Closure')
print((sum/len(Pred))*100)


print('\n\nAccording to Jaccard')
Pred = list(nx.jaccard_coefficient(G))
Pred = [(Pred[i][0], Pred[i][1])for i in range(len(Pred))]

sum=0.0
for i in Pred:
    if(i in I):
        sum= sum +1.0
print((sum/len(Pred))*100)

print('\n\nAccording to Resource Allocation')
Pred = list(nx.resource_allocation_index(G))
Pred = [(Pred[i][0], Pred[i][1])for i in range(len(Pred))]

sum=0.0
for i in Pred:
    if(i in I):
        sum= sum +1.0
print((sum/len(Pred))*100)

print('\n\nAccording to Adamic Adar Index')
Pred =list(nx.adamic_adar_index(G))
Pred = [(Pred[i][0], Pred[i][1])for i in range(len(Pred))]

sum=0.0
for i in Pred:
    if(i in I):
        sum= sum +1.0
print((sum/len(Pred))*100)

print('\n\nAccording to Preferential Attachment')
Pred =list(nx.preferential_attachment(G))
Pred = [(Pred[i][0], Pred[i][1])for i in range(len(Pred))]

sum=0.0
for i in Pred:
    if(i in I):
        sum= sum +1.0
print((sum/len(Pred))*100)


