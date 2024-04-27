def binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # If the element is not found

# 
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_element = 18

result = binary_search(my_list, target_element)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
