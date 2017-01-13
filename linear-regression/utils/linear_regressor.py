import numpy


class LinearRegression(object):

    def __init__(self, x_train, y_train):
        dimensions = len(x_train[0])

        A = numpy.matrix(numpy.zeros((dimensions, dimensions)))
        b = numpy.matrix(numpy.zeros((dimensions, 1)))
        for i in range(len(x_train)):
            nmat = numpy.matrix(x_train[i])
            temp_a = nmat.T * nmat
            A += temp_a

            temp_b = nmat.T * numpy.matrix(y_train[i])
            b += temp_b

        self.weights = A.I * b

    def predict(self, x_test):
        predictions = list()
        for i in range(len(x_test)):
            nmat = numpy.matrix(x_test[i])
            res = nmat * self.weights
            predictions.append(res.getA()[0][0])

        return predictions