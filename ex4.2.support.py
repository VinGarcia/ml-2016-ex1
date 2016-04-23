#!/usr/bin/python

import json
import matplotlib.pyplot as plt

from svm import SVM

# Load the train data:
with open('ex2-train-vecs.json') as file:
  train = json.load(file)

# Load the experiment output files:
with open('ex4.2-w_vec-list.json') as file:
  w_vec_list = json.load(file)
with open('ex4.2-avg-train-err.json') as file:
  avg_train_err = json.load(file)
with open('ex4.2-avg-validation-err.json') as file:
  avg_valid_err = json.load(file)

# Calculate the minimum validation error:
min_err = min(avg_valid_err)
min_err_idx = avg_valid_err.index(min_err)
min_train_err = avg_train_err[min_err_idx]

lamb = list(range(-9,10))[min_err_idx]

err = 0.0004
sup_vecs_ids = []
w_vec = w_vec_list[min_err_idx]
# Find the support vectors:
for idx, line in enumerate(train):
  Y = -1 if line[0] < 0 else 1
  vec = line[1]
  w_xi = sum( xi*w for (xi,w) in zip(vec, w_vec) )

  if abs(w_xi) <= 1 + err:
    sup_vecs_ids.append(idx)

print(len(sup_vecs_ids))
with open('ex4.2-support-vecs-ids.json', 'w') as file:
    file.write(json.dumps(sup_vecs_ids))

p1, p2 = plt.plot(range(-9,10), avg_valid_err, '-o', range(-9,10), avg_train_err, '-o')
plt.legend([p1,p2], ['Validation Error', 'Train Error'], bbox_to_anchor=(.95,.3))
plt.savefig('ex4.2-avg-validation-err.png')
plt.show()

  





