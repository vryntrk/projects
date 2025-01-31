def bubble_sort(array):
    for _ in range(len(array)):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


number_list = [7, 3, 8, 2, 0, 4, 1, 6, 9, 5, -1]
print("Original List: ", number_list)

sorted_list = bubble_sort(number_list)
print("Sorted List: ", sorted_list)