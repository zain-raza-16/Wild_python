def mergesort(li):
    helper = [0] * len(li)
    mergesorthelper(li, helper, 0, len(li) - 1)


def mergesorthelper(li, helper, low, high):
    if high > low:
        middle = (low + high) // 2
        mergesorthelper(li, helper, low, middle)
        mergesorthelper(li, helper, middle + 1, high)
        merge(li, helper, low, middle, high)


def merge(li, helper, low, middle, high):
    i = low
    while i <= high:
        helper[i] = li[i]
        i += 1

    left_helper = low
    right_helper = middle + 1
    current = low

    while left_helper <= middle and right_helper <= high:
        if helper[left_helper] <= helper[right_helper]:
            li[current] = helper[left_helper]
            left_helper += 1
        else:
            li[current] = helper[right_helper]
            right_helper += 1
        current += 1

    remaining = middle - left_helper
    j = 0
    while j <= remaining:
        li[current + j] = helper[left_helper + j]
        j += 1



hello = [4,5,2,9,4,1]
mergesort(hello)
print(hello)