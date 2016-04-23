#!/usr/bin/python

import json
import matplotlib.pyplot as plt

with open('ex4.1-obj_vec.json') as file:
    obj_vec = json.load(file)

plt.plot(range(1,len(obj_vec)+1), obj_vec, '-o', linewidth=2.2)
plt.savefig('ex4.1-plot.png')
plt.show()
