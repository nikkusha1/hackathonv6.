def manual_min(lst):
    if len(lst) == 0:
        return None  

    minimum = lst[0]

    
    for num in lst:
        if num < minimum:
            minimum = num
    
    return minimum
manual_min()