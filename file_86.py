
# 2026-07-14 00:22:41.545737
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# 2026-08-06 10:19:35.956173
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


# 2026-08-21 00:53:57.906563
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


# 2026-09-22 06:08:56.408833
def is_palindrome(s):
    return s == s[::-1]

