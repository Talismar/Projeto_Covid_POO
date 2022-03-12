def aritmetrica(x,y,soma=False, subtracao=False):
    if soma:
        return x + y
    if subtracao:
        return x - y

#print(aritmetrica(5,6,soma=True))

import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasAgg

figura = plt.Figure(figsize=(8,4), dpi=60)
ax = figura.add_subplot(111)

