
class Perceptron():
    
    def __init__(self, **kw):
        self.delta = kw.pop('delta', 0.1)

        if 'data' in kw:
            self.len = len(kw['data'][0][1])
            self.w_vec = [0] * self.len
            self.train(kw['data'])
        elif 'w_vec' in kw:
            self.w_vec = kw['w_vec']
            self.len = len(self.w_vec)
        elif 'length' in kw:
            self.len = kw['length']
            self.w_vec = [0] * self.len
        else:
            raise Exception("Missing necessary arguments!")

    # Receive a table with two columns:
    #   class, feature_vec
    #
    # And return a vector with the predicted
    # classes for each line of the table.
    def test(self, test_data):
        error = []
        for Class, Vec in test_data:
            error.append(abs(Class-self.classify(Vec)))

        return sum(error)/len(error)
        
    # Return a prediction for the vector class in range [0,1]
    def classify(self, vector):
        if len(vector) != self.len:
            raise Exception(
                "The length of the vector should match %s!" % self.len)

        vector = [ v*w for (v,w) in zip(vector, self.w_vec) ]
        return self.activation(sum(vector))

    # Discard old weight vector, and make a new clean one.
    def resetWeights(self):
        self.w_vec = [0] * self.len

    # Receive a table with two columns:
    #   class, feature_vec
    #
    # train data until there is no more mistakes being made.
    # Then return the total number of mistakes and the total
    # number of iterations through the data.
    def train(self, train_data, max_iter=None, verbose=False):
        epochs = 1;

        if verbose:
            print("On epoch 0")
        m_total = mistakes = self.train_epoch(train_data)

        while(mistakes != 0 and (max_iter==None or epochs<max_iter)):
            if verbose:
                print("On epoch %s" % epochs)
            mistakes = self.train_epoch(train_data)
            m_total += mistakes
            epochs += 1
        return m_total, epochs

    # Receive a table with two columns:
    #   class, feature_vec
    #
    # and return True only if all tests
    # matched their respective classes.
    # Return false otherwise.
    def train_epoch(self, train_data):
        mistakes = 0

        for idx, (exp, vec) in enumerate(train_data):
            # Check the difference between the
            # expected and the actual value:
            diff = exp - self.classify(vec)
    
            # If it matched correctly:
            if diff != 0:
                # Update the weights:
                delta = diff * self.delta
                self.w_vec = [
                    (w+delta if v>0 else w)
                    for (v,w) in zip(vector, self.w_vec)
                  ]
                mistakes += 1

        return mistakes

    def activation(self, num):
        if num >= 0:
            return 1
        else:
            return 0
