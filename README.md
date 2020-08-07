# Probability-that-the-average-of-a-sequence-is-the-sequence.
This produces the probability that a sequence of N integers from 1 to k contains the average of its sequence somewhere inside the sequence. E.g. the sequence

    (1,1,1,1)
    
contains its average, 

    (1+1+1+1)/4 = 1 
    
within its sequence.
Simply use P(N,k) which prints a lower bound as well as the number of true cases, and number of sequences that can be formed from N,k. For example,

    P(2,4) = 0.5

which means that half of the possible sequences contain the average of their sequence somewhere. 
