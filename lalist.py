"""
List Operations Demonstration
"""

# Step 1: Create an empty list called my_list
my_list = []
print("Step 1 - Create empty list:")
print(f"my_list = {my_list}")
print()

# Step 2: Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Step 2 - Append 10, 20, 30, 40:")
print(f"my_list = {my_list}")
print(f"Current length: {len(my_list)}")
print()

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("Step 3 - Insert 15 at second position (index 1):")
print(f"my_list = {my_list}")
print(f"Element at index 1: {my_list[1]}")
print()

# Step 4: Extend with [50, 60, 70]
extension_list = [50, 60, 70]
my_list.extend(extension_list)
print("Step 4 - Extend with [50, 60, 70]:")
print(f"my_list = {my_list}")
print(f"Current length: {len(my_list)}")
print()

# Step 5: Remove the last element
removed_element = my_list.pop()
print("Step 5 - Remove last element:")
print(f"Removed element: {removed_element}")
print(f"my_list = {my_list}")
print()

# Step 6: Sort in ascending order
my_list.sort()
print("Step 6 - Sort in ascending order:")
print(f"my_list = {my_list}")
print()

# Step 7: Find index of value 30
value_to_find = 30
if value_to_find in my_list:
    index_position = my_list.index(value_to_find)
    print("Step 7 - Find index of value 30:")
    print(f"Value {value_to_find} found at index: {index_position}")
    print(f"Verification: my_list[{index_position}] = {my_list[index_position]}")
else:
    print(f"Value {value_to_find} not found in the list")
print()

# Final summary
print("=" * 50)
print("FINAL SUMMARY")
print("=" * 50)
print(f"Final list: {my_list}")
print(f"List length: {len(my_list)}")
print(f"List elements: {', '.join(map(str, my_list))}")
print(f"Sorted: {my_list == sorted(my_list)}")