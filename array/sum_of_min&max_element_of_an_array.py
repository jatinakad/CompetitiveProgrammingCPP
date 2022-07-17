class Solution:
    def findSum(self,A,N): 
        min = A[0]
        max = A[0]

        for i in range(1,N):
            if min>A[i]:
                min = A[i]
            elif max < A[i]:
                max = A[i]

        return max + min

        

if __name__ == "__main__":
    N=6
    A=[1000, 11, 445, 1, 330, 3000]
    ob = Solution()
    print(ob.findSum(A,N))