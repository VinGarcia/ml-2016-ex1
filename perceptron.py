
class Perceptron():
    
    def __init__(self, length, delta=0.1):
        self.len = length
        self.delta = delta
        self.w_vec = [0] * length

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
            raise Exception("The length of the vector should match %s!" % self.len)

        vector = [ v*w for (v,w) in zip(vector, self.w_vec) ]
        return self.activation(sum(vector))

    # Receive a table with two columns:
    #   class, feature_vec
    #
    # train data until there is no more mistakes being made.
    # Then return the total number of mistakes and the total
    # number of iterations through the data.
    def train(self, train_data):
        ages = 0;
        m_total = mistakes = self.train_all_once(train_data)
        while(mistakes != 0):
            mistakes = self.train_all_once(train_data)
            m_total += mistakes
            ages += 1
        return m_total, ages

    # Receive a table with two columns:
    #   class, feature_vec
    #
    # and return True only if all tests
    # matched their respective classes.
    # Return false otherwise.
    def train_all_once(self, train_data):
        mistakes = 0

        for Class, Vec in train_data:
            if not self.train_one(Vec, Class):
                mistakes += 1

        return mistakes

    # Evaluate the vector class with classify(),
    # Update the weights if necessary and
    # return True only if the prediction was correct.
    def train_one(self, vector, expected):
        if expected not in [0,1]:
            raise Exception("The `expected` argument should be in range(0,1)!")

        # Check the difference between the
        # expected and the actual value:
        diff = expected - self.classify(vector)

        # If it matched correctly:
        if diff == 0:
            return True
        else:
            # Update the weights:
            delta = diff * self.delta
            self.w_vec = [ (w+delta if v>0 else w) for (v,w) in zip(vector, self.w_vec) ]
            return False

    def activation(self, num):
        if num >= 0:
            return 1
        else:
            return 0
