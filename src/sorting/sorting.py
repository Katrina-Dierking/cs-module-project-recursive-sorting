# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(a, b):
    el= len(a) + len(b)
    merged_arr = [0] * el
    
    ai = 0
    bi = 0
    
    while ai < len (a) and bi <len(b):
        if a[ai] <= b[bi]:
            merged_arr.append(a[ai])
            ai += 1
        else:
            merged_arr.append(b[bi])
            bi += 1
            
    while ai < len (a):
        merged_arr.append(a[ai])
        ai += 1
        
    while bi < len(b):
        merged_arr.append(b[bi])
        ai += 1 
        
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    mid_point = len(arr)//2
    LHS = arr[ :mid_point]
    RHS = arr[mid_point: ]
    
    if len(LHS) > 1:
        left = merge_sort(LHS)
    
    if len(RHS) > 1:
        right = merge_sort(RHS)
    
    arr = merge(left, right)
    
    return arr 

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here

    pass