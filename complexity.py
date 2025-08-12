# complexity_examples.py
# O(n) Time | O(1) Space
def print_elements(arr):
    print("O(n) Time, O(1) Space:")
    for item in arr:
        print(item, end = " ")

# O(n^2) Time | O(1) Space
def print_pairs(arr):
    print("\n\n O(n^2) Time, O(1) Space:")
    for i in arr:
        for j in arr:
            print(i, j)

# O(log n) Time | O(1) Space
def binary_search(arr, target):
    print("\n\nO(log n) Time, O(1) Space:")
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test functions
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print_elements(arr)
    print_pairs(arr)
    print("Index of 4:", binary_search(arr, 4))
