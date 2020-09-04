import numpy as np

def gen_candidate():
    return np.random.random(2)

def get_score(candidate, bias):
    return bias*candidate[0] + (1-bias)*candidate[1]