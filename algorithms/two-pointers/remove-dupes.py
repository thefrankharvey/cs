      #    0  1  2  3  4  5  6  7  8  9  10  11 
input_arr=[0,0,1,1,1,1,2,2,3,3,9,9,9,11]
# Output: 3
# return new length
# inplace
#  SORTED
# work?
def remove_dupes(arr):
    slow, fast = 0, 0
    while fast < len(arr)-1:
        fast+=1
        if arr[slow] != arr[fast]:
            slow+=1
            arr[slow] = arr[fast]

    arr = arr[0:slow+1]
    return len(arr)

print(remove_dupes(input_arr))