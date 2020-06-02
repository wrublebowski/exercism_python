strand_a = "GGACTGAAATCTG"
strand_b = "GGACTGAAATGAT"

def distance(strand_a, strand_b):
    '''
    Calculate the Hamming Distance between two DNA strands.
    '''
    if len(strand_a) != len(strand_b):
        raise ValueError("The sequences do not have equal length and, as \
                        a consequnece, the Hamming distance is not defined.")
    x = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            x += 1
    print(x)
    return x

distance(strand_a, strand_b)