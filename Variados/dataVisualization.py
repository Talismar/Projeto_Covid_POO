#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

class dataVisualization:
	def singlePlot(self,col_x, col_y):
		
		#plt.style.use('dark_background')
		
		# make data
		x = (col_x)
		max_value = max(col_y)+(max(col_y)*5//100)
		y = col_y
		
		# plot
		fig, ax = plt.subplots()
		
		ax.plot(x, y, linewidth=2.0, label="DATA")
		ax.set(xlim=(0, len(x)), xticks=np.arange(0, (len(x)), (len(x)*10//100)),
				ylim=(0, max_value), yticks=np.arange(0, max_value, (max_value*10//100)))
		plt.xticks(rotation=45)
		# Put a legend to the right of the current axis
		ax.legend(loc='center left', bbox_to_anchor=(1, 0.8))
		
		#legend (Title, x-label and y-label)
		#ax.set_xlabel('x-label', fontsize=12)
		#ax.set_ylabel('y-label', fontsize=12)
		#ax.set_title('Title', fontsize=12)
		
		plt.show()