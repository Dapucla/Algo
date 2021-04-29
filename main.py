import random
import time
import operator

N = int(input())
array = random.sample(range(0, N), N)
print(array)


# ----------------Декоратор----------------
def my_timer(f):
    def tmp(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - start_time
        print('Время выполнения функции {}'.format(delta_time))
        return result

    return tmp


# ----------------Вставками----------------
# @my_timer
# def insertionSort(array):
#     for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
#
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j = j - 1
#
#         array[j + 1] = key
#
#
# insertionSort(array)
# print(array)


# ----------------Выбором----------------
# @my_timer
# def selectionSort(array, size):
#     for step in range(size):
#         min_idx = step
#
#         for i in range(step + 1, size):
#
#             # to sort in descending order, change > to < in this line
#             # select the minimum element in each loop
#             if array[i] < array[min_idx]:
#                 min_idx = i
#
#         # put min at the correct position
#         (array[step], array[min_idx]) = (array[min_idx], array[step])
#
#
# size = len(array)
# selectionSort(array, size)
# print(array)


# ----------------Обменом----------------
# @my_timer
# def bubbleSort(array):
#     # loop to access each array element
#     for i in range(len(array)):
#
#         # loop to compare array elements
#         for j in range(0, len(array) - i - 1):
#
#             # compare two adjacent elements
#             # change > to < to sort in descending order
#             if array[j] > array[j + 1]:
#                 # swapping elements if elements
#                 # are not in the intended order
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
# bubbleSort(array)
# print(array)


# ----------------Слиянием----------------
# @my_timer
# def mergeSort(array):
#     if len(array) > 1:
#         r = len(array)//2
#         L = array[:r]
#         M = array[r:]
#         mergeSort(L)
#         mergeSort(M)
#         i = j = k = 0
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 array[k] = L[i]
#                 i += 1
#             else:
#                 array[k] = M[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             array[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(M):
#             array[k] = M[j]
#             j += 1
#             k += 1
#
# mergeSort(array)
# print(array)
# ----------------Пирамидальная----------------
# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#
#     if l < n and arr[i] < arr[l]:
#         largest = l
#
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
#
# @my_timer
# def heapSort(arr):
#     n = len(arr)
#
#     for i in range(n // 2, -1, -1):
#         heapify(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#
#         heapify(arr, i, 0)
#
#
# heapSort(array)
# n = len(array)
# for i in range(n):
#     print("%d " % array[i], end='')


# ----------------Быстрая----------------
# def qsort(array, left, right):
#     middle = (left + right) // 2
#
#     p = array[middle]
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)
# qsort(array, 0, len(array) - 1)
# print(array)



# ----------------Бинарный поиск----------------
# def binary_search(array, element, left, right):
#     if left > right:
#         return False
#
#     middle = (right + left) // 2
#     if array[middle] == element:
#         return middle
#     elif element < array[middle]:
#
#         return binary_search(array, element, left, middle - 1)
#     else:
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...

# print(binary_search(array, element, 0, 99))