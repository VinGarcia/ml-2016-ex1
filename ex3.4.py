#!/usr/bin/python

import json
import matplotlib.pyplot as plt

from perceptron import Perceptron

# Open all files:
with open('ex2-vocabulary.json') as file:
    vocabulary = json.load(file)
with open('ex2-train-vecs.json') as file:
    train_vecs = json.load(file)
with open('ex2-validation-vecs.json') as file:
    valid_vecs = json.load(file)

data_slices = [
    50, 75, 80, 90, 100, 110, 120, 130, 140, 150,
    175, 200, 250, 300, 400, 600, 800, 1200, 1600, 2000, 4000
  ]

plot_ages = []

p = Perceptron(length=len(vocabulary), delta=0.1)

print("Starting experiments...")
for num in data_slices:
    p.resetWeights()
    print("  Using %s lines of the train data... " % num)
    mistakes, ages = p.train(train_vecs[:num])
    plot_ages.append(ages)

plt.plot(data_slices, plot_ages, '-o', linewidth=2.3)
plt.axis([0,max(data_slices),0,max(plot_ages)])
plt.savefig('ex3.4-plot.png')
plt.show()

