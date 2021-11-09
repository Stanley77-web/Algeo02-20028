import numpy as np
from datetime import datetime


def SVDBuatan(array, r):
    U, S, VT = np.linalg.svd(array, full_matrices=True)
    S = np.diag(S)
    # print(U)
    # print(S)
    # print(VT)
    #X = U[:, :r] @ S[0:r, :r] @ VT[:r, :]
    X = U @ S @ VT
    # print(X)
    return X


def compresso(array, k):
    U, S, VT = SVD(array, k)
    S = np.diag(S)
    X = U @ S @ VT
    #X = U[:, 0:k] @ S[0:k, 0:k] @ VT[0:k, :]
    print(X)


def SVD(array, k):
    left = array @ array.T
    right = array.T @ array
    m = left.shape[0]
    n = right.shape[0]
    Q1 = np.random.rand(m, k)
    Q2 = np.random.rand(n, k)
    Q1, _ = np.linalg.qr(Q1)
    Q2, _ = np.linalg.qr(Q2)
    Q_prev = Q1
    for i in range(5000):
        Z1 = left.dot(Q1)
        Z2 = right.dot(Q2)
        Q1, R = np.linalg.qr(Z1)
        Q2, _ = np.linalg.qr(Z2)

        # can use other stopping criteria as well
        err = ((Q1 - Q_prev) ** 2).sum()
        if i % 10 == 0:
            print(i, err)

        Q_prev = Q1
        if err < 1e-3:
            break

    return Q1, np.sqrt(np.diag(R)), Q2.T


def double_power_iteration(A, B, k):
    m = A.shape[0]
    n = B.shape[0]
    Q1 = np.random.rand(m, k)
    Q2 = np.random.rand(n, k)
    Q1, _ = np.linalg.qr(Q1)
    Q2, _ = np.linalg.qr(Q2)
    Q_prev = Q1
    for i in range(1000):
        Z1 = A.dot(Q1)
        Z2 = B.dot(Q2)
        Q1, R = np.linalg.qr(Z1)
        Q2, _ = np.linalg.qr(Z2)

        # can use other stopping criteria as well
        err = ((Q1 - Q_prev) ** 2).sum()
        if i % 10 == 0:
            print(i, err)

        Q_prev = Q
        if err < 1e-3:
            break
    print(R)
    return Q1, np.sqrt(np.diag(R)), Q2.T


# startTime = datetime.now()

size = 5
A3 = np.random.rand(size, size)
# A2 = np.array([[0, 1, 1], [math.sqrt(2), 2, 0], [0, 1, 1]])
#A3 = S = np.array([[3, 1, 1], [-1, 3, 1]])
print(A3)
print("")
print("")
compresso(A3, A3.shape[0])
# SVD(A3, A3.shape[1])
# print(datetime.now() - startTime)
