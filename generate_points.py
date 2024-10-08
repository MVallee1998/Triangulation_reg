import numpy as np
import json

def print_vertices_and_weights(k):
    epsilon = 0.0000001
    n = 2*k
    N = 2*n + k*(n-1)
    points  = np.zeros((n,N),dtype=int)
    weights = np.zeros(N)
    index=n
    points[:,:n] = 2*(k+1)*np.eye(n)
    weights[:n] = (n-1)*(k-1) #+ (n-1) 
    weights[:n] -=  np.array(range(n))*epsilon
    points[:,N-n:] = np.ones((n,n)) + 2*np.eye(n)
    for l in range(k):
        weights[N-n + l] = (k-1)*(k-2) + (2*l+1)*epsilon #+ (n-2)
        weights[N-n +l + k ] = (k-1)*(k-2) + (2*l+2)*epsilon #+ (n-2)
    old_weight = (n-1)*(k)
    #weights[N-n:] = (k-1)*(k-2)
    for j in range(1,k):
        if j == 1:
            weight = (k-1)*(n-3)  #+ (n-2)
        elif j==2:
            weight = (n-3)*(k-2)  #+ (n-2)
        else:
            weight = ((j-1) * (j-2))//2 + ((n- j - 1)*(n-j-2))//2  #+ (n-2)
        for i in range(n):
            points[i,index] = k+1
            points[(i+j)%n,index] = k+1
            weights[index] = weight - i * epsilon
            index +=1
        old_weight = weight
    for i in range(k):
            points[i,index] = k+1
            weight = (k-1)*(k-2)  #+ (n-2)
            # if old_weight == weight:
            #     weight-=n*epsilon
            points[(i+k)%n,index] = k+1
            weights[index] = weight - i*epsilon
            index +=1
    print("$M = new Matrix<Rational>(",np.array2string(points.T, separator=",").replace('\n', '').replace(' ', ''),");")
    print("$w = new Vector<Rational>(",np.array2string(weights, separator=",").replace('\n', '').replace(' ', ''),");")
    print("$S = new fan::SubdivisionOfPoints(POINTS=>ones_vector|$M,WEIGHTS=>$w);")
    print('open(my $f, ">", "triang_n%d.out");' % n)
    print("print $f $S->MAXIMAL_CELLS;")
    print("close $f;")
print_vertices_and_weights(3)