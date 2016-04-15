#!/usr/bin/python

import json

from perceptron import Perceptron

# Open all files:
with open('ex2-vocabulary.json') as file:
    vocabulary = json.load(file)
with open('ex2-train-vecs.json') as file:
    train_vecs = json.load(file)
with open('ex2-validation-vecs.json') as file:
    valid_vecs = json.load(file)

# Build a clean perceptron:
p = Perceptron(len(vocabulary), delta=0.1)

print("Training...")
 
mistakes, ages = p.train(train_vecs)

print("  mistakes: %s, ages: %s" % (mistakes, ages))

print("Testing...")

mistakes_fraction = p.test(valid_vecs)

print("  Perceptron missed %s%% of the data" % (mistakes_fraction*100))
            
