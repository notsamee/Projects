import random


#merge sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


#quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


#heap sort

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


#bubble sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr



def print_array(arr):
    print(' '.join(str(elem) for elem in arr))

def get_user_choice():
    print("Available sorting algorithms:")
    print("1. Merge Sort")
    print("2. Quick Sort")
    print("3. Heap Sort")
    print("4. Bubble Sort")

    while True:
        choice = input("Enter the number of the sorting algorithm: ")
        if choice.isdigit() and 1 <= int(choice) <= 4:
            return int(choice)
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    num = 0
    while num <= 0:
        num = int(input("Enter amount of numbers you want to be sorted: "))
        if num <= 0:
            print("Invalid length. Please enter number greater than 0")

    numbers = []
    for i in range(num):
        numbers.append(random.randint(1, 51))

    choice = get_user_choice()

    print("Original Array:")
    print_array(numbers)

    if choice == 1:
        sorted_arr = merge_sort(numbers)
        print("Merge Sort:")
    elif choice == 2:
        sorted_arr = quick_sort(numbers)
        print("Quick Sort:")
    elif choice == 3:
        sorted_arr = heap_sort(numbers)
        print("Heap Sort:")
    else:
        sorted_arr = bubble_sort(numbers)
        print("Bubble Sort:")

    print("Sorted Array:")
    print_array(sorted_arr)


if __name__ == "__main__":
    main()
