def bubble_sort(arr, key=lambda x: x, reverse=False):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if _cmp(a[j], a[j+1], key, reverse):
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def insertion_sort(arr, key=lambda x: x, reverse=False):
    a = arr.copy()
    for i in range(1, len(a)):
        val = a[i]
        j = i - 1
        while j >= 0 and _cmp(a[j], val, key, reverse):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = val
    return a


def quick_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr[:]
    pivot = key(arr[len(arr)//2])
    left, mid, right = [], [], []
    for x in arr:
        k = key(x)
        if k < pivot:
            left.append(x)
        elif k > pivot:
            right.append(x)
        else:
            mid.append(x)
    left_sorted = quick_sort(left, key, reverse)
    right_sorted = quick_sort(right, key, reverse)
    if reverse:
        return right_sorted + mid + left_sorted
    return left_sorted + mid + right_sorted


def merge_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, reverse)
    right = merge_sort(arr[mid:], key, reverse)
    return _merge(left, right, key, reverse)


def _merge(left, right, key, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if _cmp(left[i], right[j], key, reverse):
            result.append(right[j]); j += 1
        else:
            result.append(left[i]); i += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def _cmp(a, b, key, reverse):
    """True, если a и b надо поменять местами."""
    if reverse:
        return key(a) < key(b)
    return key(a) > key(b)


SORT_ALGORITHMS = {
    "1": ("Пузырьковая", bubble_sort),
    "2": ("Вставками",   insertion_sort),
    "3": ("Быстрая",     quick_sort),
    "4": ("Слиянием",    merge_sort),
}


SORT_KEYS = {
    "1": ("по цене",      lambda p: p.price),
    "2": ("по весу",      lambda p: p.weight),
    "3": ("по категории", lambda p: p.category),
}