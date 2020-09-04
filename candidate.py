import numpy as np

class Candidate:

    def __init__(self, i=0, bias=.95):
        self.id = i
        self.bias = bias
        self.luck = np.random.random()
        self.qual = np.random.random()
    
    def get_score(self):
        return self.bias*self.qual + (1-self.bias)*self.luck

    def __str__(self):
        out = ''
        out += f'Candidate qualification: {self.qual}\n'
        out += f'Candidate luck: {self.luck}\n'
        return out 

    
    def __gt__(self, other):
        score_1 = self.get_score()
        score_2 = other.get_score()

        return score_1 > score_2

    def __ge__(self, other):
        score_1 = self.get_score()
        score_2 = other.get_score()

        return score_1 >= score_2
    
    def __lt__(self, other):
        score_1 = self.get_score()
        score_2 = other.get_score()

        return score_1 < score_2
    
    def __le__(self, other):
        score_1 = self.get_score()
        score_2 = other.get_score()

        return score_1 <= score_2


def generate_candidates(n):
    bias_candidates = np.array([Candidate(i,.85) for i in range(n)])
    unbiased_candidates = np.array([Candidate(i,1) for i in range(n)])
    return bias_candidates, unbiased_candidates

if __name__ == "__main__":
    b_c, ub_c = generate_candidates(33824)

    bias_top = b_c.argsort()[-1085:]
    ubias_top = ub_c.argsort()[-1085:]

    b_qmean = np.mean([i.qual for i in b_c[bias_top]])
    b_lmean = np.mean([i.luck for i in b_c[bias_top]])

    ub_qmean = np.mean([i.qual for i in ub_c[ubias_top]])
    ub_lmean = np.mean([i.luck for i in ub_c[ubias_top]])


    print(f'Mean qualification of unbiased sorting: {ub_qmean}')
    print(f'Mean luck of unbiased sorting: {ub_lmean}')

    print(f'Mean qualification of biased sorting: {b_qmean}')
    print(f'Mean luck of biased sorting: {b_lmean}')


    