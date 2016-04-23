#!/usr/bin/python

import math

from perceptron import Perceptron

class SVM(Perceptron):

    def __init__(self, **kw):
        self.t = 0
        self.lamb = kw.pop('lamb', 2**5)
        super().__init__(**kw)

    def resetWeights(self):
        self.t = 0
        super().resetWeights()

    def vec_mod(self, vec):
        return math.sqrt(sum( v**2 for v in vec ))

    def obj(self, avg_err):
        return (self.lamb/2.) * self.vec_mod(self.w_vec)**2 - avg_err

    # Receive a table with two columns:
    #   class, feature_vec
    #
    # train data until there is no more mistakes being made.
    # Then return the total number of mistakes and the total
    # number of iterations through the data.
    def train(self, train_data, max_iter=20, verbose=True):

        self.obj_vec = []
        self.num_lines = len(train_data)

        m_total, epochs = super().train(train_data, max_iter, verbose)

        return m_total

    # Receive a table with two columns:
    #   class, feature_vec
    #
    # and return True only if all tests
    # matched their respective classes.
    # Return false otherwise.
    def train_epoch(self, train_data, verbose=True):
        self.err_plot = []
        mistakes = 0

        for idx, (exp, vec) in enumerate(train_data):
            self.t += 1

            N = 1./(self.t * self.lamb)

            yi = 1 if exp == 1 else -1
            w_xi = sum( xi*w for (xi,w) in zip(vec, self.w_vec) )

            if yi * w_xi < 1:
                for i, (v,w) in enumerate(zip(vec, self.w_vec)):
                    self.w_vec[i] = w*(1-N*self.lamb) + N*yi*v
            else:
                for i, (v,w) in enumerate(zip(vec, self.w_vec)):
                    self.w_vec[i] = w*(1-N*self.lamb)
            self.err_plot.append(max([0, 1-yi*w_xi]))

            resp = self.activation(w_xi)

            # If it missed:
            if resp != exp:
                mistakes += 1

        if verbose:
            print('miss %s%% on train data' %
                    (self.test(train_data)*100))

        # Save the objective function value for this epoch:
        self.obj_vec.append(self.obj(
            avg_err = sum(self.err_plot) / self.num_lines
          ))

        return mistakes

