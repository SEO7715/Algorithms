Array = [5, 3, 1, 2, 7]


## bubble sort
def bubble_sort(Array):
    N = len(Array) 
    for k in range(N, 0, -1):
        for i in range(1, k):
            if Array[i-1] > Array[i]:
                Array[i-1], Array[i] = Array[i], Array[i-1]



def selection_sort(Array):
    # new_Array = []
    N = len(Array) 
    # for _ in range(N):
    #     min_array = min(Array)
    #     Array.remove(min_array)
    #     new_Array.append(min_array)
    
    for x in range(N-1):
        for i in range(x+1, N):
            if Array[i-1] > Array[i]:
                min_idx = i   
        Array[x], Array[min_idx] = Array[min_idx], Array[x]

selection_sort(Array)