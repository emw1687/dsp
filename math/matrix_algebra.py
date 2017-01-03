# Matrix Algebra
import numpy as np
import math

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])
alpha = 6

def try_eval(prob_dict):
    for problem in sorted(prob_dict):
        print problem
        try:
            print eval(prob_dict[problem])
            print '----------'
        except:
            print 'not defined'
            print '----------'

#1. Matrix Dimensions
problem1 = {
    '1.1)': A,
    '1.2)': B,
    '1.3)': C,
    '1.4)': D,
    '1.5)': u,
    '1.6)': w
}

for problem in sorted(problem1):
    print problem
    print problem1[problem].shape
    print '----------'

#2. Vector Operations
problem2 = {
    '2.1)': 'u + v',
    '2.2)': 'u - v',
    '2.3)': 'alpha * u',
    '2.4)': 'np.dot(u,v)',
    '2.5)': 'np.linalg.norm(u)'
}

try_eval(problem2)

#3. Matrix Operations
problem3 = {
    '3.1)': 'A + C',
    '3.2)': 'A - C.T',
    '3.3)': 'C.T + 3*D',
    '3.4)': 'B*A',
    '3.5)': 'B*A.T'
}

try_eval(problem3)

#Optional
problem_opt = {
    '3.06)': 'B*C',
    '3.07)': 'C*B',
    '3.08)': 'B**4',
    '3.09)': 'A*A.T',
    '3.10)': 'D.T*D'
}

try_eval(problem_opt)
