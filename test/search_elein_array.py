def search(arr, X):
    for i, element in enumerate(arr):
        if element == x:
            return i
    return -1


arr_input = input("Enter elements of the array separated by spaces: ")
arr1 = list(map(int, arr_input.split()))


x1 = int(input("Enter the element to search: "))


result1 = search(arr1, x1)

if result1 != -1:
    print(f"{x1} found at index {result1}")
else:
    print(f"{x1} not found in the array.")
