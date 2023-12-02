def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

def elements_in_list_a_not_in_list_b(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.difference(set_b)

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = common_elements(list1, list2)
print("Common elements:", common)

only_in_list1 = elements_in_list_a_not_in_list_b(list1, list2)
print("Elements in list1 but not in list2:", only_in_list1)
