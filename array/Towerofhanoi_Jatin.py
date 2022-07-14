
# We mark three towers with name, source, destination and aux (only to help moving the disks).
# we are in a position to design an algorithm for Tower of Hanoi with 6 disks. 
# We divide the stack of disks in two parts. 
# The largest disk (nth disk) is in one part and all other (n-1) disks are in the second part.
# Our ultimate aim is to move disk n from source to destination and then put all other (n1) disks onto it.
# We can imagine to apply the same in a recursive way for all given set of disks.
#The steps to follow are −
# Step 1 − Move n-1 disks from source to aux
# Step 2 − Move nth disk from source to dest
# Step 3 − Move n-1 disks from aux to dest

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1: #initially disk are at rod 1
        print(f"Move disk 1 from source {source},to destination {destination}")
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print(f"Move disk,{n},from source,{source},to destination {destination}")
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
# Driver code
n = 6 # n = no of disks i.e. 6
TowerOfHanoi(n,'A','B','C') # A, C, B are the name of rods


# Analysis of Recursion
# Recursive Equation : T(n) = 2T(n-1) + 1  ——-equation-1 

# Solving it by Backsubstitution : 
# T(n-1) = 2T(n-2) + 1  ———–equation-2 
# T(n-2) = 2T(n-3) + 1  ———–equation-3 

# Put the value of T(n-2) in the equation–2 with help of equation-3 
# T(n-1)= 2( 2T(n-3) + 1 ) + 1  ——equation-4 

# Put the value of T(n-1) in equation-1 with help of equation-4 
# T(n)= 2( 2( 2T(n-3) + 1 ) + 1 ) + 1  
# T(n) = 2^3 T(n-3) + 2^2 + 2^1 + 1  

# After Generalization : 
# T(n)= 2^k T(n-k) + 2^{(k-1)} + 2^{(k-2)} + ............ +2^2 + 2^1 + 1  

# Base condition T(1) =1 
# n – k = 1 
# k = n-1
# put, k = n-1
# T(n) =2^{(n-1)}T(0) + + 2^{(n-2)} + ............ +2^2 +2^1 + 1  

# It is a GP series, and the sum is 2^n - 1  

# T(n)= O( 2^n - 1)  , or you can say O(2^n)  which is exponential

# for 6 disks i.e. n=6 It will take 2^6-1=63 moves.

# Most of the recursive programs takes exponential time that is why it
# is very hard to write them iteratively .
# T(1) = 2k T(2) = 3k T(3) = 4k 
# So the space complexity is O(n). 
# Here time complexity is exponential but space complexity is linear.  