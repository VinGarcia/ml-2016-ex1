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
p = Perceptron(length=len(vocabulary), delta=0.1)

print("Training...")
 
mistakes, ages = p.train(train_vecs)

if p.test(train_vecs) > 0:
    print("Some problem ocurred!")
else:
    print("  mistakes: %s, ages: %s" % (mistakes, ages))

print("Testing...")

mistakes_fraction = p.test(valid_vecs)

print("  Perceptron missed %s%% of the data" % (mistakes_fraction*100))

# Write generated data:
with open('ex3.2-w_vec.json', 'w') as file:
    print("\n  Writing `w_vec` to file...\n")
    file.write(json.dumps(p.w_vec))

            














