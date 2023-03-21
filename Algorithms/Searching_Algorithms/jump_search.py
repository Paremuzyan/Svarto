import math


def linear_search(B, item, loc):
    print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            return loc+i
        i += 1
    return -1


def jump_search(sorted_arr, el):
    n = len(sorted_arr)
    m = int(math.sqrt(n))
    i = 0
    while i != n - 1 and sorted_arr[i] < el:
        if sorted_arr[i+m-1] == el:            
            return i+m-1
        elif sorted_arr[i+m-1] > el:           
            B = sorted_arr[i: i+m-1]
            return linear_search(B, el, i)
        i += m

    B = sorted_arr[i:i+m]                       
    print("Processing Block - {}".format(B))
    return linear_search(B, el, i)      


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(jump_search(arr, 3))