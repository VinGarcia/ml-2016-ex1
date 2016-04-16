#!/usr/bin/python

import json

# Read the perceptron weights and vocabulary:
with open('ex3.2-w_vec.json') as file:
    w_vec = json.load(file)
with open('ex2-vocabulary.json') as file:
    vocabulary = json.load(file)

spam_words = sorted(
    zip(vocabulary, w_vec),
    key=lambda x: x[1],
    reverse=True
  )

print("Most positive weights:")

for word, value in spam_words[:15]:
    space = " " * (10-len(word))
    print("  " + word + space + "%.1f" % value)

print()

print("Most negative weights:")
for word, value in spam_words[-15:]:
    space = " " * (9-len(word))
    print("  " + word + space + "%.1f" % value)
