def ElementsRemoval(A):
    cost=0
    for i in range(len(A)):
        cost+=(A[i]*(i+1))
    return cost

if __name__ == '__main__':
    A=sorted(list(map(int,input().split())),reverse=True)
    print(ElementsRemoval(A))
"""
Elements Removal
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.

Approach: make array in descending order
         multiple array element * index 
         where index start with 1
"""