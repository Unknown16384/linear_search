from part01 import linear_search, list_create
import timeit

lst = list_create(10)
print(timeit.timeit(lambda: linear_search(lst, 111), number=10000))
lst = list_create(100)
print(timeit.timeit(lambda: linear_search(lst, 111), number=10000))
lst = list_create(1000)
print(timeit.timeit(lambda: linear_search(lst, 111), number=10000))