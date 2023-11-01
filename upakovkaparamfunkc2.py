def sort_numbers(*args):
    negative_numbers = sorted([num for num in args if num < 0], reverse=True)
    non_negative_numbers = sorted([num for num in args if num >= 0])
    return negative_numbers, non_negative_numbers

result = sort_numbers(5, -3, 10, -2, 0, -8, 7)
print(result)
