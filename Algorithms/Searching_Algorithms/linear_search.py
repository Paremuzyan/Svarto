def linear_search(lst, el):
    for i in range(len(lst)):
        if lst[i] == el:
            return f"{el} is present at index {i}"
        else:
            return f"{el} not found! in {lst}"


lst = [3, 8, 30, 5]
el = 7
print(linear_search(lst, el))