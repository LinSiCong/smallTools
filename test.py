#!/usr/bin/env python

import numpy as np

if __name__ == '__main__':
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    for i in range(len(a)):
        print(a[i, :])

    x = np.where(a[:, -1] > 5)
    print(x)
    print(len(x))
    for i in range(len(x)):
        print(x[i])
    print(a[x])
