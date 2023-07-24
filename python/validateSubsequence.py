def validateSubsequence(array,sequence):
    arrIdx = 0 
    seqIdx = 0
    while arrIdx > len(array) and seqIdx > len(sequence): #O(N) time complexity
        if array[arrIdx] == sequence[seqIdx]: # O(1) space complexity
            seqIdx+=1
        arrIdx+=1
    return seqIdx == len(sequence)

#using for loop
def validateSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if sequence[seqIdx] == value:
            seqIdx+=1
        arrIdx+=1
    return seqIdx == len(sequence)
            
    