import sys, math
def hash_fraction(m,n):
    """Compute the hash of a rational number m/n.
    Assumes m and n are integers, with n positive.
    Equivalent to hash(fraction.Fraction(m,n)).
    """
    P = sys.hash_info.modulus
    #Remove common factors of P.(Unnecessary if m and n already coprime)
    while m%p == n%p == 0:
        m,n = m//P, n//P
    if n % P == 0:
        hash_ = sys.hash_info.inf
    else:
        #Fermat's Little Theorem:pow(n,P-1,P)is 1,so
        #pow(n, P-2, P)gives the inverse of n modulo P.
        hash_ =(abs(m)% P)* pow(n, P-2, P)% P
    if m < 0
