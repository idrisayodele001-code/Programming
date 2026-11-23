# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:07:42 2026

@author: HP 840 G3
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


aaa = pd.read_excel('student data.xlsx', 'Sheet1')
aaa = aaa.set_index("Name")
print(aaa)

days = list(aaa.columns)             
index = np.arange(len(days))         


bbb = aaa.iloc[0, :]                
ccc = aaa.iloc[1, :]                 
ddd = aaa.iloc[2, :]                 
vvv = aaa.iloc[:3, :]                
print(vvv)

avg = round(aaa.mean(), 2)           
print(avg)

total = aaa.sum(axis=1)             
print(total)


width = 0.25                         
plt.figure(figsize=(9, 5))
plt.bar(index, bbb, width, label='Idris', color='steelblue')
plt.bar(index + width, ccc, width, label='John', color='orange', hatch='//')
plt.bar(index + 2 * width, ddd, width, label='Peter', color='seagreen', alpha=0.7)
plt.plot(index + width, avg, label='Average (all students)',
         color='red', marker='o', linestyle='--')
plt.title("Bar chart: values of 3 students by day")
plt.xlabel("Day")
plt.ylabel("Value")
plt.legend(loc='best')
plt.xticks(index + width, days)
plt.grid(axis='y', linestyle=':')
plt.savefig('chart1_bar.png')
plt.show()


plt.figure(figsize=(9, 5))
markers = ['o', 's', '^', 'D', '*', 'v', 'x', 'P', 'h']
for i in range(len(aaa)):           
    plt.plot(days, aaa.iloc[i, :], marker=markers[i],
             linewidth=1.5, label=aaa.index[i])
plt.plot(days, avg, color='black', linewidth=4, linestyle='--',
         label='Average')          
plt.title("Line chart: all students by day")
plt.xlabel("Day")
plt.ylabel("Value")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()
plt.savefig('chart2_line.png')
plt.show()


explode = [0] * len(total)          
explode[int(np.argmax(total.values))] = 0.1

plt.figure(figsize=(7, 7))
plt.pie(total, labels=total.index, autopct='%1.1f%%',
        explode=explode, startangle=90, shadow=True)
plt.title("Pie chart: share of each student in the weekly total")
plt.savefig('chart3_pie.png')
plt.show()