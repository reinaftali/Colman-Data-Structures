class Node:
    def __init__(self, height, index):
        self.height = height
        self.index = index
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, height, index):
        new_node = Node(height, index)
        new_node.next = self.head
        self.head = new_node

    def remove_shorter_buildings(self, height):
        while self.head and self.head.height <= height:
            self.head = self.head.next

def find_visible_buildings(heights):
    n = len(heights)
    result = [0] * n
    buildings = LinkedList()

    for i in range(n):
        buildings.remove_shorter_buildings(heights[i])

        if not buildings.head:
            result[i] = 0  # Can see the sea
        else:
            result[i] = buildings.head.index + 1  # +1 to convert from 0-index to 1-index

        buildings.insert_at_beginning(heights[i], i)

    return result



if __name__ == "__main__":
    heights = []
    print("Enter 30 building heights:")
    for i in range(30):
        height = int(input(f"Enter height for building {i + 1}: "))
        heights.append(height)

    print("\nArray A (input heights):")
    print(heights)

    visible = find_visible_buildings(heights)

    print("\nVisible buildings or sea from each building:")
    for i, v in enumerate(visible):
        if v == 0:
            print(f"From building {i + 1}: Sea")
        else:
            print(f"From building {i + 1}: Building {v}")

    print("\nArray B (output):")
    print(visible)