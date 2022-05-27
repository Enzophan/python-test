

def quick_sort (sequence):
    lenght = len(sequence)
    if lenght <=1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([1,3,4,8,1,3,9,0,4,42,5,64,10]))