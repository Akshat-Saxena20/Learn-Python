def swap_elements(lst, index1, index2):
    # Ensure the indices are within the bounds of the list
    if index1 >= len(lst) or index2 >= len(lst) or index1 < 0 or index2 < 0:
        raise IndexError("Index out of range")
    
    # Swap the elements
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
swapped_list = swap_elements(my_list, 1, 3)
print("List after swapping:", swapped_list)