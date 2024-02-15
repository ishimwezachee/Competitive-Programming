#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        if len(A) != len(B):
            return 0
            
        a = sorted(A)
        b = sorted(B)
        
        for i in range(N):
            if a[i] !=b[i]:
                return 0
        return 1
