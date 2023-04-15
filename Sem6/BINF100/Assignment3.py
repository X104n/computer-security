import numpy as np
import random
from itertools import permutations

"""
a) needleman_wunsch function calculates the optimal alignment score using dynamic programming.

b) random_sequences function generates 1000 random sequences by shuffling the characters from seq2.

c) random_scores_1 and random_scores_2 are lists containing the optimal scores for aligning each of the 1000 random sequences with seq1a and seq1b, respectively.

d) p_value function calculates the p-value of the original score based on the statistics of scores from c).

e) The final lines of the script print the answers to questions 1 and 2 based on the significance level alpha=0.01.

Please note that the p-values and answers might vary slightly each time you run the script due to the randomness in the generated sequences.
"""

def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    n, m = len(seq1), len(seq2)
    score_matrix = np.zeros((n + 1, m + 1))

    for i in range(n + 1):
        score_matrix[i, 0] = gap * i

    for j in range(m + 1):
        score_matrix[0, j] = gap * j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq1[i - 1] == seq2[j - 1]:
                match_score = score_matrix[i - 1, j - 1] + match
            else:
                match_score = score_matrix[i - 1, j - 1] + mismatch

            score_matrix[i, j] = max(match_score, score_matrix[i - 1, j] + gap, score_matrix[i, j - 1] + gap)

    return score_matrix[n, m]

def random_sequences(seq, num):
    return [''.join(random.sample(seq, len(seq))) for _ in range(num)]

def p_value(observed_score, random_scores):
    count = sum([1 for score in random_scores if score >= observed_score])
    return count / len(random_scores)

seq1a = "AATTTT"
seq1b = "GCAATTTT"
seq2 = "TAAAGCAATTTTGGTTTTTTTCCGA"

# Calculate observed scores
observed_score_1 = needleman_wunsch(seq1a, seq2)
observed_score_2 = needleman_wunsch(seq1b, seq2)

# Generate 1000 random sequences
random_seq2s = random_sequences(seq2, 1000)

# Calculate random scores
random_scores_1 = [needleman_wunsch(seq1a, random_seq) for random_seq in random_seq2s]
random_scores_2 = [needleman_wunsch(seq1b, random_seq) for random_seq in random_seq2s]

# Calculate p-values
p_value_1 = p_value(observed_score_1, random_scores_1)
p_value_2 = p_value(observed_score_2, random_scores_2)

alpha = 0.01

# Answer questions 1 and 2
print("1. Are seq1a and seq2 homologous?", p_value_1 < alpha)
print("2. Are seq1b and seq2 homologous?", p_value_2 < alpha)


