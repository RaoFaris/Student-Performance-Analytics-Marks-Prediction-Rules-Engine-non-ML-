import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
pd.options.mode.chained_assignment = None

sp=pd.read_csv('StudentsPerformance.csv')
sp.head(5)
sp.describe()