#!/usr/bin/python

import json

from svm import SVM

# Open all files:
with open('ex2-vocabulary.json') as file:
    vocabulary = json.load(file)
with open('ex2-train-vecs.json') as file:
    train_vecs = json.load(file)
with open('ex2-validation-vecs.json') as file:
    valid_vecs = json.load(file)

print("Building SVM...")

svm = SVM(length=len(vocabulary))

print("Start Training...")

# Train the svm:
mistakes = svm.train(train_vecs)

print('The svm missed %s%% classifications on the validation data.' %
    (svm.test(valid_vecs)*100) )

print('Writing weight vector on file.')

with open('ex4.1-w_vec.json', 'w') as file:
    file.write(json.dumps(svm.w_vec))

with open('ex4.1-obj_vec.json', 'w') as file:
    file.write(json.dumps(svm.obj_vec))












