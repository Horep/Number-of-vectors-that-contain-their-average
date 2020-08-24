This produces the number of 1..k vectors of length N that contain the average of its sequence somewhere inside the sequence. E.g. the sequence

    (1,1,1,1)
    
contains its average, 

    (1+1+1+1)/4 = 1 
    
within its sequence.

To calculate the number of length three 0..n vectors that contain their arithmetic mean, you would use A(3,n). It is similar for the geometric mean, except you would use G.

To calculate a sequence of these 10 of these length three geometric mean numbers, you would use GiveList(G, 3, 10). To produce several lists, use Give GiveTable(y, N_num, k_num).

To calculate k=(num) non-trivial consecutive terms, use give_nontrivial_consecutive(y, N, num).
