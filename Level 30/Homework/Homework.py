#1

def find_item(item_list, item):
    if item in item_list:
        return True
    return False


#2

def max_item(num_list):
    return max(num_list)


#4

def increment_list(num_list):
    return [num + 1 for num in num_list]


#5


def reverse_string(word):
    return word[::-1]
