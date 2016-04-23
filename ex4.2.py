#!/usr/bin/python

import json

from svm import SVM

with open('ex4.1-w_vec.json') as file:
    w_vec = json.load(file)
with open('ex2-train-vecs.json') as file:
    train_vecs = json.load(file)
with open('ex2-validation-vecs.json') as file:
    valid_vecs = json.load(file)

max_iter=20

w_vec_list = []
avg_train_err = []
avg_valid_err = []

print("Starting experiments...")
for val in range(-9, 10):
    
    print("  Experiment with val=2**%s" %
        (val if val>=0 else ("(%s)" % val))
      )

    # Build a new svm:
    svm = SVM(w_vec=w_vec, lamb=2**val)

    # Train it
    num_erros = svm.train(train_vecs, max_iter=max_iter)

    # Save the weight vector:
    w_vec_list.append( svm.w_vec )

    # Save the train data:
    avg_train_err.append( float(num_erros)/(max_iter*len(train_vecs)) )

    # Save the validation data:
    avg_valid_err.append( svm.test(valid_vecs) )

min_err = sorted(
    zip(range(-9,10), avg_valid_err),
    key = lambda x : x[1]
  )[0]

min_err_index = list(range(-9,10)).index(min_err[0])

print("The minimum error was with lambda = 2**%s: %s" % min_err)
print("The respective training error was %s" %
    avg_train_err[min_err_index])

with open('ex4.2-w_vec-list.json', 'w') as file:
    file.write(json.dumps(w_vec_list))

with open('ex4.2-avg-train-err.json', 'w') as file:
    file.write(json.dumps(avg_train_err))

with open('ex4.2-avg-validation-err.json', 'w') as file:
    file.write(json.dumps(avg_valid_err))




