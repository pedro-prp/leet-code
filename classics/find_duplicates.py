def find_duplicates(numbers):
    
    counts_dict = {}

    duplicates_list = []

    for num in numbers:

        if num in counts_dict:
            counts_dict[num] = counts_dict[num] + 1
            duplicates_list.append(num)
        else:
            counts_dict[num] = 1

    return duplicates_list


print(find_duplicates([1, 2, 3, 2, 4, 5, 6, 6]))
