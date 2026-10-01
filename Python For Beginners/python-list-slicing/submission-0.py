from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    new_list = []
    for x in range(-1,-4,-1):
        list_number = (my_list[x])
        new_list.append(list_number)
    return new_list[::-1]
        


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
