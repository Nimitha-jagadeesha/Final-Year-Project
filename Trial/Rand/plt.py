import pandas as pd
import numpy as np
import random
import networkx as nx
from tqdm import tqdm
import re
import matplotlib.pyplot as plt

df = pd.read_csv('metrics.csv')
df.plot(kind='bar', figsize=(15, 8))
plt.show()
