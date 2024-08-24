def search_iterative(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row, col = 0, m - 1

    while row < n and col >= 0:
        if matrix[row][col] == target:
            return (row, col)
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return "element not found"


def search_recursive(matrix, target, row=0, col=None):
    """
    סיבוכיות זמן הריצה של הפונקציה: O(n+m)
    כאשר-n הוא מספר השורות במטריצה ו-m מספר העמודות במטריצה.
    פירוט מלא עבור שיטת האב והאיטרציה בקובץ ה-PDF המצורף.
    """
    if col is None:
        col = len(matrix[0]) - 1

    if row >= len(matrix) or col < 0:
        return "element not found"

    if matrix[row][col] == target:
        return (row, col)
    elif matrix[row][col] > target:
        return search_recursive(matrix, target, row, col - 1)
    else:
        return search_recursive(matrix, target, row + 1, col)


if __name__ == "__main__":
    print("Search functions on a 50x50 matrix")
    A = [[i * 50 + j for j in range(50)] for i in range(50)]

    print("\nIterative search results:")
    print(f"Searching for 1275 in the matrix:")
    print(search_iterative(A, 1275))  # Output: (25, 25)
    print(f"Searching for 1300 in the matrix:")
    print(search_iterative(A, 1300))  # Output: (26, 0)
    print(f"Searching for 2600 in the matrix:")
    print(search_iterative(A, 2600))  # Output: element not found

    print("\nRecursive search results:")
    print(f"Searching for 1275 in the matrix:")
    print(search_recursive(A, 1275))  # Output: (25, 25)
    print(f"Searching for 1300 in the matrix:")
    print(search_recursive(A, 1300))  # Output: (26, 0)
    print(f"Searching for 2600 in the matrix:")
    print(search_recursive(A, 2600))  # Output: element not found
