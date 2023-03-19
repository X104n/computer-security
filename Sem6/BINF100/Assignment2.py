# Define the scoring scheme
match_score = 1
mismatch_score = -1
gap_penalty = 2

def smith_waterman(seq1, seq2):
    # Initialize the matrix
    matrix = [[0 for j in range(len(seq2) + 1)] for i in range(len(seq1) + 1)]
    
    # Initialize the maximum score and its location
    max_score = 0
    max_location = (0, 0)
    
    # Fill in the matrix
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            match = matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
            delete = matrix[i-1][j] - gap_penalty
            insert = matrix[i][j-1] - gap_penalty
            score = max(0, match, delete, insert)
            matrix[i][j] = score
            
            # Update the maximum score and its location
            if score > max_score:
                max_score = score
                max_location = (i, j)
                
    # Trace back to find all optimal local alignments
    alignments = []
    i, j = max_location
    while matrix[i][j] != 0:
        if matrix[i][j] == matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score):
            alignments.append((seq1[i-1], seq2[j-1]))
            i -= 1
            j -= 1
        elif matrix[i][j] == matrix[i-1][j] - gap_penalty:
            alignments.append((seq1[i-1], '-'))
            i -= 1
        elif matrix[i][j] == matrix[i][j-1] - gap_penalty:
            alignments.append(('-', seq2[j-1]))
            j -= 1
    
    # Reverse the alignments to get the correct order
    alignments = alignments[::-1]
    
    return alignments

# Task 1
def task1():
    # Task 1.a)
    seq1 = 'ACGTAGCTAGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC'
    seq2 = 'ACGTAGCTAGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC'
    alignments = smith_waterman(seq1, seq2)
    print("Task 1.a: ", alignments)

    # Task 1.b)

    # >A/California/07/2009_segment_7
    seq1 = """TAGATATTAAAGATGAGTCTTCTAACCGAGGTCGAAACGTACGTTCTTTCTATCATCCCGTCAGGCCCCC
    TCAAAGCCGAGATCGCGCAGAGACTGGAAAGTGTCTTTGCAGGAAAGAACACAGATCTTGAGGCTCTCAT
    GGAATGGCTAAAGACAAGACCAATCTTGTCACCTCTGACTAAGGGAATTTTAGGATTTGTGTTCACGCTC
    ACCGTGCCCAGTGAGCGAGGACTGCAGCGTAGACGCTTTGTCCAAAATGCCCTAAATGGGAATGGGGACC
    CGAACAACATGGATAGAGCAGTTAAACTATACAAGAAGCTCAAAAGAGAAATAACGTTCCATGGGGCCAA
    GGAGGTGTCACTAAGCTATTCAACTGGTGCACTTGCCAGTTGCATGGGCCTCATATACAACAGGATGGGA
    ACAGTGACCACAGAAGCTGCTTTTGGTCTAGTGTGTGCCACTTGTGAACAGATTGCTGATTCACAGCATC
    GGTCTCACAGACAGATGGCTACTACCACCAATCCACTAATCAGGCATGAAAACAGAATGGTGCTGGCTAG
    CACTACGGCAAAGGCTATGGAACAGATGGCTGGATCGAGTGAACAGGCAGCGGAGGCCATGGAGGTTGCT
    AATCAGACTAGGCAGATGGTACATGCAATGAGAACTATTGGGACTCATCCTAGCTCCAGTGCTGGTCTGA
    AAGATGACCTTCTTGAAAATTTGCAGGCCTACCAGAAGCGAATGGGAGTGCAGATGCAGCGATTCAAGTG
    ATCCTCTCGTCATTGCAGCAAATATCATTGGGATCTTGCACCTGATATTGTGGATTACTGATCGTCTTTT
    TTTCAAATGTATTTATCGTCGCTTTAAATACGGTTTGAAAAGAGGGCCTTCTACGGAAGGAGTGCCTGAG
    TCCATGAGGGAAGAATATCAACAGGAACAGCAGAGTGCTGTGGATGTTGACGATGGTCATTTTGTCAACA
    TAGAGCTAGAGTAAAAAACTACAGGATGGGAACTGGTGACCACAGAAGCTGCTTTTGGTCTAGTGTGTGC"""

    # >A/Brisbane/59/2007_M2_coding_region
    seq2 = """ATGAGTCTTCTAACCGAGGTCGAAACGCCTATCAGAAACGAATGGGGGTGCAGATGCAACGATTCAAGTG
    ATCCTCTTGTTGTTGCCGCAAGTATAATTGGGATTGTGCACTTGATATTGTGGATTATTGATCGCCTTTT
    TTCCAAAAGCATTTATCGTATCTTTAAACACGGTTTAAAAAGAGGGCCTTCTACGGAAGGAGTACCAGAG
    TCTATGAGGGAAGAATATCGAGAGGAACAGCAGAATGCTGTGGATGCTGACGATGATCATTTTGTCAGCA
    TAGAGCTAGAGTAA"""

    alignments = smith_waterman(seq1, seq2)
    print("Task 1.b: ", alignments)

if __name__ == '__main__':
    task1()