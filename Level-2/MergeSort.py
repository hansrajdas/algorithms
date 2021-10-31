print("Number Sequence Before Merge Sort")
seq=[5,2,1,8,3,5,3]
print(seq)

def mergeSort(nums):
    n=len(nums)
    if(n<2):
        return nums
    mid=int(n/2)
    L=nums[0:mid]
    R=nums[mid:n]
    L=mergeSort(L)
    R=mergeSort(R)
    nums=merge(L,R,nums)
    return nums

def merge(L,R,nums):
    nL=len(L)
    nR=len(R)
    nNums=len(nums)
    [i,j,k]=[0,0,0]
    while(i<nL and j<nR):
        if(L[i]<=R[j]):
            nums[k]=L[i]
            i+=1
        else:
            nums[k] = R[j]
            j += 1
        k+=1

    while(i<nL):
        nums[k] = L[i]
        i += 1
        k += 1

    while (j < nR):
        nums[k] = R[j]
        j += 1
        k += 1

    return nums

print("Number Sequence After Merge Sort")
print(mergeSort(seq))







