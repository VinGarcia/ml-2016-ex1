#!/usr/bin/python

import re

class Vocabulary():

    words = []

    def __init__(self, train_data):
        wCounter = {}
        s = set()
    
        # For each line in train:
        for line in train_data:
            # Build a bag:
            w_set = set(re.split('\s+', line[1]))
            for word in w_set:
                # Add it to the feature vector:
                if word not in wCounter:
                    wCounter[word] = 1
                else:
                    wCounter[word] += 1
    
        # Remove any entries that appear in less than 30 e-mails
        aux = { k:v for (k,v) in wCounter.items() if v > 30 }
    
        self.words = list(aux.keys())
        self.len = len(self.words)

    # Build a feature vector for a given text:
    def get_features(self, text):
        email = set(re.split('\s+', text))
        vec = []

        for word in self.words:
            vec.append( int(word in text) )
        
        return vec








