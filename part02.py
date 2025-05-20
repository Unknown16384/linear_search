from part01 import linear_search, list_create
import timeit

lst = list_create(100)
print(linear_search(lst, 10), timeit.timeit(lambda: linear_search(lst, 10), number=10000))
print(linear_search(lst, 20), timeit.timeit(lambda: linear_search(lst, 20), number=10000))
print(linear_search(lst, 30), timeit.timeit(lambda: linear_search(lst, 30), number=10000))