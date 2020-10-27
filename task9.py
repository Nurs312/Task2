the_list = input('Enter any numbers: ').split()


def count(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return len(unique_list)

print(count(the_list))