from logistic_regression import logistic_regression


def get_data():
    datamatrix = []
    labelmatrix = []
    fr = open('logistic.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        datamatrix.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelmatrix.append(int(lineArr[2]))
    return datamatrix, labelmatrix


def plot_fit(fit_line, datamatrix, labelmatrix):
    import matplotlib.pyplot as plt
    import numpy as np

    weights = fit_line.getA()

    dataarray = np.asarray(datamatrix)
    n = dataarray.shape[0]

    # Keep track of the two classes in different arrays so they can be plotted later...
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelmatrix[i]) == 1:
            xcord1.append(dataarray[i, 1])
            ycord1.append(dataarray[i, 2])
        else:
            xcord2.append(dataarray[i, 1])
            ycord2.append(dataarray[i, 2])
    fig = plt.figure()

    # Plot the data as points with different colours
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')

    # Plot the best-fit line
    x = np.arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)

    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()

    
X, Y = get_data()

clf = logistic_regression(5000)
w = clf.fit(X, Y)
print 'Weights:', w
plot_fit(w, X, Y)
# clf.predict(X)
