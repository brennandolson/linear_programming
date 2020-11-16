import numpy as np
from numpy.linalg import det

def b(n, l):
    s = list(map(int, bin(n)[2:]))
    if len(s) >= l:
        return s
    else:
        return [0] * (l - len(s)) + s

def laminar(r1, r2):
    p, m = 0, 0
    for i in range(len(r1)):
        if r1[i] and not r2[i]:
            p += 1
        elif r2[i] and not r1[i]:
            m += 1
    return p * m == 0 or p + m == len(r1)

def test_group(arr, g):
    if len(g) == 1:
        return True
    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            if not laminar(list(arr[g[i]]), list(arr[g[j]])):
                return False
    return True

def test_groups(arr, g1, g2):
    return test_group(arr, g1) and test_group(arr, g2)

def good_groups(arr):
    for g1, g2 in [[0], [1,2,3]], [[1], [0,2,3]], [[2], [0,1,3]], [[3],
            [0,1,2]], [[0,1], [2,3]], [[0,2], [1,3]], [[0,3], [1,2]]:
        if test_groups(arr, g1, g2):
            return True
    return False

def test(n):
    for i in range(pow(2, n*n)):
        arr = np.reshape(b(i, n*n), (n,n))
        if det(arr) > 1.001 and good_groups(arr):
            yield arr

for m in test(4):
    print (m)
    print ()
# for m in test(3):
    # print (m)
    # print ()
    # input()
# arr = np.zeros((3,3))
# arr = np.reshape([0,1,0,0,1,1,1,0,0], (3, 3))
# print (test_groups(arr, [0], [1,2]))
# print (arr)
# print ()
# print (test_group(arr, [0]))
# print (test_group(arr, [0,1]))
# print (test_group(arr, [0, 2]))
