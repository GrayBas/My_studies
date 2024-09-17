def sort_merge(lst: list):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = sort_merge(lst[:mid])
    right = sort_merge(lst[mid:])
    return merge(left, right, lst.copy())

def merge(left, right, merged):
    left_c = 0
    right_c = 0
    while left_c < len(left) and right_c < len(right):
        if left[left_c] <= right[right_c]:
            merged[left_c + right_c] = left[left_c]
            left_c += 1
        else:
            merged[left_c + right_c] = right[right_c]
            right_c += 1

    for left_c in range(left_c, len(left)):
        merged[left_c + right_c] = left[left_c]

    for right_c in range(right_c, len(right)):
        merged[left_c + right_c] = right[right_c]


    return merged


print(sort_merge(list(map(int, input("Enter numbers separated by spaces:\n").split()))))


