import numpy as np
from numpy.random import uniform as rand
from scipy.optimize import linprog as solve

def sample(n, test_integrality=False):
    '''
    assigns all n^2 edge-weights of a 
    K_{n,n} independently as U(0, 1).
    returns min-weight matching
    '''

    # weights iid U(0, 1)
    w = rand(size = n**2)
    
    # constraint matrix
    # Note: linprog solver uses x>= 0 as a default
    # so these constraints are implicit.
    A = np.zeros((2*n, n**2))
    for i in range(n):
        for j in range(n):
            A[i][i*n + j] = 1
            A[n + j][i * n + j] = 1
    
    # right-hand side
    b = np.ones((2*n, 1))

    # solve for x and objective value
    full_results = solve(w, A_eq = A, b_eq = b)
    x = full_results.x
    obj = full_results.fun 

    if test_integrality:
        integrality_error = 0
        for i in range(n):
            for j in range(n):
                ndx = i * n + j
                integrality_error += abs(x[ndx] - round(x[ndx]))
        return integrality_error
    
    return obj


def monte_carlo(n, rounds=500):
    tot = 0
    for _ in range(rounds):
        tot += sample(n)
    return tot / rounds



# Warning: scipy complains to stderr
# frequently about non-full-rank matrices.
# Recommended to suppress error output by running as
#
# python Knn.py 2> /dev/null

if __name__ == "__main__":
    data = open('out.txt', 'a')
    for n in range(25, 31):
        res = monte_carlo(n)
        data.write(str(n) + ' ' + str(res)+'\n')
    data.close()

