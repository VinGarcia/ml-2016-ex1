#!/usr/bin/python

import json

from vocabulary import Vocabulary as Vocab

with open('spam_train.txt') as file:
    train = file.readlines()
    train = [ (int(line[0]), line[2:]) for line in train ] 

with open('spam_validation.txt') as file:
    valid = file.readlines()
    valid = [ (int(line[0]), line[2:]) for line in valid ] 

# Build the vocabulary
# (a list of distinct words frequent on the emails):
vocab = Vocab(train)

# Build a feature vector for each line of the data:
train = [ (line[0], vocab.get_features(line[1])) for line in train ]
valid = [ (line[0], vocab.get_features(line[1])) for line in valid ]

# Write it down: 
with open('ex2-train-vecs.json', 'w') as file:
    file.write(json.dumps(train))

with open('ex2-validation-vecs.json', 'w') as file:
    file.write(json.dumps(valid))

with open('ex2-vocabulary.json', 'w') as file:
    file.write(json.dumps(vocab.words))


















