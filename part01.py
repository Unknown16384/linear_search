import random

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def list_create(list_len):
    lst = []
    for _ in range(list_len):
        lst.append(random.randint(0, 100))
    return lst