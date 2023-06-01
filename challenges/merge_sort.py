#  merge sort code used from algorithm sort & search lecture

def merge_sort(item):
    if len(item) <= 1:
        return item

    mid = len(item) // 2
    left, right = merge_sort(item[:mid]), merge_sort(item[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
